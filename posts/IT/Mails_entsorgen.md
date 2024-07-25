Title: Emails serverseitig nach Alter entsorgen
Date: 2014-06-18 21:46
Author: Jan H. Krüger
Category: IT
Tags: Maildir, Entsorgen, Automatisierung, Linux, Maildir
Slug: emails-serverseitig-nach-alter-entsorgen

Der Mailclient Thunderbird besitzt eine wie ich finde sehr praktische Funktion: Emails nach Alter entsorgen. Sie hat leider einen Haken. Nutze ich kein Thunderbird sondern zum Beispiel mal meinen Webclient werden keine alten Mails entsorgt. Und was Thunderbird kann, muss ja auch irgendwie serverseitig auch gehen.

<!--more-->

Also suchte ich eine Weile und wurde tatsächlich fündig. Vor vier Jahren hat **Fred Wenzel** dies bereits gelöst und der Welt per [Github geteilt][1]. Oder zumindest hat er zu diesem Zeitpunkt das ganze in seinem öffentlichem Repository eingecheckt. 
Das ganze ist ein recht geschmeidiges Pythonskript. Was es für mich noch sympatischer gestaltete da ich so nichts weiter installieren musste. Python habe ich eh auf meinem Server am Laufen. Doch hier nochmal der Hinweis: es werden Postfächer im **Maildir**-Format bearbeitet.

Das Skript kann einfach kopiert werden, eine Instalation entfällt. Im Header sind vorbildlich alle Optionen gelistet. Wer sich unsicher ist kann das Skript zuerst mittels *`--trial-run`* starten. Das Skript listet so nur auf was es abarbeiten würde doch führt keine Änderungen durch.

Ein Beispielhafter Aufruf sieht bei mir nun wie folgt aus: 

    cleanup-maildir.py --quiet --age=30 --keep-flagged-threads --maildir-root=/var/Maildir/ delete 'Mailordner'

Die Parameter bedeuten konkret:

*   `--quit` keine der üblichen Ausgaben 
*   `--age=30` Mails älter 30 Tage 
*   `-- keep-flagged-threads` Behalte Threads in denen eine Mail als wichtig markiert wurde
*   `--maildir-root`  Wo das zu suchende Maildirverzeichnis zu finden ist
*   `delete` die Mails sollen gelöscht werden 
*   `'Mailordner'` der spezifische Ordner im Postfach


Das war es auch schon. Das Skript nun noch für alle relevanten Ordner in ein Shellskript packen und dieses dann per Cronjob täglich ausführen lassen. Fertig ist die automatische Entsorgung alter Emails.

Um das Skript auch in Zukunft noch direkt im Zugriff zu haben ist es von mir in meinem [Git Repository][2] übernommen worden.


Quelle: [Fred Wenzels Repository][1]

[1]: https://gist.github.com/fwenzel/280896
[2]: http://janhkrueger.de/gitpup/cleaningmaildir/	

