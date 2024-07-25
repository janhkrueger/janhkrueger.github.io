Title: Insulae - Aktueller Stand Januar 2017
Date: 2017-01-01 14:50
Author: Jan H. Krüger
Tags: Insulae, Zwischenstand, PBBG, Browsergame
Category: Insulae
Slug: insulae-stand-januar2017
Series: Insulae-Stand

Moin und ein frohes neues Jahr zusammen!

ich weiß ich weiß, die letzten Monate habe ich kein Update geschrieben. Ihr Spieler jedoch habt es ja im Spiel selbst miterlebt was so alles passiert ist.

Im Hintergrund habe ich weiter an den APIs geschraubt. Derzeit bin ich auch noch dabei die bestehenden APIs mit Hilfe von [swagger.io][2] zu dokumentieren. Das läuft auch super, die Ergebnisse gefallen mir sehr. Swagger bietet Wege einen Art selbst dokumentierende API zu schreiben. Weiterhin kann Swagger aufgrund der API-Definition auch gleich Code für die Serverseite aber auch für nutzende Clients generieren. Also richtig genialer Scheiß.

Nachteil (und ich sehe das wirklich als Nachteil an): swagger Editor und swagger UI laufen komplett auf Node.js. Das habe ich ja bisher immer gemieden wie die Pest. Auf meinen Server kommt das definitiv nicht. Mal sehen, vielleicht als lokale Variante in einem Container.

Im Hintergrund habe ich weiter nach Wegen gesucht die API auf C++ umzustellen. Ehrlich gesagt nicht so erfolgreich. Zuletzt habe ich mir 
[pistache.io][1], ein C++ REST framework angeschaut. Sieht sehr vielversprechend aus. Allerdings: es will partout nicht auf meinem Server die Framework eigenen Beispiele kompilieren. Im Moment sieht es so aus als ob die Frameworkinternen Methodenaufrufe ungünstig benannt wurden. Konkret wohl die namespace Angaben.

Derzeit habe ich noch keinen Call beim Entwickler offen, der wird noch eingestellt. Noch hoffe ich dass ich pistache wirklich irgendwann einsetzen kann. Wäre toll denn dann hätte ich endlich einen Weg um auch an dieser Stelle auf C++ sinnvoll umzustellen.

Wenn das erledigt ist steht ein Upgrade auf PostgreSQL auf Version 9.6 an. Die Upserts haben es mir angetan, hinzu kommen noch weitere Performancegeschichten die ich gerne mitnehmen möchte. Das wird einfach allen zugute kommen.
Da Debian Stable derzeit jedoch die von mir gewünschte Version nicht anbietet könnte es sein das ich hier auf ein Postgres im Container umstelle. Mal sehen.

Spielintern selbst läuft derzeit etwas richtig tolles ab. Die Götter gehen gerade in einen Krieg hinein der in Insulae bereits als die "Götterkriege" bezeichnet wird. Ausgelöst wurde das ganze dadurch dass der Heilige Nes'Quick an seinen Gläubigen bereits (RL) am 20. Dezember geschenkte verteilt hat. Was Urvan erzürnte und dieser meinte dadurch würde Weihnachten sabotiert. Wie das ganze ausgehen wird: keine Ahnung.
Schön ist jedoch dass sich hier einmal mehr auszahlt das ich die Götter von echten Spielern mit Gottaccounts betreuen lasse. Echte Personen hinter den Göttern erlaubt gerade in Situationen wie dieser der Spielwelt ein Eigenleben das ich alleine so nie hervorrufen könnte, etwas das es früher in Scherbenwelten auch nie gab. Und mit meinem Wissen über KIs ist es an der Stelle nicht soweit das ich das automatisieren kann.

Der Plan Spieler auch eigene Portale zu anderen Welten bauen zu lassen ist noch nicht abgeschlossen. Irgendwie fehlt mir noch das Konzept zu dem ich sage: “Jou, das ist es.”
Sind ja im Grunde mehrere Themen.

- der Bau des Portales
- der Prozess geeignete Koordinaten zu finden
- wird ein atmosphärisches Gegenstück benötigt?
- wenn ja, wie wird dieses konstruiert?

Die Bereitstellung der Tempel per API hat dazu geführt das jemand aktiv alle dort gelisteten anreist um zu prüfen dass dort keine Dämonen sich verstecken. Interessanter Ansatz. Ich denke zwar dass nur dann ein Dämonentempel gefunden wird wenn der Besitzer gerade einen Fehler begangen hat… Dennoch viel Spaß bei diesem Kreuzzug :)

Die Borgias haben die API der Märkte genutzt um effizient gute Gelegenheiten zu Handeln zu finden. Im Zuge dessen hat der Spieler welcher seine gesamten Charaktere als Bürgermeister einsetzt mittlerweile seine achte Stadt. Um die Versorgung seiner Städte einfacher zu gestaltet hat er alle 8 Märkte für die API freigegeben. Die Versorgung ist, laut seiner Aussage, für ihn einfacher denn je geworden. Freut mich persönlich das die Spieler so langsam anfangen die Daten der APIs sinnvoll zu nutzen und bestärkt mich an dieser Stelle auch weiter zu arbeiten.

