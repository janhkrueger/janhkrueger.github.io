Title: EVE - Auswertung des zKillboards
Date: 2014-03-01 23:10
Author: Jan H. Krüger
Category: Games
Tags: Datenanalyse, Datenauswertung, EVE, Killboard, Python, Raspberry Pi
Slug: eve-auswertung-des-zkillboards

Im [eveger-Forum][eveger-Forum] tat sich vor kurzem ein interessantes Projekt auf.
Die Sammlung und Auswertung aller Verlust von Capitalschiffen. Etwas
perfektes für den hier noch rumliegenden Raspberry Pi :)

Es musste etwas geschaffen werden was eines oder die Killboards
ausliest. Eine kurze Recherche führte dazu das es bereits etwas
vergleichbares gibt. Über [K162space][K162space] bin ich auf das Projekt
von [@Lockefox][@Lockefox] (eve-prosper) gestoßen welches genau dies bereits
erledigt. Es nutzt die vom [zKillboard][zKillboard] bereit gestellten Daten. Naja,
ohne lange zu zögern habe ich das [GIT-Projekt][GIT-Projekt] geklont und mir
angeschaut. Erst einmal etwas verwirrend, Lockefox scheint alles erstmal
nur so in sein Repository zu werfen. Zumindest war es mir auch nicht
immer klar. Egal.

Der [KillReporter][KillReporter] ist genau das was ich gesucht habe. Notwendige
Vorbereitungen waren im Grunde nur das Einrichten einer MySQL-Datenbank
auf dem Pi

> `sudo apt-get install mysql`

Fertig. Python ist bereits unter Raspian vorhanden, da muss nichts
weiter unternommen werden. Es fehlte lediglich noch der Zusatz damit
Python auch mit MySQL reden kann.

> sudo apt-get install python-mysqldb

hat es für mich gerichtet.

Damit ist das ganze schon fast einsatzbereit.

DerKillReporter nutzt eine Datei zur Konfigurierung, **init.ini**
genannt.

<iframe style="border: none; width: 100%;" src="https://janhkrueger.de/stikked/view/embed/6b835ee7" height="240" width="320"></iframe>

Sieht die Datei bei mir aus. Im Grunde schon selbsterklärend. Relevant
sind die Einträge

> <span style="color: #444444; font-family: Helveticam, Arial, sans-serif; font-size: 13px; line-height: 21.450000762939453px;">db\_name=killdatenbank</span>  
>
> <span style="color: #444444; font-family: Helveticam, Arial, sans-serif; font-size: 13px; line-height: 21.450000762939453px;">db\_host=127.0.0.1</span>  
>
> <span style="color: #444444; font-family: Helveticam, Arial, sans-serif; font-size: 13px; line-height: 21.450000762939453px;">db\_user=killuser</span>  
>
> <span style="color: #444444; font-family: Helveticam, Arial, sans-serif; font-size: 13px; line-height: 21.450000762939453px;">db\_pw=passwortzudb</span>  
>
> <span style="color: #444444; font-family: Helveticam, Arial, sans-serif; font-size: 13px; line-height: 21.450000762939453px;">db\_port=3306</span>  
>
> <span style="color: #444444; font-family: Helveticam, Arial, sans-serif; font-size: 13px; line-height: 21.450000762939453px;">user\_agent
> = janhkrueger.de</span>

Damit steht der Killreporter auch schon für den ersten Einsatz bereit.
Erstmal völlig ohne weitere Betrachtung der erste Test ob alles läuft.
Also nun der Besuch auf der Konsole, der spannende Moment:

> python KillReporter.py

Und es läuft. Tada!

 

Dabei kamen dann zwei Engpässe auf. Das Skript von [@Lockefox][@Lockefox] knallt
gesammelte Kills erst einmal in den Speicher und schreibt zum Abschluss.
Unter Umständen können denn die 512MB RAM des Pi zu klein werden. Nein,
er wird mit der Zeit zu klein. Es musste also eine Lösung her.

Zuerst habe ich die abzufragenden Systeme eingegrenzt. Da uns primär die
Capitals interessieren kann der gesammte HighSec ausgespart werden. Dort
darf eh keines rumdüsen. Das entspannte das ganze etwas, war allerdings
immer noch nicht das wahre. Glücklicherweise hat [@Lockefox][@Lockefox] dies
alles auch schon berücksichtigt und noch zwei weitere Dateien zur
Konfiguration bereit gestellt. toaster\_shiplist.json
und toaster\_systemlist.json. In der einen wird definiert welche
Schiffsgruppen überhaupt abgefragt werden sollen, in der anderen welche
Systeme zu betrachten sind.

Somit habe ich mal ein paar Datenabfragen vorgenommen und S1dy zukommen
lassen. Befriedigend war die Auswertung für mich vom technischen Punkt
jedoch noch nicht. Zu viel Konsolengetippe für mich um zB Supercarrier
eines kompletten Jahres abzufragen.

Nach ein paar Überlegungen und einer kleinen Änderung im Originalskript
habe ich ein paar Shellskripte angelegt welche den Aufwand für mich so
gering wie möglich gestalten. Insgesamt habe ich folgendes umgesetzt:

-   Anpassungen im Skript um die Start und Endzeitpunkte parametrisiert
    zu übergeben. Im Original sind sie hart hinterlegt.
-   Entfernung unnötiger Ausgaben um das Konsolenfeedback so gering und
    interpretierbar zu gestalten wie ich es behaglich finde.
-   Erstellung eigener Shiplist-Dateien für jede zu betrachtende Gruppe.
    Also Carrier, Titanen etc.
-   Um dieses Konstrukt dann Shellskripte welche ein komplettes Jahr in
    5-Tages-Schritten für die jeweilige Schiffsklasse bearbeitet.

