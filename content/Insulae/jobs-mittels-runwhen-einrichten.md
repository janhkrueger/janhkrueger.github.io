Title: Jobs mittels RUNWHEN einrichten
Date: 2013-11-14 03:26
Author: Jan H. Krüger
Category: Insulae
Tags: Insulae, RUNWHEN, uberspace
Slug: jobs-mittels-runwhen-einrichten

<span style="line-height: 21px;">Da Uberspace RUNWHEN empfiehlt habe ich
die regelmäßigen Jobs von Insulae damit eingerichtet. Ist auch kein
Hexenwerk. Kleines Beispiel am Skript welches allen Gebäudeinsassen ihre
Erfahrungspunkte zuteilt.</span>

> runwhen-conf \~/etc/insulae/run-xp-gebaeude "python
> \~/clouddata/repinsulae/batch/xp\_gebaeude.py"

Zeit angeben wann das Skript ausgeführt werden soll:

> nano \~/etc/insulae/run-xp-gebaeude/run

Und den Service aktivieren:

> ln -s \~/etc/insulae/run-xp-gebaeude \~/service

Fertig. Das war es schon, ab sofort läuft die tägliche Verarbeitung
wieder ohne mein zutun.

 

Die Kontrolle ob ein Lauf auch ausgeführt wurde bzw. wann der nächste
ansteht kann mit folgendem Kommando erfolgen:

> tail \~/service/run-xp-gebaeude/log/main/current | tai64nlocal

 

Ergibt bei mir unter der aktuellen Einstellung:

> 2013-11-11 16:22:29.071616500 next run time: 2013-11-12
> 15:15:50.000000000

 

Selbstverständlich kann der Job auch manuell gestartet werden, so ausser
der Reihe. Gerade für den Test, ob Einrichtung oder Einbau neuer
Features sehr praktisch. Dieser Aufruf im Gegensatz zum direkten Call
von python hat den Vorteil das ich so direkt erlebe wie das Skript sich
auch produktiv verhält.

> svc -a \~/service/run-xp-gebaeude

 

Quelle: [Uberspace][]

  [Uberspace]: http://uberspace.de/dokuwiki/system:runwhen
