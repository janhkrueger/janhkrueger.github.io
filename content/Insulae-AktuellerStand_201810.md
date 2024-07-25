Title: Insulae - Oktober 2018 Status
Date: 2018-10-25 14:50
Author: Jan H. Krüger
Tags: Insulae, Zwischenstand, PBBG, Browsergame
Category: Insulae
Slug: insulae-stand-oktober2018
Series: Insulae-Stand

Moin zusammen!

der Oktober war für Insulae ein, technisch gesehen, sehr produktiver Monat. Primär daraus gekommen das ich zwischen meinem Ende bei meinem alten Arbeitgeber und dem Start beim neuen Arbeitgeber drei Wochen Zeit hatte, aber auch da ich entsprechend motiviert war.

* Kleinere Anpassungen an der Buildinfrastruktur
* Verlagerung der Issues in ein anderen Repository
* Historiendaten nun per API
* Historienapi in der Oberfläche eingebunden
* Marktdaten nun in der Stadtapi


An der Buildinfrastruktur habe ich primär die URL von meinem Gitrepository verändert. Anstatt gitlab.* nun git*. Eine rein kosmetische Änderung. Leider habe ich auch am Montag den 22. auch die Integration zwischen Jenkins und Gitlab gekillt. Offenbar so gut das ich es bisher nicht wieder hinbekommen habe. Vorher wurde bei jedem Push ein Build gestartet. Das funktioniert derzeit nicht mehr. Derzeitige Lösung: einfach jede Stunde das System bauen. Nicht schön, aber läuft erstmal.

In Gitlab selbst habe ich eine schöne Eigenschaft entdeckt welche ich direkt nutze. In Gitlab ist es möglich in einem Projekt zwar das eigentliche Repository, also den Quellcode privat zu halten, die Issues jedoch öffentlich. In Github musste ich früher dafür zwei separate Projekte anlegen. Daher auch die Projektnamen "insulae-private" und "insulae-public". Das kann ich mir nun komplett sparen. Es gibt weiterhin die Möglichkeit Issues als "Confidental" zu markieren. Damit kann ich steuern das ein Issues doch nur für die Projektmitglieder zu sehen ist und eben nicht öffentlich ist. Alles in allem jedoch für mich sehr angenehm von der Verwaltung da ich im Grunde nur noch ein Projekt pflegen muss.

Die Historiendaten sind nun vollständig mittels API bereitgestellt. Per Phase getrennt aber auch selektiv pro Kategorie. Weiterhin sind die per API bereitgestellten Daten auch gleich in der spielinternen Oberfläche eingebunden. Zur Darstellung der Historieneinträge wird also nicht mehr mittels SQL-Anweisung abgefragt sondern der zugehörige JSON-Stream per API gelesen. Für das Testsystem sieht das zum Beispiel gerade so aus:

Unpraktisch ist noch das Einträge dort immer noch als unix timestamp hinterlegt sind. Das ist ein Thema das ich bei Gelegenheit einmal angehen werde. Dennoch, der Issue ist die Nummer [Issue #69][1], also bereits zur Umsetzung vorgesehen ;)


Ein riesen großer Schritt vorwärts ist jedoch der Punkt das nun die Marktdaten einer Stadt ebenfalls in der API hinterlegt sind. Bisher wurde nur die ID des Primärmarktes ausgewiesen, welche Waren dort zum Handel angeboten werden war dort jedoch noch nicht hinterlegt. Dies ist seit heute anders. Damit kann perspektivisch die Anzeige auch direkt in die API übernommen werden, der derzeit zugehörige PHP-Code in die Rente geschickt werden. Dabei habe ich im Hintergrund die Struktur wie Waren gelagert werden etwas geändert. Ich arbeite im Hintergrund nun nur noch mit Märkten (wird noch auf etwas wie Warenlager oder so umbenannt). Dabei ist es mir erst einmal egal wie die Waren herkommen, ob aus einer Stadt, einem Handelsposten, das Lager eines Gebäudes damit gemeint ist oder in der Theorie auch jene Waren welche auf der Hand einer Gruppe liegen.
Da in ~80 Prozent der Fälle die Warenlisten nur gelesen und angezeigt werden kann ich hier direkt an mehreren Stellen in der Oberfläche ansetzen.
Bürgermeister können natürlich auch hier selbst festlegen ob die Daten ihrer Stadt in der öffentlichen API gelistet werden sollen oder nicht. Dabei ist nur ein "Alle oder Nix" möglich. Auf Einzelwarenbasis ist eine Steuerung derzeit nicht möglich und von mir zum aktuellen Stand auch nicht vorgesehen.
Um das zu erreichen habe ich die Waren jedoch aus der Stadt rausgenommen und an einen Marktplatz gehängt. Ich muss dazu jeder Stadt noch einen Primärmarkt zuweisen und die Waren migrieren da ich es vorgezogen habe eine neue Datenstruktur aufzubauen und nicht das alte irgendwie zurecht biege.
Wenn alles so läuft wie ich das erwarte, kann ich am Wochenende auch den Schalter betätigen und die Änderung produktiv legen.

Ebenfalls kann ich nun ohne viel Aufwand eine andere Sache umsetzen die ich schon länger haben wollte. Verbundene Märkte. Also ein Marktplatz welcher über verschiedene Zugangswege, eine Stad, einen Handelsposten oder ähnliches erreicht werden kann. Der Inhalt des Marktes jedoch ist überall identisch. Das ist mehr eine Story- und Rollenspielgeschichte und weniger ein knallhartes, dauerhaft verfügbares Feature. Ich bin auch noch nicht sicher ob es irgendwann Spielern möglich sein wird solch verbundene Märkte selbst zu betreiben. Aber mal sehen.

Kleiner Wermutstropfen das nun die Waren ebenfalls in der Stadtapi enthalten sind: der Response ist von 1KB auf 5KB gestiegen. Die Waren alleine benötigen 4K. Mal schauen. Aber die 4K sind derzeit das Maximum. Waren welche nicht in einer Stadt lagern, werden, Stand heute, nicht angezeigt.

![StadthandelAPI](images/Stadthandel_API.png)

Und dann im Spiel:
![Stadthandel](images/Stadthandel.png)


Bis zum nächsten Monat.

[1]: https://git.janhkrueger.de/insulae/insulae-private/issues/69
[2]: https://api.insulae.janhkrueger.de/town
