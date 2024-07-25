Title: Insulae - Aktueller Stand August 2017
Date: 2017-08-11 14:50
Author: Jan H. Krüger
Tags: Insulae, Zwischenstand, PBBG, Browsergame
Category: Insulae
Slug: insulae-stand-august2017
Series: Insulae-Stand

Moin Moin,

es wird mal wieder Zeit für ein Update. Genauer gesagt ist es längst überfällig.

Auch die letzten Monate waren eher technisch motiviert. Am API-Server habe ich immer mal wieder geschraubt und wenn es notwendendig war auch an anderen Punkten. Die auf Swagger [dargelegte API][1] ist soweit umgesetzt auch wenn ich aufgrund der API wieder ein paar Änderungen immer wieder mal ein paar Änderungen an den regulären Klassen vornehmen musste. Wobei das eigentlich gut ist denn so wachsen API, Batch und Online immer mehr zu einer Codebasis auf C++ Basis zusammen. 
Im Grunde könnte man auch sagen das dieses Jahr rein auf technischen Maßnahmen ruht :)

Dafür habe ich die Liste der Städte nun als API freigegeben. Alle per OptIn verfügbaren Städte können nun jederzeit über die [Stadt-API][2] eingesehen werden.

Anfang des Monats habe ich dann meinen Server gewechselt. Es gab keine Notwendigkeit dazu, doch Hetzner bietet noch dieses Monat Server ohne Einrichtungsgebühr an. Da habe ich bei einem Dedicated zugeschlagen. Endresultat: 8 echte Kerne statt 8 virtuelle, 64GB RAM statt 32GM RAM, 1 GBit/s garantierte Bandbreite statt nur bis zu 1 GBit/s. Allerdings ging es auch ein wenig runter. Anstatt 600GB SSD habe ich nur noch 240GB zur Verfügung. Jetzt kein Beinbruch, ich habe zu jeder Zeit maximal 50GB verwendet. Die 240GB werden daher denke ich auch noch lange reichen.
Netter Nebeneffekt: von monatlich 60€ bin ich runter auf 47€. Also gleich noch Geld gespaart.

Wie wirkt sich das nun für euch Spieler aus? Hervorragend!


Alter Server:
```
[2017-08-10 02:16:01.675] [Stadtauswertung] [info] Stadtauswertung gestartet
[2017-08-10 02:16:01.825] [Stadtauswertung] [info] Beendet
```

Neuer Server:
```
[2017-08-10 13:40:35.200] [Stadtauswertung] [info] Stadtauswertung gestartet
[2017-08-10 13:40:35.246] [Stadtauswertung] [info] Beendet
```

Bei 613 Städten wohlgemerkt. Sieht jetzt erstmal nicht so viel aus, jedoch schon spürbar.
Beim Wachstum der Ressourcen sieht es jedoch nochmals besser aus. Von 8 Minuten auf 3 runter. Für *alles*.

Der Wert für die Query Peak/s sieht es toll aus. Das musste ich selbst mit einem Lasttest ermitteln, das schafft ihr Spieler nicht auf Kommando :)

Alt:
![Insulae_August2017_](images/InsulaeQueryPeakAlt.png)

Neu:
![Insulae_Welt_007](images/InsulaeQueryPeakNeu.png)



Ingame: Der Krieg der Götter ist immer noch dabei. Da zuckt noch was. Auch wenn es sich schon spürbar beruhigt hat.

[1]: https://app.swaggerhub.com/apis/janhkrueger/InsulaeAPI/1
[2]: https://api.insulae.janhkrueger.de/town
