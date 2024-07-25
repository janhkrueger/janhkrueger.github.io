Title: EVE - Auswertung Killboard - Nachtrag
Date: 2014-03-12 17:42
Author: Jan H. Krüger
Category: Games
Tags: Datenanalyse, EVE, EVE Online, Killboard
Slug: eve-auswertung-killboard-nachtrag

Ich muss gerade feststellen das die Auswertung spürbar negative
Auswirkungen auf den Rest des Betriebes hat. Wenn meine Vermutung
richtig ist, dann wird im Scraperskript nicht korrekt die
Datenbankverbindung abgebaut.

Ich erhalte, auch von anderen Prozessen, die Meldung das mein User die
maximale Anzahl an erlaubten Verbindungen aufgebaut hat. Kurz: Mist!

Als ersten Punkt konnte ich vorhin schonmal sicherstellen das bei meinem
Verwaltungstool für die Corp am Ende definitiv die Verbindung
geschlossen wird. Kann das ganze natürlich nur temporär lösen. Zumal die
dortigen aufgebauten Verbindungen eigentlich vorher schon korrekt
beendet werden sollten. Mal sehen.

Dabei ist mir noch etwas anderes aufgefallen. Die Laufzeit des Skriptes
ist bei größerer Datenbank mittlerweile grottig. Liegt insbesondere
daran wenn der Bestand durchsucht werden muss um einen bereits
vorhandenen Kill zu aktualisieren. Hier tritt der nächste Punkt zu Tage,
da muss ich mir die Indizies optimieren.

Für das erste musste ich mich damit begnügen auf der Datenbank zu prüfen
welche Prozesse da noch aktiv sind und diese nach einer Prüfung hart zu
beenden:

> <div id="magicdomid108">
> SHOW PROCESSLIST;
> </div>
> <div id="magicdomid124">
> KILL [ID];
> </div>

<div>
Nach einer Kontrolle kann ich nun sagen, in meinem Verwaltungstool
bleiben keine Verbindungen mehr offen.

</div>
<div>
Bleiben zwei Schritte über: Optimierung der Datenbank im Hinblick auf
Indizes und die bereits eingerichtete Partitionierung.

</div>
<div>
</div>
<div>
Das sinnvollste wird sein die Sicherung der nächsten Nacht zu nehmen und
bei mir lokal einzuspielen um dort die Optimierungen vorzunehmen. Und
das Skript genau zu durchforsten ob eventuell die Verbindungen wirklich
nicht abgebaut werden.

</div>
<div>
</div>

