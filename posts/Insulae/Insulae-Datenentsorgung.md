Title: Datenentsorgung
Date: 2015-01-09 13:04
Author: Jan H. Krüger
Tags: Insulae, Datenentsorgung, Statistiken


Über die Zeit hinweg sammeln sich in Insulae doch so einige Daten an welche, bei einer Betrachtung des Zeitstrahles, irgendwann nicht mehr notwendig werden. Bisher habe ich da noch keine Zeit investiert um dem nachzugehen. Sprich, ich habe noch nichts weiter implementiert.

Im Zuge der Umstellungen auf C++ und der wieder stärkeren Beschäftigung mit Insulae wurde das Thema jedoch auch wieder notwendig. Zum Hintergrund: ich erhebe automatisiert eine ganze Reihe von Daten welche mir den Betrieb von Insulae erleichtern. Das sind zum einen aktuelle Statistiken über die Verteilung von Gebäuden, Berufen und so. Jedoch auch reine Protokolldaten. Wann welche Skripte gelaufen sind, wann sich Spieler eingeloggt haben. Infos über die Auslastung von CPU, Datenbank und sowas.

Daher habe ich die Tage daran gearbeitet hier Entsorgungen vorzunehmen. Je nach Kategorie werden die Inhalte nun nur noch ein Jahr bis zu fünf Jahre aufbewahrt. Ausnahme bilden die Datensammlungen über die Verteilung von Gebäuden etc. Die Daten stelle ich ja auch meinen Spielern zur Verfügung damit diese eigene Auswertungen darauf basierend fahren können.
Aktuell hab ich diese Entsorgungen als Triggerfunktion gelöst welche nach einem Insert gestartet wird. Das macht es für mich in sofern elegant als das es kein separates Programm benötigt und die Lastverteilung über die Zeitspanne auch recht gering ausfällt. Das werde ich mir jedoch nochmal weiter anschauen.