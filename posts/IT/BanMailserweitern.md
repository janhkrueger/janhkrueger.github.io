Title: Mails von Fail2Ban mit weiteren Inhalten anreichern
Date: 2015-01-24 12:36
Author: Jan H. Krüger
Tags: Fail2Ban, BruteForce, Server, Abwehr

Wie quasi bei jeder Hardware welche am Internet hängt wird auch mein Server jeden Tag damit konfrontiert das Reihenweise Angriffe mittels Bruteforce gefahren werden.
An sich vergleichsweise harmlos.

Um das ganze jedoch etwas einzudämmen verwende ich Fail2Ban. Eine einfache und dennoch effektive Software um eben solche Angreifer fernzuhalten. Wie funktioniert es? Fail2Ban behält die Protokolldateien von verschiedenen Diensten im Auge. Taucht eine IP-Adresse dort innerhalb eines wählbaren Zeitraumes zu oft auf wird diese Adresse mittels iptables für einen wählbaren Zeitraum gesperrt. Der Quellrechner kann keine Verbindung mehr mit meinem Server aufnehmen.

Fail2Ban blockiert die angreifenden Quellrechner jedoch nur für einen bestimmte Zeit. Im Laufe der Monate geschieht es dann das sich die Angreifer mit der Zeit wiederholen. Die Adressen kommen mir mit der Zeit doch sehr vertraut vor.
Jetzt könnte ich einfach den Zeitraum der Blockade erhöhen. Will ich aus diversen Gründen nicht. Jedoch die "Dauergäste", die will ich einfach auch dauerhaft aussperren. Auch nach einem Serverneustart. Und ich will sie eindeutig identifizieren, als 

Den ersten Punkt löse ich mittels zweier Shellskripte. Das eine ist eine simple Sammlung von Anweisungen für iptables mit zu blockenden Adressen. Dieses Skript wird automatisch bei einem Serverneustart aktiviert. An dieser Seite ist danach alles erledigt.

Das zweite kümmert sich darum Eingaben welche ich tätige an das erste Skript anzuhängen. Einfach aufrufen, die zu sperrenden IP-Adresse als Parameter anhängen. Das sieht dann in etwa so aus:

<iframe src="https://janhkrueger.de/stikked/view/embed/890769e9" style="border:none;width:100%"></iframe>

Daraus resultiert folgende Datei:

<iframe src="https://janhkrueger.de/stikked/view/embed/98e51b4e" style="border:none;width:100%"></iframe>

Nun noch die Initalisieurungsdatei bei einem Neustart ausführen lassen:
    @reboot /path/to/iptablesAddNumbers.sh

So. Damit ist bereits der Punkt erledigt das die Dauergäste auch dauerhaft gesperrt bleiben. Offen der Punkt das ich auch sicher gehen will nur die wirklichen Problemfälle so zu behandeln. Fail2Ban führt, sofern entsprechend konfiguriert, ein whois auf die Adresse aus. Mag unfair sein, doch Adressen aus China zum Beispiel blockiere ich ohne weiter zu prüfen. Für alle anderen gibt es im Internet ein gutes Angebot an Seiten um solches zu prüfen. Als Beispiel sei http://www.tcpiputils.com/browse/ip-address/89.163.224.14 genannt.

Jetzt will ich ja auch nicht jedesmal selbst die Seiten eingeben und die zu prüfende Adresse anhängen. Ausserdem sendet mir Fail2Ban sowieso eine Mail wenn es eine Adresse sperrt. Also, was liegt näher in diese Mail noch weitere Inhalte aufzunehmen? Die dafür zuständige Datei lautet: /etc/fail2ban/action.d/sendmail-whois.conf
Zumindest bei mir unter CentOS6.

In dieser Datei findet sich ein Abschnitt "actionban". Dies ist der interessante Bereich. Hier nun ein paar Anpassungen und schon steht in der Mail von Fail2Ban ein direkter Link zu tcpiputils oder spamhaus:

<iframe src="https://janhkrueger.de/stikked/view/embed/292fb8e6" style="border:none;width:100%"></iframe>

Das war es auch schon. Jetzt finden sich die Links zu den Seiten mit denen ich die IP-Adressen überprüfe direkt in den Mails und ich muss nur noch klicken.