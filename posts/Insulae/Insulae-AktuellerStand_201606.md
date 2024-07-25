Title: Insulae - Aktueller Stand Juni 2016
Date: 2016-06-28 14:50
Author: Jan H. Krüger
Tags: Insulae, Zwischenstand, PBBG, Browsergame
Category: Insulae
Slug: insulae-stand-juni2016
Series: Insulae-Stand

Wieder ist etwas über einen Monat in das Land gegangen.

Die bisherige **Anzahl an Welten** werde ich in den nächsten Zeit nicht mehr anpassen. Ich denke die Spielwelt ist aktuell groß genug und besitzt noch nicht das von mir gewünschte Konfliktpotential. Jetzt könnte ich entweder Inseln und Welten wieder entfernen. Oder künstlich eine Rohstoffverknappung herbeiführen.
Das fühlt sich im Moment jedoch nicht richtig an. Und eine wirkliche Not eine Änderung herbei zu führen gibt es ja auch nicht.

Was gab es noch. In **Welt sieben** gab es den ersten Zwischenaufall aufgrund der auseinander driftenden Inseln. Ein hier nicht näher genannter, selbst ernannter Kriegsherr wollte lieber noch den 100.000 Ent töten und stellt erst am Ende fest das sein Schiff ihn nicht mehr in zivilisierte Gewässer bringen kann. Und aufgrund vorherige Differenzen mit den sonst stehts zur Verfügungstehenden Rittern des Ni, speziell die Logistikabteilung wollte, wollte niemand aushelfen. Und leider, leider waren die eigenen Krieger so gut trainiert das es ihm nicht möglich war im Kampf gegen die Ents zu unterliegen. Und naürlich war besagter selbsternannter Kriegsherr vorher auch zu geizig für einen Gifttrank zu sorgen.
Am Ende ging es dann noch gut aus und der Recke konnte gerettet werden. Ich vernahm jedoch das eine nicht näher genannte Person kurz darauf einen Auftrag über 500 Giftränke erteilte. :-)

**Auf der technischen Seite** hat sich nicht ganz so viel getan. Ich habe in meinen Batchjobs weiter die Compilermeldungen ausgebaut und insbesondere einen Fokus auf die hässlichen CWE-190 Meldungen gelegt.
Dennoch. In der Stadtauswertung gibt es nun keine Meldungen mehr. Auch Flawfinder, cpplint etc. finden nicht mehr wirklich etwas. Nebeneffekt: die Stadtauswertung für alle 613 Städte dauert nunmehr nur noch 3 Sekunden. Nicht schlecht wie ich denke. Insbesondere wenn ich überlege das die Stadtrunde in SW früher mal eine halbe Stunde dauerte.
In den drei Sekunden ist bisher noch keine ernsthafte Performanceoptimierun eingebaut. Keine Paralellisierung. Kein Nutzen von memcache oder Redis, Threading oder whatever. Bedeuted: wenn ich wollte wäre da noch Luft nach oben.

Jedoch ist derzeit der **Marktplatz** in den Innenstädten, konkret das gleichlautend Gebäude **unter dem Prüfstand**. Derzeit produziert der Marktplatz Thaum und Kakao. Hierbei stören mich zwei Dinge. Zum einen die feste Vorgabe von Thaum und Kakao. Andererseits können beide Rohstoffe ja auch in einigen Welten direkt auf Feldern abgebaut werden und besitzen nicht den Seltenheitswert wie in Scherbenwelten. Der bisherige Stand ist seinerzeit so von Scherbenwelten übernommen worden. Dort konnte es Sinn ergeben beide Rohstoffe darüber zu produzieren da es sonst keine wirklich nennenswerten Zuflüsse gab. Hier gibt es jedoch keinen Zeitdruck, die Umfrage im Forum diesbezüglich läuft auch noch drei Wochen. Mal sehen was ich dann daraus erarbeite.

Also, an sich recht wenig jedoch auch nichts dramatisches. Ah, ich bin mit meinen **Repositorys nach GitHub umgezogen**. Auf die kostenpflichtige Variante da nur dort private Repositorys möglich sind.
Öffentlich habe ich zwei Stück eingerichtet. [insulae-public][1] und [sw-images][2]. Um Insulae-public liegen unter anderem die exportierten Kartendaten der SW-Beta. Sollte jemand mal die alte Welt nachbauen wollen, ein paar Screenshots. In sw-images liegen die alten SW-Bilder, also das Grafikpack.

[1]: https://github.com/janhkrueger/insulae-public
[2]: https://github.com/janhkrueger/sw-images
