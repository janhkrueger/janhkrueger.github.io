Title: Python 3 = *grmpf*
Date: 2009-07-04 08:01
Author: Jan H. Krüger
Category: IT
Slug: python-3-grmpf

Nachdem ich die Tage hoch getoent habe das die Umstellung auf Python 3
erfolgreich war, kam die Tage nun die ernuechterung. Es funktionieren
mit pg8000 bei mir nur die Basisprozesse.  
  
Aus mir nicht verstaendlichen und nachvollziehbaren Gruenden weigert
sich pg8000 Updates auszufuehren. Select- und Insert-Querys stellen kein
Problem dar, aber Updates... keine Chance. Hinzu kommt noch das ich die
Fehlerbehandlung bei Python 3.1 / pg8000 nicht durchdrungen habe. Unter
Python 2.5.2 / psycopg2 kam ich problemlos an die Fehlermeldungen heran.
Das klappt hier nicht mehr. Vielleicht waere ich mit einer Fehlermeldung
auch in der Lage pg8000 zu ueberreden auch Updates auszufuehren.  
  
Konsequenz: Ich bin wieder zu Python 2.5.2 zureuck gegangen. Hier
funktionieren zumidnest noch alle Bibliotheken und Module. Vielleicht
schaue ich mir in einem halben Jahr noch einmal eine aktuelle Version
an, wenn diese etwas gereifter ist und noch weitere Module nachgezogen
haben.