Außerhalb von Insulae im Bezug der ehemaligen Scherbenweltenfront entwickelt sich, so wie ich das sehe, nichts mehr. 

"[The game with no name][3]" scheint seit Februar wieder eingefroren zu sein. Von Webtales und Scherbenwelten selbst ist wie zu erwarten nichts mehr zu lesen gewesen. Ich gehe mal davon aus das sich die ehemaligen Inhaber von Scherbenwelten auch nie mehr melden werden. Mein Angebot steht zwar noch Scherbenwelten auf eigenen Kosten wieder zu betreiben und weiterzuentwickeln. Jedoch nur wenn ganz klar ist das ehemals-Webtales sich dann komplett raus hält. (Muss ne Nachwirkung von Neujahr sein. Die melden sich eh nie mehr.)

[Inselpioniere][4] scheint ebenfalls immer noch zu ruhen. Die im Impressum verlinkte [Webseite des Serverbetreibers][5] selbst ist nicht mehr aktiv. Oder zumindest scheint seit Juli 2016 nur noch eine Defaultseite eines Apache unter Ubuntu zu laufen. Die [Webseite des Programmierers][6] bindet Inselpioniere selbst nur per Frame ein. Muss nix bedeuten. Intern könnte Inselpioniere natürlich auch brummen wie ein Hornissenstaat. Kann ich von außen jedoch nicht erkennen.

Kommen wir zur "[Welt in Scherben][7]". Ich glaube im Mai 2016 ins Leben gerufen um einen Nachbau von Scherbenwelten zu erstellen um darauf aufbauend weiter zu entwickeln. Für mich von außen, bzw. nur mit öffentlichem Forenaccount, sieht es derzeit so aus als ob mangels Entwickler dort noch nichts präsentables existiert.

Kann anders sein, ist jedoch nicht zu erkennen. Ich möchte Welt in Scherben nicht schlecht reden, das liegt mir fern. Ich denke jedoch auch dass wir dort in der nächsten Zeit nichts sehen werden. Zum einen weil wir nach über einem halben Jahr immer noch nichts sehen können und auch weil ich überzeugt bin das der Anfang falsch aufgestellt wurde. Bitte beachtet das dies nur meine Meinung und nichts objektives darstellt. Ich denke ein solches Projekt, ehrenamtlich, neben der Arbeit, ohne Entgelt nur dann funktionieren kann wenn ein Entwickler sich sagt “Ich will das jetzt umsetzen” und sich hinsetzt und sich um diesen bei Bedarf nach und nach weitere Personen, Co-Entwickler, Grafiker etc. sammeln. Derzeit, so verstehe ich das, gibt es keinen festen Entwickler welcher regelmäßig sich Abends ein wenig dran setzt. Somit kann keine technische Basis entstehen und das Projekt kann insgesamt nicht vorankommen. Ich denke weiterhin das am Anfang zu viel versucht wurde zu planen was alles benötigt wird und nicht einfach mal bei kleinen Dingen angefangen. Wir erinnern uns, SW (Furunkel zu Beginn) war kurz nach der Jahrtausendwende so genial da es im Browser eine interaktive Karte auf der die Spieler laufen und interagieren konnten bot. Die Darstellung der Welt war der Beginn, der Rest ist nach und nach gekommen.

Und genauso habe ich Insulae auch angefangen. Erst Karte, dann Spieler auf der Karte, dann laufen, dann Ernten, Gebäude und so weiter.
Story hatte für mich, und das ist auch mein Eindruck aus SW, eine untergeordnete Priorität und wird auch erst durch die Spieler gelebt.
Und, es scheint eben keinen Entwickler zu geben welcher sich regelmäßig Abends ein wenig Zeit nehmen kann. Entweder gibt es einen solchen Entwickler der das ganze treibt, oder das Projektmanagement müsste einen einkaufen. Hobbyprojekt ergo kein Geld für einen Entwickler. Hobbyprojekt bedeutet auch Familie, Arbeit, Ehrenamt etc gehen vor. Geht mir ja nicht anders. Ich habe immer gesagt, ich entwickle wie eine Sinuskurve. Mal ganz viel, mal gar nicht, mal so dazwischen. Deswegen glaube ich einfach nicht das wir in der nächsten Zeit da etwas “zum anfassen” sehen werden. Die Voraussetzung um eine Basis zu schaffen sehe ich derzeit nicht.

Ich mag den Beteiligten unrecht tun wofür ich mich auch entschuldigen möchte und bereits morgen könnten wir sehen wie man auf einer “Welt in Scherben”-Scherbe umherwandern kann. Für die ehemaligen SWler würde es mich freuen.

**Update**
Natürlich war der Stand Januar 2017 gemeint, nicht wir vorhin getippt August 2017 ;)

[1]: http://pistache.io/
[2]: http://swagger.io/
[3]: http://tgwnn.rpgame.de/
[4]: http://inselpioniere.de/
[5]: http://karasan.de/
[6]: http://www.joscha2k.de/
[7]: http://www.scherbenwelten.net/


