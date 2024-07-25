Title: EVE - Bereitstellung der KillReports
Date: 2014-03-11 17:57
Author: Jan H. Krüger
Category: Games
Tags: Datenauswertung, EVE, Killmails
Slug: eve-bereitstellung-der-killreports

Eine kleine Änderung bei der Bereitstellung der bisherigen Killreports.

Den Datenbestand aus dem [Git Repository][] habe ich entfernt. Muss dort
nicht rein. Dafür wird nun täglich automatisiert der \*gesamte\* Bestand
bereit gestellt.

Und zwar unter [http://janhkrueger.de/KillReports/][] in der Datei
"KR\_participants.sql.xz". Das ist ein regulärer MySQL-Dump welcher noch
gepackt wurde. Kann also direkt in jede andere MySQL-Datenbank
eingespielt werden um darauf aufbauend weiterführende Aufgaben
durchzuführen.

Jede Nacht um 03:35 Uhr wird die tägliche Sicherung rüberkopiert und
über das oben genannte Verzeichnis bereit gestellt.

  [Git Repository]: http://janhkrueger.de/gitpup/
  [http://janhkrueger.de/KillReports/]: http://janhkrueger.de/KillReports/
