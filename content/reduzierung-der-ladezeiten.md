Title: Reduzierung der Ladezeiten
Date: 2010-05-27 22:10
Author: Jan H. Krüger
Category: Insulae
Slug: reduzierung-der-ladezeiten

Nach einiger Tüftelei und vor allem einer geänderten Herangehensweise
konnte ich die Ladezeiten in Insulae bedeutend verbessern. Der
Gruppenschirm, ein zentraler Bestandteil von Insulae, stellt er
schließlich die Welt für den Spieler dar und bietet somit
Interaktionsmöglichkeiten, war stets etwas "zäh".  
  
Gegen Ende, nachdem so einige Dinge eingebaut waren wie ich es wollte,
betrug die durchschnittliche Ladezeit 1121 Millisekunden. Definitiv
nichts was irgendjemanden vom Hocker hauen kann, geschweige denn etwas
was für einen Massenbetrieb geeignet ist.  
  
Also habe ich ein wenig getüftelt, gedreht und überlegt was verändert
werden kann. Ich denke ich kann sagen, die Arbeit von 4 Tagen war ein
voller Erfolg. Von den eben erwähnten 1121 Millisekunden sind nun nur
noch 16 Millisekunden über geblieben. Ja, richtig gelesen, 16. Der
Seitenaufbau fluppt nun sozusagen.  
  
Um dieses zu erreichen, habe ich als erstes die Protokollierung der
Datenbank hoch geschraubt. PostGreSQL loggte nun haarklein, welche
Querys ausgeführt werden, der Zeitverbrauch eben dieser und ob sie
erfolgreich waren. Bei der Analyse eben dieser Protokolle viel eines
zuerst auf: Es wurden mehrere, zum Teil zeitintensive Querys
unnötigerweise ausgeführt. Um dem nachzugehen wurden die Klassen für die
Spieler, die Karte sowie der Quellcode des Gruppenschirmes genauestens
überprüft. Und siehe da, es fanden sich ein paar Logikfehler. Diese
wurden ausgebaut, das zähe Verhalten fing an sich zu lösen. Dennoch war
es noch nicht ideal. Den wirklichen Durchbruch habe ich erzielt, indem
ich die Abfragelogik der 49 dargestellten Felder grundlegend umwarf.  
  
So wurde bisher jedes Feld für sich von der Datenbank angefordert. Wenn
man bedenkt das nicht nur das Feld, sondern auch eventuelle Gebäude,
Städte, Spieler- und Monstergruppen, Straßen, Schilder, Karawanen,
Trigger etc. auf Existenz an der betreffenden Koordinate geprüft wurden,
kamen da schon recht viele Querys zusammen. Von der Einzelfeldabfrage
bin ich nun weg und lese alle Felder des Kartenbereiches aus. Die
Datenbank wird damit entlastet, die weitere Logik geschieht bequem
innerhalb von Python. Ich mag die Dictioneries ;)  
  
Im Anschluss gab es noch ein paar kleinere Umstellungen des
Datenmodells, einige  der großen Tabellen wurden aufgeteilt um nur
relevante Daten durchsuchen zu müssen.  
  
Nun, letzten Endes hat sich gezeigt dass es, auch bei einem bestehenden,
funktionierenden System sich lohnen kann Zeit zu investieren um
Optimieren vorzunehmen. Damit ist Insulae wieder einen Schritt näher
produktiv zu gehen.
