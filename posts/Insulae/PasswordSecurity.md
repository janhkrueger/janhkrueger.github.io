Title: Insulae - Password security
Date: 2019-06-03 20:05
Author: Jan H. Krüger
Tags: Insulae, Zwischenstand, PBBG, Browsergame
Category: Insulae
Slug: insulae-passwordsecurity

Password security is always an important topic for IT-Systems and especially for systems being online. In the last years there have been rapid changes. GPUs are going to melt down the time to calculate passwords. Flaws in stablished algorithms are found, new algorithms are developed. Still, a burned password should not be used again. Or one that is used often.

The National Institute of Standards and Technologies (NIST) has issued a new version of their  "Digital Identity Guidelines". Ok, it's from december 2017. There you can read the following:

> "When processing requests to establish and change memorized secrets, verifiers SHALL compare the prospective secrets against a list that contains values known to be commonly-used, expected, or compromised." 

Given, I will never try to make Insulae full NIST compatible. Insulae is not intended to be used in any regulatory context. Still, there is nothing why I shouldn't give a warning that a password is already used somewhere or even already burned. On common issues is reusing passwords.

To check if a passort is affected by a previous data breach [Troy Hunt][2] provides an API to check for such passwords. Alternatively you can download the entire database with the hashes for the people who don't want to rely on external services.

Since the weekend Insulae is now connected to the database provided by Troy Hunt. I have choosen to host the database in my own infrastructure and not to ask external services. Thus the approach of having as much as possible under one's own control and having as little reliance as possible on external services is also fulfilled here.
Upon every password change the desired password is not checked against the database. Not only check it and give a warning but indeed deny setting it. Yes, uncomfortable. But hey, it's your accounts!
I will not going to check current passwords against the database. First, all passwords are stored only salted and peppered so I have no way to check against the original password. Second, in 90 days it should be solved naturally.

So, what's needed to do do use the password hashes Troy Hunt provides?

First, create a new schema and a table for the hashes:

```
== Create schema and database
CREATE SCHEMA pawneddb;
CREATE TABLE pawneddb.hashes ( id bigserial PRIMARY KEY, hash bytea);
CREATE INDEX ON pawneddb.hashes (substring(hash for 7));
```

Next I can load the hashes into the database:

```
== Load Password Hashes
sed -r 's/(.{40}).*/\1/' pwned-passwords-sha1-ordered-by-hash-v4.txt | sed -e 's/^/\\\\x/' | time psql -h 172.19.0.10 -U insulae_user insulae_db -c "copy pawneddb.hashes (hash) from STDIN WITH DELIMITER ':'"
```

I only look at the first 40 characters of the source file. In the source there is also a count how often a password is affected. This is not relevant in any way for my use case, I'm only interested if a password us affected by a data breach. Further, the hash is defined as hex so I can used the bytea data type in PostgreSQL. The loading can take some time depending on the file system and the database. The source file is around 24GB, in the database it should be something like 57GB.

So, to check if a specific hash is already in the database I do the following:

```
=== Definition Function
prepare pw_lookup (bytea) as select * from pawneddb.hashes WHERE substring(hash for 7) = substring($1 for 7) and hash = $1;

=== Check password against the database
execute pw_lookup(pawneddb.digest('passwort','sha1'));
```

The initial prepare-query comes from [Lukas Erlacher][1]

If there is a hit the password is affected by a previous known breach and should be declined. At least the player should be informed that the password is not considered safe anymore.

A short info. The used sha1 algorithm is not the one used for Insulae but the one Troy uses with his hash database. He is not hands out the passwords itself but only hashed ones. In Insulae I use Argon2. This one has won the Password Hashing Competition in 2015.

The query time with this mass of data, somewhat over half a billion, is absolutely acceptable on my system. With currently 1200 players and projected up to 3000 max on the current server I can work this way under the current feature map without negative impacts to the entire system.

```
                                                          QUERY PLAN                                                                                                                                               
------------------------------------------------------------------------------------------------------------------------------                                                                                     
 Index Scan using hashes_substring_idx on hashes  (cost=0.57..8.59 rows=1 width=29) (actual time=0.057..0.057 rows=1 loops=1)                                                                                      
   Index Cond: ("substring"(hash, 1, 7) = '\xf3390fe2e5546d'::bytea)                                                                                                                                               
   Filter: (hash = '\xf3390fe2e5546dac3d1968970df1a222a3a39c00'::bytea)                                                                                                                                            
 Planning Time: 0.112 ms                                                                                                                                                                                           
 Execution Time: 0.066 ms                                                                                                                                                                                          
(5 rows)
```


Regarding the hashed data one comment. In v4 of the source file there are 551.510.000 entries. This results in adminer in my system to a data size if 33,2GB and an index size of 24,7.
Currently the hashes are stored in a dedicated schema in the main database of insulae. Because it is quit big and is not in any way native data of Insulae I will separate in a second database. Also I will put a a small REST service to query the data. This will be closer to my intened target picture of the infrastructure.

For the time being I have excludet the table from the daily database backup with an `--exclude-table-data=hashes`. Yes, if something is going to explode I have to reload the data. So what, this time I will take. Perhaps there will be a new hash file and I have to reload anyways.


A big thank you to Troy for his amazing work and [Stefán Jökull Sigurðarson][3] for constantly reminding me with his posts for "Do it also for your stuff!" 


[1]: http://www.lerlacher.de/posts/2017-10-26-pwned-passwords.en.html
[2]: https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/
[3]: https://twitter.com/stebets
