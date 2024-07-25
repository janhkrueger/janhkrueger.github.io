Title: Insulae - September 2018 Status
Date: 2018-09-01 14:50
Author: Jan H. Krüger
Tags: Insulae, Zwischenstand, PBBG, Browsergame
Category: Insulae
Slug: insulae-stand-september2018
Series: Insulae-Stand


Hui, das war eine lange Zeit. Über ein Jahr habe ich es nicht mehr geschafft hier etwas zu schreiben.
Meine bisherige Arbeit hat mich ziemlich mitgenommen, körperlich und geistig was dazu geführt hat das ich ausser dem notwendigsten kaum noch etwas unternommen habe. Aber, das ändert sich nun und ich merke schon wie ich solangsam wieder hier rein komme.

Jedoch gab es daher im letzten Jahr eher im Hintergrund Anpassungen. Neue Features im Spiel habe ich nicht eingebaut, nur wenn nowendig kritische Fehler behoben.

Das was ich anfang letzten Jahres begonnen habe konnte ich dennoch ansatzweise fortführen. Die technische Basis ist nun fast komplett auf Dockercontainer umgestellt. Der Start und Stop (fast) der gesamten Infrastruktur kann nun mittels eines Kommandos erfolgen:

```
docker-compose up -d
```

Fertig, das war es. Schon steht alles einsatzbereit zur Verfügung. Das ganze ist auch asciinema auch einmal dargestellt:


[![asciicast](https://asciinema.org/a/uSFwPzcVkPuBaGTZTp2pdpMiE.png)](https://asciinema.org/a/uSFwPzcVkPuBaGTZTp2pdpMiE?rows=25)


Damit bin ich einen großen Schritt weiter Insulae irgendwann einmal OpenSource gestalten zu können. Je einfacher später das Aufsetzen einer eigenen Instanz ist umso mehr auch etwas weniger technikaffince Interessierte können dabei mitmachen. Offen sind dabei noch die folgenden Punkte:

* automatisierter Build mittels Jenkins
* Anlage der Verzeichnisstrukturen bei erstmaliger Benutzung
* Verlagerung der persistenten Ablage der Datenbank in ein docker-managed Volume.

Und naja, der größte Punkt: das Neuschreiben der Oberfläche in C++. Mit [wt][1] habe ich wohl ein vernünftiges Framework gefunden. Benötigt nur noch Zeit es auch anzuwenden.


Die vergangenen Monate haben eine Sache jedoch ganz klar gezeigt. Die Infrastruktur ist jetzt bereits absolut stabil. Selbst wenn ich Wochen nicht reingeschaut habe: es läuft einfach. Technisch aber auch im Spiel. Die Götter von echten Menschen spielen zu lassen war denke ich eine der besten Entscheidungen. So kommt regelmäßig Abwechslung von aussen rein ohne das ich dies erledigen muss.

Bei den Dungeons bin ich auch echt zufrieden. Mittlerweile sehe ich anhand der Auswertungen, KPIs etc ganz klar: es entwickelt sich ein kompletter Industriezweig welcher sich damit beschäftigt Dungeonbesucher bei ihren Vorhaben zu unterstützen. Quasi alles was hilft länger in den Dungeons zu verweilen. Aktuell ist das höchste (tiefste ;) ) Level 78. Ordentlich. So langsam kommen auch die fiesen Untoten raus. Wobei ich hier denke ich stärker darauf achten muss wie die Generierung und Auswahl der Monster und Gruppengrößen läuft. Da werde ich ein paar weitere KPIs bauen und neue Testfälle. Auch denkbar sind weitere Gegenstände speziell für die Dungeons. Eines ist bereits vorhin eingebaut worden.


Ab heute ist im Spiel das erste Dungeonitem implementiert. Ein "Fluchtseil" welches das schnelle Entkommen aus einem Dungeon ermöglicht ohne stets über 50/50 zu gehen. Bei Benutzung wird der Anwender direkt auf 50/50 der ersten Dungeonstufe teleportiert. Den letzten Schritt muss dann immer noch selbst getätigt werden. So kann ich jedoch verhindern das jemand direkt an die Oberfläche teleportiert wird und dann dort womöglich mitten in ein Monster oder so rennt.
Zugegeben, von den Pokemonspielen inspiriert. Aber es funktioniert.
Besonders ist jedoch: das Rezept ist nur in den Dungeons selbst zu finden und kann nicht in Städten erworben werden. Wer es findet kann es selbst anwenden und der Rezeptliste hinzufügen oder an andere Spieler verkaufen. Ist es einmal der Rezeptliste hinzugefügt kann verschwindet der Rezeptgegenstand. Will jemand anderes lernen Fluchseile zu produzieren muss ein neues Rezept gefunden werden.

Ich erwarte das dadurch in den nächsten Tagen wenn die ersten Rezepte gefunden werden ein interessantes Hin- und Her im Handelsforum auftreten wird. Wie die Spieler die Rezepte gerade am Anfang bewerten... da bin ich gespannt und habe keine Vorstellung. Das Rezept ist gleichzeitig das erste das als solches keinen Preis in irgendeiner Weise von mir bekommen hat.

Perspektivisch kann ich mir vorstellen Waffen und Rüstungen mit speziellen Fähigkeiten für Dungeons bereit zu stellen. Aber eines nach dem anderen.


Die ACLs zur Steuerung für Passierscheine, Steuersätze etc. sind derzeit noch nicht so für mich befriedigend. Technisch gesehen. Da werde ich demächst mal ein Auge drauf werfen.

[1]: https://www.webtoolkit.eu/wt
[2]: https://api.insulae.janhkrueger.de/town
