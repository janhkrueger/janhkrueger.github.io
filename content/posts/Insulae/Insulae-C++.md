Title: Umstellung auf C++
Date: 2014-12-23 13:01
Author: Jan H. Krüger
Category: Insulae
Tags: Insulae, Browsergame, C++
Slug: umstellung_auf_CPlusPlus

Seit Jahren laufen in Insulae meine Programme für den BackEnd-Bereich auf Pythonbasis. Während ich die Sprache als solches mag und sie mir auch gefällt war es immer irgendwie.. weiß nicht. Mir hat was gefehlt.
Seit einiger Zeit reifte bei der der Wunsch mich wieder fitter in C++ zu halten.
Was bietet sich da besser an wie mein altes Spielprojekt an dem ich eh schon seit über einer Dekade für mich neue Techniken ausprobiere hervorzukramen? Gesagt getan.


Nachdem nun die ersten Programme umgestellt sind kann ich mehrere Punkte feststellen:

* Die Umstellung ist, nachdem eine Einarbeitungshürde genommen ist, schnell getan.
* Eclipse als IDE ist weiter zu tunen damit auch wirklich alle Warnungen und Fehlermeldungen gemeldet werden.
* Die Laufzeit eines der wichtigsten Programme ist von ~ 45 Sekunden auf kann ~ 7 Sekunden gesunken.
* Ich nutze nun konsequenter Transaktionen. Bisher ein All-Time "Mach ich mal später".
* Es ist deprimierend zu sehen das ich offensichtlich mehr C++ Wissen vergessen habe wie ich dachte das ich gehabt hätte.


Die Performancegewinne sind echt genial. Das hätte ich an sich nicht erwartet. Macht Spaß auf mehr, wenn auch die größeren Skripte umgestellt sind.

Eine Sache fiel mir jedoch auch bereits negativ auf. Das betrifft jedoch eher mein Entwicklungssetup. Auf meinem Macbook ist zwars ein g++ vorhanden. Dies ist jedoch eine andere Version, von Apple angepasst wie jene welche auf meinem Server läuft. Hat zu erst zur Folge gehabt das ich auf dem Server nach einer Änderung Fehler um die Ohren gehauen bekommen habe welche ich lokal nicht hatte. Die, für mich, auch erst einmal keinen Sinn ergaben.
Am Ende stellte sich raus: ich habe in einer Headerdatei ein Attribut angegeben welches zu dieser Zeit, wenn von der Klasse ein Objekt angelegt wird, nicht verfügbar ist. Der Applecompiler lässt es durchgehen. GNU g++ meckert es an.
Zwar habe ich es das Attribut auch nicht benötigt und konnte daher den Eintrag in der Headerdatei auch entfernen. Ich muss dennoch irgendwann einmal nachlesen warum genau der eine Compiler das nicht meldet während der andere es kritisiert. Wird wohl darauf hinauslaufen das ich lokal den GNU g++ noch bereit stelle.


Die nächsten Schritte sehen auch recht übersichtlich aus:

* Umzug der Programme in das zentrale Insulae-Repository
* Einrichten von Git-Hooks um nach einem Push auf dem Server die Programme neu zu kompilieren und bei Erfolg die Binarys laufen lassen.

Und irgendwann einmal werde ich die in PHP geschriebenen Klassen in C++ nachbauen und in PHP bereitstellen. Wird dann wohl über eine PHP Extension laufen. Doch das hat noch ein wenig Zeit.

Zum Glück sind demnächst 5 Tage frei in denen ich, neben ausschlafen, experimentieren kann.