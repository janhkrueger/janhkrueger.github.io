Title: PostGres bei Uberspace
Date: 2013-11-11 15:49
Author: Jan H. Krüger
Tags: PostGres, Python, uberspace, Insulae

Einer der Gründe für Uberspace war für mich die Nutzung von PostGres.
Derzeit noch in der Betaphase ist es dennoch bereits nutzbar. Da ich
Anfangs ein paar Hürden hatte es vollständig einzurichten und in Betrieb
zu nehmen, hier eine kurze Anleitung.

Erster Anlaufpunkt ist die [Uberspace-Anleitung][] selbst. Die Anleitung
ist auch soweit gut durchzuarbeiten. Der erste Schritt aus der Anleitung
ist:

> uberspace-setup-postgresql

<span style="line-height: 21px;">Das Passwort für die nächsten Schritte
befindet sich
unter </span>**\~/.pgpass**<span style="line-height: 21px;">. Dieses
wirklich lange Teil, bedeutend länger wie das MySQL-Passwort welches
Uberspace initial vergibt. </span>Allerdings habe ich das nur für
die initiale Einrichtung meines eigentlichen Benutzers gebraucht.

Diesen habe ich wie folgt angelegt. Die Frage nach dem Passwort dieses
Benutzers folgt direkt nach der Befehlseingabe. Anschließend habe ich
die zugehörige Datenbank angelegt mit dem Benutzer aus dem ersten
Schritt. für createdb habe ich bereits das Passwort aus dem Schritt
craeteuser verwendet, nicht das Masterpasswort aus \~/.pgpass

> createuser -d -P -e jhk001\_insulae
>
> <span style="line-height: 21px;">createdb -e --encoding=UTF8
> --owner=jhk001\_insulae jhk001\_insulaedb</span>

Und nun habe ich bereits einen vorher per SFTP bereit gestellten Dump
eingespielt:

> psql -U jhk001\_insulae jhk001\_insulaedb \< insulae\_db.dump

Ein kurzer Test sagte mir hier bereits das die Daten angekommen waren
und genutzt werden können. Wäre da nicht noch die weitere Konfiguration
von PostGres auf Uberspace.

 

Zum einen muss PostGres wissen welche User von wo aus zugreifen dürfen.
Dazu dient ein Eintrag in der Datei **\~/postgresql/pg\_hba.conf** Bei
mir wurde es folgender Eintrag.

> local jhk001\_insulaedb jhk001\_insulae  password

Also ohne Hostangabe. Genau dies war auch der Punkt an dem ich mit dem
Support Kontakt aufnehmen musste. Meine ursprüngliche Einstellung beim
Host war falsch. An dieser Stelle nochmal Dank an die Kollegen von
Uberspace.

Als nächstes kam die Einstellung auf welchem Port PostGres lauscht dran.
Hierzu ist die Datei **\~/postgresql/postgresql.conf** zu bemühen und
die Einstellung bei "listen\_adresses" sowie "port" anzupassen. Meine
Konfiguration sieht nun wie folgt aus:

> \#listen\_addresses = ''  
>  listen\_addresses ='localhost' \# what IP address(es) to listen on;  
>  \# comma-separated list of addresses;  
>  \# defaults to 'localhost'; use '\*' for all  
>  \# (change requires restart)  
>  port = 64535                        \# (change requires restart)

Damit das weitere Arbeiten auf der Konsole weiterhin möglich ist kann
über die **\~/.bashrc** der Port definiert werden. Einfach folgende
Zeile dort ablegen:

> export PGPORT=64535

Nun ist es an der Zeit PostGres auch mal neu zu starten damit alle
Einstellungen auch gezogen werden. Hierzu reicht gemäß der Anleitung bei
Uberspace ein:

> svc -iu \~/service/postgresql

*Hinweis: Damit der Eintrag aus der \~/.bashrc auch gezogen wird ist
eine Neuanmeldung erforderlich!*

Damit sollte, wenn nichts schief geht, PostGres einsatzbereit sein.
Fehlt nur noch eine wichtige Angelegenheit. Das Backup. Auch hier
schreibt die Anleitung etwas dazu. Mittels eines einfachen Befehles wird
das Backup eingerichtet:

> uberspace-setup-postgresql-backup

Bei mir wurde das Verzeichnis "**\~/postgresql-backup/**" nicht
automatisch angelegt. Ich habe es daher per Hand angelegt. Da jeden
Abend dort etwas rein geschrieben wird scheint es ok zu sein. Offen nur
noch der Zeitpunkt wann das Backup ausgeführt werden soll. Dazu in die
durch das obige Skript angelegte Datei rein:

> nano \~/service/postgresql-backup/run

Die Einstellung bei **RUNWHEN=",H=[Stundenangabe]"** ist entsprechend
der eigenen Vorstellungen anzupassen. Ich lasse meine Datenbank um 3 Uhr
sichern weshalb der Eintrag auch wie folgt aussieht:

> RUNWHEN=",H=3"

 

Tjo, das war es eigentlich auch alles. Viel Spaß mit eurem PostGres!

 

Für mich selbst war es damit noch nicht getan. Ich hatte noch die
Anforderung das ich mit Python auf die Datenbank zugreifen kann. Seit
Jahren nutze ich dazu **psycopg**. Sehr erfreut war ich daher als ich
sah das ich dieses auch auf meinem Uberspace installieren kann. Die
entsprechende [Anleitung für die Installation von Pythonpackages][]
findet sich bei Uberspace.

Da ich Python in der Version 2.6 nutzen will habe ich dieses noch bereit
gestellt und gleich die weiteren Pakete installiert.

> mkdir -p \~/bin \~/lib/python2.4 \~/lib/python2.6  
>  easy\_install psycopg2  
>  easy\_install django  
>  pip install flup  
>  mkdir \~/html/static  
>  cp -a
> \~/lib/python2.6/Django-1.5.5-py2.6.egg/django/contrib/admin/static/admin/
> \~/html/static/

Der Test eines meiner Skripte führte dann auch zu einem positiven
Ergebnis. Daher: alles Läuft!

  [Uberspace-Anleitung]: https://uberspace.de/dokuwiki/database:postgresql
  [Anleitung für die Installation von Pythonpackages]: https://uberspace.de/dokuwiki/development:python
