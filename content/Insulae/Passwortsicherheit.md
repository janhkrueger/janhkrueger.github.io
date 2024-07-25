Title: Insulae - Passwortsicherheit
Date: 2019-06-03 20:05
Author: Jan H. Krüger
Tags: Insulae, Zwischenstand, PBBG, Browsergame
Category: Insulae
Slug: insulae-passwortsicherheit
Series: Insulae-Stand

Passwortsicherheit ist immer ein wichtiges Thema für IT-Systeme und insbesondere für online bereit gestellte Dienste. In den letzten Jahren hat sich an der Front auch viel getan. GPUs lassen stetig die Zeit schrumpfen um ein Passwort zu errechnen, in etablierten Algorithmen werden Lücken entdeckt, gleichzeitig werden auch stets neue Algorithmen entwickelt.
Dennoch bleibt, ein verbranntes Passwort sollte nicht wieder genutzt werden. Auch kein häufig verwendetes.

Das National Institute of Standards and Technologies (NIST) hat dazu mitterweile auch sogar "Digital Identity Guidelines". Ok, Im Dezember 2017. Darin findet sich unter anderem:

> "When processing requests to establish and change memorized secrets, verifiers SHALL compare the prospective secrets against a list that contains values known to be commonly-used, expected, or compromised." 

Zugegeben, Insulae werde ich nie versuchen NIST konform zu halten. Es wird nie erstrebt Insulae in einem Regierungskontext anzuwenden. Dennoch, es spricht auch nichts dagegen an dieser Stelle darauf hinzuweisen das ein Passwort schon woanders eingesetzt wird. Eines der häufigsten Probleme ist unter anderem die Wiederverwendung von Passwörtern.

Um nun zu überprüfen ob ein Passwort schon einem Einbruch entwendet wurde stellt [Troy Hunt][2] eine API bereit in welcher dies überprüft werden kann. Alternativ steht die Datenbank mit den Hashwerten auch zum Download zur Verfügung für jene welche hierfür nicht auf einen externen Dienst angewiesen sein wollen.

Seit dem Wochenende ist Insulae auch an die Datenbank von Troy Hunt angebunden. Ich habe mich dafür entschieden die Datenbank selbst in meiner Infrastruktur zu hosten und nicht jedesmal externe Dienste abzufragen. Damit ist auch hier der Ansatz, möglichst viel in Eigenregie zu haben und möglichst wenig auf externe Dienste angewiesen zu sein erfüllt. Bei jedem Passwortwechsel wird nun das Passwort überprüft, Ich habe mich entschieden ein solches Passwort dann auch hart abzulehnen und nicht nur darauf hinzuweisen. Ja, mag unbequem sein. Aber hey, geht um eure Accounts. Nicht erfolgen wird eine Überprüfung der bestehenden Passwörter. Zum einen sind die Passwörter eh nur noch gesalzen und gepfeffert gespeichert, zum anderen werden sich die alten Passwörter spätestens in 90 Tagen sowieso ausgewachsen haben.


Was ist nun zu unternehmen um die Passworthashes von Troy Hunt zu verwenden?

Zuerst ein neues Schema und eine Tabelle für die Passwort Hashes anlegen:


```
== Create schema and database
CREATE SCHEMA pawneddb;
CREATE TABLE pawneddb.hashes ( id bigserial PRIMARY KEY, hash bytea);
CREATE INDEX ON pawneddb.hashes (substring(hash for 7));
```


Anschließend kann ich die Daten in die Datenbank laden.

```
== Load Password Hashes
sed -r 's/(.{40}).*/\1/' pwned-passwords-sha1-ordered-by-hash-v4.txt | sed -e 's/^/\\\\x/' | time psql -h 172.19.0.10 -U insulae_user insulae_db -c "copy pawneddb.hashes (hash) from STDIN WITH DELIMITER ':'"
```



Hiermit betrachte ich nur die ersten 40 Zeichen in der Datei. In der Quelle wird neben jedem Hash auch die Anzahl der Funde mit angegeben. Die Anzahl der Funde ist für meinen Anwendungszweck allerdings nicht relevant, da interessiert nur ob das Passwort bereits verbrannt ist oder nicht. Weiterhin wird der Hash als Hex definiert damit in der Datenbank der Datentyp bytea genutzt werden kann. Das Laden kann etwas dauern abhängig vom Filesystem und der Datenbank. Die Rohdaten sind ca 24GB derzeit, in der Datenbank selbst werden es 56GB sein.

Möchte ich nun prüfen ob ein spezieller Hash bereits vorhanden ist, kann wie folgt vorgegangen werden.


```
=== Definition Function
prepare pw_lookup (bytea) as select * from pawneddb.hashes WHERE substring(hash for 7) = substring($1 for 7) and hash = $1;

=== Passwort gegen die Hashdatenbank prüfen.
execute pw_lookup(pawneddb.digest('passwort','sha1'));
```

Die prepare-Anweisung stammt von [Lukas Erlacher][1]


Sollte hier ein Treffer existieren so ist das Passwort in einem vorherigen Breach bereits verwendet worden und sollte daher abgelehnt werden. Mindestens muss der Spieler eine Information erhalten das das gewählte Passwort bereits verbrannt ist.
Auch hier der Hinweis. Der verwendete sha1 ist nicht jener welcher für die Speicherung der Passwörter in Insulae genutzt wird sondern die Passwörter werden von Toy nicht im Klartext veröffentlicht sondern nur als sha1. Ich verwende Argon2. Dieser gewann 2015 die Password Hashing Competition.

Die Abfragezeit bei der Masse an Daten, etwas über eine halbe Milliarde Einträge, ist auf meinem System auch noch absolut erträglich. Bei derzeit 1200 Nutzern und hochgerechnet maximal 3000 auf meiner Plattform beim aktuellem Funktionsumfang ist das etwas was die Gesamtperformance des Systemes nicht negativ beeinflussen wird.

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

Bezüglich der Hashdaten noch eine Anmerkung. In v4 des Datensatzes liefert Troy Hunt 551.510.000 Sätze. Das bedeuted bei mir laut Adminer eine Datasize von 33,2 und eine Indexsize von 24,7GB.
Derzeit liegt die Passwortdatenbank als separates Schema in der Datenbank von Insulae. Da sie doch recht groß ist und nativ nicht zu Insulae gehört werde ich sie in eine eigene Datenbank auslagern. Der Zugriff hat dann über eine REST-API zu erfolgen und wäre damit noch näher an meinem Zielbild der Infrastruktur.

Für das erste habe ich mit einem `--exclude-table-data=hashes` die Tabelle aus dem Backup ausgenommen. Ja, sollte etwas explodieren muss ich die Daten neu einladen. Aber so what. Die Zeit muss sein. Bis dahin gibt es ggf. auch schon eine neue Version der Hashdatei.




[1]: http://www.lerlacher.de/posts/2017-10-26-pwned-passwords.en.html
[2]: https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/


