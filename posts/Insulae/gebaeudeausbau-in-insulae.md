Title: Gebäudeausbau in Insulae
Date: 2009-05-30 23:43
Author: Jan H. Krüger
Tags: Insulae, Gebäude, Ausbau

Vor ein paar Tagen habe ich angefangen die Grundlagen fuerfür die
individuellen Gebäudeausbauten DB-seitig zu legen.

  

Was sind diese Gebäudeausbauten eigentlich? Nun, in Insulae kann ein
Gebäide ueber mehrere "AddOns" verfügen. Diese AddOns haben Einfluss
auf die maximale Produktionsmenge innerhalb eines definierten
Zeitraumes. Je höger die Stufen eines "AddOns", umso stärker die
Produktion.

  

Während bei allen produzierenden Gebäuden die Fertigkeiten der
Insassen, ein von der Gebäudeart abhängiger Koeffizient und die
Landgüte eine Rolle spielt, fliesst grundsätzlich noch die Stufe der
für jeden Gebäudetyp unterschiedlichen Ausbauten hinzu. Bei den reinen
Veredelungsgebäuden spielt die Landgüte allerdings keine Rolle.

  

Dabei besitzt jedes Gebäude sein eigenes Set an Ausbauten. In einem
Bauernhof ist es zum Beispiel möglich die Felder und Ställe
aufzuwerten um die Produktion von Getreide und Kühen anzukurbeln.
Felder und Ställe ergeben jedoch bei einer Goldmine keinen Sinn, dafür
gibt es dort Stollen welche die Goldförderung antreiben. Auch die zum
Steigern dieser Ausbaustufe nötigen Waren sind dabei unterschiedlich
und sind von dem Ausbau, nicht vom Gebäude abhängig.

  

Dies umzusetzen ist auf verschiedene Arten möglich. Zum einen haette
ich von vornherein sagen können das es nur n Ausbauten geben darf. Und
im folgenden dann lediglich hart codieren das Ausbau 1 bei dem Bauernhof
eben "Felder" heisst und bei der Goldmine "Stollen", die benötigten
Waren ebenfalls hart codiert in den Skripten hinterlegen. Das empfinde
ich aber als eine unfeine Einschränkung der Möglichkeiten. Also blieb
mir nur die Variante sowohl die einzelnen Ausbauten, aber auch deren
kosten flexibel in der Datenbank zu hinterlegen. Aus folgendem Grunde.
Ich möchte mir die Möglichkeit offen halten schnell Änderungen am
System zu ermöglichen. Änderungen welche gegebenenfalls auch von reinen
Moderatoren vorgenommen werden können anhand einer Onlinemaske und
nicht eine Änderung im Programmcode erfordern. Die Konsequenz,
Performanceeinbußen, sind mir durchaus bewusst. Aber bei Insulae geht es
ja nicht allein um Performance, sondern um eine technische Spielwiese.

  

Ich habe also um ein Gebäude zu verwalten 5 Relationen in meine
Datenbank. In der Relation __archetyp.haus__ sind die Grundlegen Daten der
Gebäude abgelegt. Die Individuelle ID, der Name, Beschreibung etc. Zu
einem Gebäude sind dann in der Relation __archetyp.haus\_ausbau__ die für
ein Gebäude zutreffenden AddOns abgelegt, ebenfalls mit Name,
Beschreibung und so weiter. Ein Gebäude kann keines, eines oder mehrere
AddOns besitzen. Dazu referenzierend gibt es noch eine Relation
__archetyp.haus\_ausbau\_ware__ in welcher abgelegt ist welche Waren fuer
eine Steigerung der Stufe notwendig sind. Dabei wird von einer
Berechnung von

  

    benötigte Warenmenge = aufrunden(S + 1 \* G \* P)

  
Wobei  

-   S die aktuelle Stufe des Ausbau ist
-   G die Grundwarenmenge
-   und P der Phasenkoeffizient.

  

ausgegangen. Diese Berechnung wird fuer jeden Warentyp vorgenommen. Wie
leicht zu erkennen ist, wird ein Ausbau mit jeder weiteren Stufe teurer.
Der Phasenkoeffizient kann genutzt werden um die Kosten pro Phase
unterschiedlich zu gestalten. In meiner primären Phase nutze ich hier
den Wert 1.0. In einer "Speed-Runde" ist denkbar den Wert hierfuer
niedriger zu halten um schneller an höher ausgebaute Gebäude zu
gelangen. Aber, steuerbar ohne noch nachträglich in den Programmcode
einzugreiffen.

  

