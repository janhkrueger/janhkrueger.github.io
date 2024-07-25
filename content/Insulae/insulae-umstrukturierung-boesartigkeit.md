Title: Umstrukturierung Boesartigkeit
Date: 2010-05-28 15:47
Author: Jan H. Krüger
Tags: Insulae, Bösartigkeit, Umstrukturierung

Die Bösartigkeit, also der Wert, welcher in Insulae und auch
Scherbenwelten angibt, wie viele böse Taten ein Account bereits begangen
hat, war bisher ein globaler Wert welcher auf der gesamten Welt
Gültigkeit besaß. Dieses wurde nun von mir geändert, die Bösartigkeit
steht nicht mehr für die gesamte Welt sondern nur noch für die Insel
bzw. den Kontinent auf dem die böse Tat begangen wurde. Als Nebeneffekt
werden die einzelnen Regionen noch stärker hervorgehoben im Spiel, da
sich eben auch Änderungen im Verhalten der Bewohner ergeben können.  
  
Die Ablage im Datenmodell ist dabei so einfach wie möglich gehalten,
anbei ein Beispiel. Kurz, knapp und auch für die Datenbank leicht zu
verarbeiten.  
  
[![Bild][]][]  

Was hat dies für Konsequenzen? Nun, erst einmal kann es so nun passieren
das ein Account in seinem Heimatland zwar ein ganz schlimmer Junge ist,
am anderen Ende der Welt jedoch noch niemand etwas davon gehört hat. Der
Bösartigkeitswert wird nun daher für jede Insel und jeden Spieler
getrennt gespeichert. Erhöht die Datenmenge, aber ich denke dies ist es
wert. Nun erfährt nicht sofort Bauer Hans auf der anderen Seite der Welt
das Person A mal wieder Sklaven gesammelt hat. Wenn allerdings ein
gewisser Schwellenwert überschritten wird, wird die erhaltene
Bösartigkeit jedoch auch auf die umliegenden Inseln anteilig weiter
gereicht. Die Geschichten über die schrecklichen Taten verbreiten sich
also auch über die Landesgrenzen hinweg.

  

Andererseits ergeben sich für einen Account der stets nur auf derselben
Insel verbleibt keine Änderungen, für diesen gibt es (scheinbar) nur
einen abgespeicherten Wert.

  

Dies bedeutet allerdings auch, dass ein schlimmer Finger auf der anderen
Seite der Welt erst einmal eine weiße Weste hat. Der Neuanfang in einem
fremden, weit entfernten Land wird damit unterstützt.

  

Beispiel wie die Bösartigkeitstabelle mit Inhalten aussieht:

  

[![Bild][1]][]

  

Mit dieser Änderung einhergehend, wird auch der Abfall der Bösartigkeit
angepasst. Für jede Region wird die Bösartigkeit getrennt herabgesetzt.
Grundsätzlich gilt auch weiterhin: Je höher der Wert, umso länger dauert
es bis dieser abgebaut worden ist.

  [BIld]: https://www.janhkrueger.de/blog/wp-content/uploads/2010/05/spieler_boesartigkeit1.png
    "Tabelle der Datenablage"
  [![Bils][]]: http://www.janhkrueger.de/blog/wp-content/uploads/2010/05/spieler_boesartigkeit1.png
  [1]: http://www.janhkrueger.de/blog/wp-content/uploads/2010/05/spieler_boesartigkeit_zahlen.jpg
    "Beispielhafte Werte für die Bösartigkeit"
  [![Bild][1]]: http://www.janhkrueger.de/blog/wp-content/uploads/2010/05/spieler_boesartigkeit_zahlen.jpg
