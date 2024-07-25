Title: YOURLS am nach Hause telefonieren hindern
Date: 2014-03-04 15:17
Author: Jan H. Krüger
Category: IT
Tags: #ethomephone, SelfHosted, YOURLS
Slug: yourls-am-nach-hause-telefonieren-hindern

Ich bin ja ein Riesenfreund der Shortender-Anwendung YOURLS. Doch ein
Pukt stößt mir gerade nach einem Update sauer auf. Die Software
kommuniziert per Default an den Hersteller. Ein NoGo!

<!--more-->

Vor ein paar Minuten habe ich für mich das Update von 1.51 auf 1.7
durchgeführt. Soweit so gut. Ich freue mich über die aktive Entwicklung
von YOURLS. Doch der Umstieg wird teilweise konterkariert wenn die
Software nach Hause telefoniert und Daten weiterleitet.

Der Umfang der Daten ist auf der ersten Blick wohl harmlos, auf den
zweite denke ich auch. Eher die Art wie diese Funktion eingeführt wird.
Nämlich ist diese Punkt per Default aktiv. Sensibel wäre gewesen, den
Nutzern welche ihre Daten dem Projekt beisteuern wollen die Möglichkeit
zu gebe dies optional zu aktivieren.

So ist es für mich notwendig dies manuell zu deaktivieren. Fairerweise
ist zu sagen, wie dies zu erledigen ist liefert der Hersteller gleich
selbst, in seinem [Blog][] in welchem über die Änderung gesprochen wird.
Wird auch direkt mit "*But, you know, privacy!?*" betitelt. Die
Entwickler sind sich also durchaus bewusst das dies nicht jedermann
behagt.

Anzupassen ist die zentrale Konfigurationsdatei `config.php`. Dort
folgende Zeile einfügen:

> `define( 'YOURLS_NO_VERSION_CHECK', true );`

Erledigt. Leider ist die Sammlung der Statistiken an die Überprüfung auf
eine neue Version gebunden. Technisch nicht notwendig, soll wohl eher
dazu beitragen die Deaktivierung nochmal zu überdenken. Schade, aber ist
halt so.

Quelle: [YOURLS-Blog][Blog]

  [Blog]: http://blog.yourls.org/2014/01/on-yourls-1-7-and-api-yourls-org/
