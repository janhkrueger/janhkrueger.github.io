Title: EVE - Wechsel vom Raspberry
Date: 2014-03-05 15:52
Author: Jan H. Krüger
Category: Games
Tags: Datenauswertung, EVE, Raspberry Pi
Slug: eve-wechsel-vom-raspberry

Seit einiger Zeit bin ich dabei die Capitalkills in EVE Online zu
sammeln und auszuwerten. Doch mit der Zeit sammelt sich ein sehr großer
Datenbestand an.

<!--more-->Bisher konnte ich die Datensammlung recht gut auf meinem
Raspberry Pi unterbringen. Die Datenbank ist aktuell knapp 450MB groß.
Mit den 512MB RAM des kleinen Gerätes geht das noch so irgendwie. Will
ich jedoch Abfragen darauf tätigen hört es mittlerweile auch schon auf.
Der Kleine ist dafür einfach nicht geschaffen. Also, andere Lösung muss
her.

Zuerst habe ich alles auf meinen iMac gepackt. Schnelle CPU, 12GB RAM,
passt. Ist aber blöde wenn ich die zukünftigen Daten ermitteln will und
auch anderen zur Verfügung stellen. Meinen Rechner will ich ja nicht
rund um die Uhr an lassen und den Wartungsaufwand auch so gering wie
möglich halten.

Eine befriedigende Lösung habe ich noch nicht gefunden. Aktuell habe ich
alles in einer Datenbank bei meinem Webhoster Uberspace. Kann jedoch
auch keine dauerhafte Lösung sein. Denn die Auswertungen laufen unter
Umständen schon sehr lange. Da entsteht über einen längeren Zeitraum
(über eine halbe Stunde) stressende Last auf dem MySQL-Server. Muss ja
in einer Shared Hosting Umgebung nicht sein, schon aus Respekt den
anderen Nutzern gegenüber.

Ein System mit welchem ich BigData auswerten kann wäre genial. Doch
wirklich befriedigende Angebote habe ich aktuell noch nicht gefunden.
Googles SQL Clound mag ich nicht. Amazons Service auch nicht. Ich kann
nicht auf eine Art versuchen mich von großen, zentralen Firmen im Netz
unabhängiger zu bewegen wenn ich bei solchen Aufgaben dann wieder auf
ihre Dienste zurück greife.

Einen eigenen, dedizierten Server, Root-Server oder ähnliches mag ich
mich auch nicht zulegen. Ich bin mit Uberspace richtig zufrieden. Und
der Sprung hin zu einem Root Server ist preislich dann auch wieder so
eine Sache. Ich will ja im Grunde nur einen Datenbestand in annehmbarer
Zeit auswerten. Nein, sogar regelmäßig auswerten.

Ich füchte aktuell werde ich kritische Abfragen auf meinem Rechner
ausführen müssen und die Ergebnisse dann wieder auf meine
Onlineplattform zurück spielen. Unbefriedigend, aufwändig,
fehleranfällig. Wer eine probate Lösung kennt, bitte melden.
