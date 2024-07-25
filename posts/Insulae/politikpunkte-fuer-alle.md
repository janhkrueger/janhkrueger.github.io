Title: Politikpunkte fuer alle
Date: 2009-03-22 10:59
Author: Jan H. Krüger
Category: Insulae
Slug: politikpunkte-fuer-alle

**Nach einer etwas laengeren Pause konnte ich endlich einen elementaren
Teil von Insulae beenden. Die taegliche Berechnung der Politikpunkte
(PP) ist nun einsatzbereit.**  
  
Konkret laeuft nun taeglich eine rekursive Funktion welche bei der
Auswertung eventuelle vorhanden Staedte sowie Raenge innerhalb einer der
Kirchen beruecksichtigt. An sich ist das ganze gar nicht so schwierig,
aber ein solches Skript an sich hilft ja noch nichts. Also mussten
Spielerdaten her.  
  
Gesagt getan, habe ich mich daran gemacht knapp 1000 Spieler wie sie in
Scherbenwelten vorkommen in Insulae nachzubilden. Konkret habe ich die
grossen Lehnsketten verarbeitet. Spielername, Lehnsherr, Avatarbild und
partiell sogar die Nation selbst sind nun, per Hand, aus Scherbenwelten
in Insulae uebertragen worden. Das war streng genommen auch der laengste
Part der ganzen Arbeiten. Aber wie auch immer, ich habe nun konkret 1162
Accounts abgebildet. Jeder natuerlich mit seinem Hauptcharakter, dessen
Fertigkeiten, den Startgegenstaenden etc. Ich denke daher das ich
hierbei nun eine recht grosse Aehnlichkeit mit der Realitaet habe. Zum
Vergleich, in Scherbenwelten waren in den letzten 7 Tagen 1099 Spieler
aktiv.  
  
Mit dieser theoretischen Spielerbasis kann ich mein PP-Programm also
unter realistischen Bedingungen laufen lassen. Und das Beste: es laeuft
immer noch in unter einer halben Minute.  
Allerdings fehlt noch eine Sache. Im Original kann ein Lehe maximal
soviele PP erhalten wie sein Lehnsherr. Alles darueber wird
abgeschnitten.  
Dies habe ich bisher noch nicht realisiert, denn auf Basis einer
Rekursion faellt mir dafuer noch keine saubere Loesung ein.
Wahrscheinlich werde ich nach der eigentlichen Verarbeitung noch einen
Korrekturlauf einbauen welcher explizit nur dies behandelt und dann erst
die PP einem Spieler zuweist. Aber denkbar waere auch das ich hier einen
anderen Weg begehe wie in SW. So koennte das Lehnsverhaeltnis auch
aufgeloest werden wenn ein Lehe mehr PP erhaelt. Doch da muss ich erst
noch mal drueber nachdenken was ich genau fuer Insulae will.  
  
Erstmal wird das PP-Programm taeglich mitlaufen und fleissig die Punkte
auswerten.
