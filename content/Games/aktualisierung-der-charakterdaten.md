Title: Aktualisierung der Charakterdaten
Date: 2014-03-19 12:36
Author: Jan H. Krüger
Category: Games
Tags: API, Charakter Updates, EVE, EVE Online
Slug: aktualisierung-der-charakterdaten

Bei der Abfrage der KillMails und deren Auswertung ist uns schon früh
ein Manko aufgefallen welches wir alsbald angehen wollten. Nachdem nun
die Abfrage der KillMails vollständig automatisiert abläuft hatte ich
Zeit mich darum zu kümmern.

Konkret besteht bei den KillMails folgendes Problem: die Charaktere
werden mit ihren Corporations und Allianzen gespeichert. Zum Zeitpunkt
des Kills. Das diese Charaktere jedoch mittlerweile schon längst
woanders angeheuert haben kann durch die Momentaufnahme einer KillMail
nicht wiedergespiegelt werden. Also habe ich nach einem Mechanismus
gesucht um die derzeitige Zugehörigkeit eines Charakters zu ermitteln.

Als erstes eine Tabelle in welche ich die Charaktere mit ihrer ID
speichere damit ich diese dann nach und nach abarbeiten kann:

<iframe style="border: none; width: 100%;" src="https://janhkrueger.de/stikked/view/embed/9c5e6118" height="240" width="320"></iframe>

So, Grundgerüst steht, fehlt eine Initialbefüllung. Da nehme ich mir
einfach mal alle Charaktere in der Tabelle **KR\_participants**.  

<iframe style="border: none; width: 100%;" src="https://janhkrueger.de/stikked/view/embed/b931934e" height="240" width="320"></iframe>  
Fertig. Jede Menge characterIDs welche bearbeitet werden müssen.

Um an die aktuellen Daten zu gelangen, nutze ich die API von EVE, die  
`https://api.eveonline.com/eve/CharacterInfo.xml.aspx?characterID=`  
Damit erhalte ich fast genau das was ich möchte. Eher sogar zu viel.
Dabei gibt es dann ein paar Punkte zu berücksichtigen.

Zum einen kann es passieren das ein Charakter gar nicht mehr
exisistiert. Die API liefert dann ein Meldung einer ungültigen ID aus.
Soll das Skript ja nicht an einer solchen Grenze scheitern. Daher wird
im Skript darauf abgeprüft. Existert ein Charakter nicht mehr, wird er
darüber hinaus im Feld **lastUpdate** entsprechend gekennzeichnet damit
ich diese ID nicht mehr von der API abfrage. Gesetzt wird in diesem Fall
das Datum **2099-01-01**. Entsprechend weit in der Zukunft. Ich glaube
zum einen nicht das EVE bis dahin existieren wird, zum anderen werde ich
dieses Datum wohl auch nicht erleben.

Joa, dann ist es im Grunde recht einfach. Daten aus der API werden
übernommen und entweder komplett neu eingefügt oder die bestehenden
Daten aktualisiert. Die aktuelle Version befindet sich im Anhang. Das
Skript bedarf noch ein wenig poliererei, insbesondere im Bezug auf das
Fehlerhandling. Bisher ist nichts passiert doch da sind jede Menge
Punkte welche einen Fehler werfen könnten.

In der Konfigurationsdaten wurden dafür zwei neue Parameter aufgenommen.
Zum einen der Name der Tabelle. Kann ja sein das jemand den mal Anpassen
will. Zum anderen die Anzahl der Chars welche in einem Rutsch von CCP
angefragt werden sollen.

Derzeit aktualisiere ich so alle 20 Minuten 100 weitere Charaktere.
Nicht viel, dessen bin ich mir bewusst. Es geht ja nur auch um einen
schonungsvollen Umgang mit der API. Das ganze wäre wohl einfacher wenn
der öffentliche CREST-Endpoint con CCP Foxfour frei verfügbar wäre.
Damit ist es auch möglich Massendaten abzufragen. Aber hey, bis dahin
halt so.

<iframe style="border: none; width: 100%;" src="https://janhkrueger.de/stikked/view/embed/42d96cc1" height="240" width="320"></iframe>

Wie üblich findet sich das Skript auch im [Repository][].

Im täglichen Datenexport werden die aktuellen Charakterdaten ab sofort
mitgeliefert. Als hübsche, kleine CSV-Daten mit dem Namen
[characters.csv][] Aktuell enthält diese 5561 Charaktere. Stetig
steigend. Wo lang nochmal die Grenze für Excel Daten anzuzeigen? Liegt
die immer noch bei 64 Tausend?

Blick in die Zukunft
--------------------

Ich könnte dabei nun aufhören. Wäre jedoch etwas blöd, das ganze ist
noch nicht "rund" in meinen Augen. Da müssen noch ein paar Punkte getan
werden.

-   Aktualisierung bei Killboardabfrage
-   Fehlerhandling
-   Umstellung auf CREST
-   Abfrage alter Charaktere

Aktualisierung bei Killboardabfrage
-----------------------------------

In der nächsten Iteration soll die Funktionalität die Daten zu
aktualisieren gleich in den Scraper für das KillBoard eingebaut werden.
Somit sollen die Daten dann von alleine aktuell gehalten sowie neue
Charaktere gleich in die Tabelle eingetragen werden.

Fehlerhandling
--------------

Hatte ich vorhin schon mal angesprochen. Es gibt noch zu viele Punkte
bei denen das Skript einfach abbrechen könnte.

Umstellung auf CREST
--------------------

Da muss ich zugegebenerweise warten bis CCP die API frei gibt. Doch dann
wird es leichter und bequemer die Daten zu erhalten welche hierfür
erforderlich sind.

Abfrage alter Charaktere
------------------------

Da es auch vorkommen kann das ein Charakter länger nicht mehr an einem
Kampf teilnimmt, würde er über eine Aktualisiert per Scraperskript nicht
erfasst. Daher muss ich mir noch einen Intervall überlegen um Charaktere
gemäß **lastUpdate** zu aktualisieren. Aktuell schwebt mir so einmal im
Monat vor. Doch das muss ich mir dann konkret einmal anschauen.

 

Kurz: Ja, es gibt noch genug zu erledigt :)

  [Repository]: http://janhkrueger.de/gitpup/?p=KillReporter.git
  [characters.csv]: http://janhkrueger.de/KillReports/characters.csv
