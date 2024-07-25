Title: Einführung von Beute
Date: 2015-02-01 00:58
Author: Jan H. Krüger
Tags: Insulae, Beute, Monster

Über 10 Jahre läuft Insulae bereits. Über eine Dekade war es normal durch das Besiegen von Gegnern lediglich Erfahrung und Ruhm zu erlangen. Dennoch gab es, schon fast seit Anfang an, den Wunsch auch Beute von den Gegnern zu erlangen. Habe ich lange Zeit nicht eingeführt. Auch jetzt noch bin ich nicht vollständig überzeugt. Gerade nach einer so langen Zeit kann dies auf die Wirtschaft einen enormen Einfluss haben. Oder auch nicht. Je nachdem wie die Beute eingeführt wird.

Dennoch, es reizte mich schlicht dies technisch anzugehen.

Also, kurz angeschaut was ich als Grundlage habe. Meine Tabelle mit den Völkern und jene mit den Gegenständen. Daraus lässt sich was zaubern.
Im Grunde muss ich ja nur folgendes Wissen:

* Volk
* Gegenstand
* minimale und maximale Menge

Das sieht dann bei mir wie folgt aus:

![Beutetabelle](images/InsulaeTabelleBeute.jpg)

Die Phase ist enthalten damit ich noch pro Spielwelt differenzieren kann. Und mittels __beuteAktiv__ kann die Beute bei Bedarf schnell, und in Zukunft auch per Oberfläche für die Supporter, an- und abgeschaltet werden. Könnte ja mal nötig sein aufgrund unerwarteter Nebeneffekte eine Beute schnell zu deaktivieren.

Um das System einzuführen bekommen meine Riesenratten als erstes etwas zugeteilt. __Rattenzähne__ und __Rattenschwänze__ scheinen einen soliden Eindruck zu ergeben, für den Anfang. Auf die Theorien der Spieler wozu die Gegenstände zu gebrauchen sind bin ich schon gespannt.

Also flux in die Datenbank eingetragen, damit sieht das dann wie folgt aus:

![BeutetabelleRatte](images/InsulaeTabelleBeuteRatte.jpg)

Das war es eigentlich auch schon. Derzeit wird ganz platt für jeden Gegenständ eine Wahrscheinlichkeit von 10% angenommen. Das werde ich die Tage noch verfeinern um Beutesysteme vergleichbar mit den handelsüblichen MMOs abzubilden. Doch eines nach dem anderen.

__beuteVolk 1000000001__ ist bei mir nichts anderes wie die übliche Riesenratte. So, jetzt ist es raus. Ratten sind bei mir nur Ziffern ;)
__beuteGegenstand 1583__ identifiziert den Rattenzahn.
__beuteGegenstand 1584__ identifiziert den Rattenschwanz.
__beutePhase 1000000000__ sagt aus das die Riesenratten in meiner primären Spielwelt betroffen sind.

Die restlichen Spalten sollten sich von alleine erklären.

Wenn nun ein Spieler eine Riesenratte in der Phase 1000000000 erschlägt wird derzeit nur geprüft ob mit der oben genannten Wahrscheinlichkeit von 10% die Riesenratte einen Gegenstand zurück lassen kann. Ist dem so wird noch zusätzlich zufällig ein ein von __beuteMin__ bis einschließlich __beuteMax__ ermitteln. Das Ergebnis ist die Anzahl der Gegenstände welche der Spieler von der Ratte erhält. Ja, auch hier kann es nochmal passieren das der Spieler keinen Rattenschwanz erhält.

Quick & Dirty, doch für den Anfang soll es mir genügen. Eine differenziertere Beuteverteilung werde ich die Tage einbauen.
Wirklich spannend wird es ja auch wenn an einem Kampf mehrere Spieler teilnehmen. Sollen da Gegenstände zwischen den Spielern aufgeteilt werden? Welche Effekte kann ich an anderen Stellen implementieren um die Wahrscheinlichkeit Beute zu bekommen zu erhöhen? Ich denke da an __"Glücksamulette"__, __Goldtränke__ oder __Hexenflüche__ welche das ganze beeinflussen können. Positiv wie negativ. 

Hm, ein Fluch welcher das Opfer nur Steine sammeln lässt beziehungsweise alle Gegenstände zu Staub zerfallen klingt in meinem Kopf gerade sehr fies :-) Doch eines nach dem anderen.


Eine sehr interessante Beschreibung welche bedeutend weiter ins Detail geht wie ein Beutesystem implementiert werden kann findet sich bei [CodeProject][1].


[1]: http://www.codeproject.com/Articles/420046/Loot-Tables-Random-Maps-and-Monsters-Part-I