Wird nun ein neues Gebäude gebaut, wird ein neuer Eintrag in der
Relation __welt.haus__ erzeugt. Aus dieser geht eindeutig hervor wem das
Gebäude gehoert, welcher Gebäudetyp es ist, wo es steht, zusätzlich
zu ein paar weiteren Werten. Die Insert-Query aktiviert dabei gleich
einen Trigger welcher in der Relation __welt.haus\_ausbau__ die Einträge
über die für das Gebäude vorliegenden Ausbauten vornimmt. An dieser
Stelle ist bewusst ein Trigger verwendet worden um diese Logik nicht
zusätzlich im Programm abzulegen. Gleichzeitig sind in
__welt.haus\_ausbau__ auch die Stufen der Ausbauten hinterlegt.

  

Warum nun der ganze Aufwand? Ganz einfach:

  

-   eine Onlinemaske um ein neues Gebäude samt Kosten, Bauland etc. zu
    hinterlegen anzulegen
-   eine Onlinemaske um für einen Gebäudearchetyp ein neues AddOn zu
    erstellen und mit Baukosten zu hinterlegen
-   eine weitere Maske um einen Gebäudearchetyp im Spiel zu aktivieren
    bzw. zu deaktivieren.
-   weiterin eine Maske um die Daten eines Ausbaus zu verändern. Kann
    ja sein das ich die Kosten nachträglich nochmal veraendern will.

  

Und schon habe ich eine Verwaltung welche kaum noch Eingriffe in den
Programmcode erfordert, eine Verwaltung welche auch von nicht
technischem Personal erfolgen kann. Ebenso ist es ueber die Daten eines
Ausbaues auch möglich seine Produktionsformel grundlegend zu
verändern. Die Gewichtung der einzelnen Parameter welcher über die
Produktionshöhe entscheiden ist so ebenfalls ohne codeseitige Arbeiten
möglich. Komplex in der Realisierung und auch fuer die
Produktionsauswertungen nicht das schnellste, aber was ist heutzutage
schon nach viel begrenzte Rechenkapazitaet im Vergleich zu vor fünf
Jahren? :) Ganz davon abgesehen das ich hier auf einer technischen
Spielwiese unterwegs bin, nicht im realen Leben.

  

Klar, in den Relationen stecken noch ein paar Elemente mehr, welche ich
hier jedoch nicht weiter erläutern will. Aber wer Insulae oder
Scherbenwelten kennt, der weiss das noch irgendwo die Information sein
muss was in einem Gebäude produziert wird. Generell gilt jedoch:

  

    Ertrag = (S = 1) \* A \* (F/8) \* H \* W \* G \*P

  

Wobei

  

-   S die Fertigkeitsstufen der Insassen,
-   A die Stufe des Ausbaus,
-   F die Feldstärke,
-   H der für dieses Gebaeude spezielle Koeffizient,
-   W die Modifikation gemäß des aktuellen Wetters,
-   G ein Globaler Produktionsmodifikator ist und
-   P ein für die Phase gültiger Koeffizient ist.

  

Der Skill wird wahrscheinlich von mir irgendwann noch einmal
differenziert in Gesamtskill, höchster Einzelskill, geringester
Einzelskill etc. Für den ersten Betrieb langt mir aber dieses
Berechnungsmodell. Klingt erstmal kompliziert, ist es aber in keinster
Weise. Und durch ein paar Filternde Tricks wird auch die
Auswertungsrunde, also die Berechnungs wenn alle Gebäude in Insulae
produzieren, auch nicht umständlich in die Laenge gezogen.

  

Einen weitere Möglichkeit hat dieses System: Ich bin in der Lage einem
Gebäude einen Ausbau zuzuordnen den dieser Gebäudetyp für gewöhnlich
nicht besitzt. Eine Holzhütte die auch gleich Fleisch produziert?
Einfach den Ausbau dem spezifischen Gebäude eines Spielers zuweisen und
fertig. Keine statischen Gebäude mehr, sondern eine flexible Grundlage.
Lediglich an zwei Stelle habe ich begrenzend die Strukturen gebildet:

  

-   es kann nur eine Fertigkeit für die Produktion eines Ausbaus
    herangezogen werden
-   ein Ausbau kann nur eine Ware produzieren

  

Dieses auch noch weiter zu unterteilen wuerde dann, sogar fuer meine
Verhältnisse, unnötige Einbussen auf die Betriebsgeschwindigkeit
besitzen.

  

Das sind die Grundzüge meiner Gebäudestruktur. Datenbankseitig steht
alles, Grundzüge sind auch bereits in den den Spielern zur Verfuegung
stehenden Skripten enthalten. Lediglich die Onlinemasken für die
Verwaltung stehen noch nicht. Aber die kommen noch. Und wer weiss,
eventuell fällt mir ja noch bei der Implementierung der anderen Dinge
etwas ein was dort berücksichtigt werden muss.