Das sieht dann zum Beispiel wie folgt aus:

<iframe style="border: none; width: 100%;" src="https://janhkrueger.de/stikked/view/embed/9b3da773" height="240" width="320"></iframe>

Das dort aufgerufene Skript selbst wiederrum enthält folgendes:

<iframe style="border: none; width: 100%;" src="https://janhkrueger.de/stikked/view/embed/922e7714" height="240" width="320"></iframe>

Tjoa, das war es im Grunde. S1dy regte dann im laufenden Prozess noch an
das wir, um alle Capitals und deren Piloten zu erwischen, wir auch die
Killmails von anderen Elementen betrachten müssen. Zum Beispiel jene
Killmails von Infrastructure Hubs bei denen Capitals mit beteiligt sind.

Gesagt getan, mittlerweile werden IHubs, SBUs, TCUs und Control Tower
ebenfalls genutzt. Resultat jetzt zu diesem Zeitpunkt habe ich die
folgenden Gruppen abgefragt mit Ausnahme der Controltower aus 2011. Hier
läuft die Abfrage noch:

-   Carrier
-   Control Tower
-   Dreadnought
-   Infrastructure Hub
-   Sovereignty Blockade Unit
-   Supercarrier
-   Territorial Claim Unit
-   Titan

Das ist schon ne ganze Menge. Zusätzlich ist nicht nur der Loss
gespeichert sondern auch wer an dem Kill beteiligt war.

Bei einer ersten Analyse fiel jedoch auch auf warum die Daten stets
ungenau sein werden. Nicht jeder Kill wird dem Killboard überhaupt
mitgeteilt. So sind zum Beispiel nicht alle Kills der erst kürzlich
erfolgten Megaschlacht bei B-R5RB dort vorhanden. Die Zahlen sind
insofern leicht zu kontrollieren gewesen da [CCP dieses mal selbst die
konkreten Verluste benannt hat][]. Gut, kann ich nicht ändern. Ist halt
so.

Offen sind nun vom rein technischen Standpunkt nur noch ein paar Punkte:

-   Automatisierung damit die Abfragen jede Woche von alleine starten
-   Anpassung des Skriptes damit ich keine Start- und Endeparameter
    mitgeben muss sondern immer die letzte Woche betrachtet wird.
-   Automatischer Export der Daten als CSV und SQL-Dateien

Der erste Punkte ist sehr einfach. Erfordert jedoch Punkt 2. Die
Anpassung des Skriptes dürfte dank der guten Datumsfunktionen in Python
auch nicht das Problem sein. Muss halt nur mal umgesetzt werden. Der
dritte Punkte ist von der reinen Durchführung auch harmlos. Jedoch
müssen die Dateien ja auch irgendwie zum Empfänger. Ein Frontend um auf
die Daten zuzugreifen möchte ich für externe nicht aufziehen. Also
bleibt nur die Daten statisch bereit zu stellen oder sie gar gleich auf
einen anderen Space hochladen. Da werde ich mir jedoch erst ganz zum
Schluss weitere Gedanken drum kreisen lassen.

Öffentlich sollen die Daten auf jeden Fall sein. So können auch andere
die Daten für sich verwenden und müssen nicht noch selbst das Killboard
mit ihren Abfragen belasten.

Und dann kann das eigentlich für mich Interessante beginnen.
Auswertungen auf den Datenbestand vornehmen :) Wenn ich die entsprechend
aufbereite lassen sich da sicherlich interessante Daten für die
Corp-Verwaltung ableiten um die Forschungen und die zu erstellenden
Verkaufsaufträge zu erstellen. Oder den Bestand an Archon-BPOs erhöhen,
wie erst kürzlich.

Allerdings ist ein Punkt jetzt bereits klar. Auswertungen können auf dem
kleinen Gerät nicht selbst erfolgen. Für diese Datenmengen ist der Pi zu
klein. Sowohl von seiner CPU wie auch vom Arbeitsspeicher her. Bedeutet
für mich das ich bevor ich eine Auswertung starten möchte ich womöglich
erst den aktuellen Datenbestand von Pi auf einen anderen Rechner ziehen
muss. Doch das ist ja die kleinste Übung.

Ach ja, sollte jemand interessiert sein das ganze selbst aufzubauen, die
von mir vorgenommenen Modifikationen sowie die Shellskripte habe ich
soeben online bereit gestellt. Bis ich etwas anderes gefunden habe wo ich den Code ablegen kann, dient 
~~GitHub~~, [mein eigenes Git-Repository ][SelfHostedGitRepo] auch wenn mir etwas self
hosted besser gefallen würde.

Dank im übrigen nochmals an S1dy welcher im evger-Forum die Thematik
überhaupt zur Sprache gebracht hat.

Quellen: [eveger][eveger-Forum], [K162Space][K162space],
[zKillBoard-API][zKillboard], [EVE Prosper][EVEProsper],

  [eveger-Forum]: http://www.eveger.de/forum/showthread.php?51938-Supercapitals-in-Eve
  [K162space]: http://k162space.com/2013/12/04/jump-freighter-kill-statistics/
  [@Lockefox]: https://twitter.com/HLIBIndustry
  [zKillboard]: https://zkillboard.com/information/api/
  [GIT-Projekt]: https://github.com/lockefox/
  [KillReporter]: https://github.com/lockefox/EVE-Prosper/tree/master/KillReporter
  [CCPVerluste]: http://community.eveonline.com/news/dev-blogs/the-bloodbath-of-b-r5rb/
  [SelfHostedGitRepo]: https://janhkrueger.de/gitpup/KillReporter.git/
  [EVEProsper]: http://eve-prosper.blogspot.de/
