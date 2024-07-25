Title: Stikked - Unerwünschte Einträge löschen
Date: 2014-03-04 14:03
Author: Jan H. Krüger
Category: IT
Tags: SelfHosted, Spam, Stikked
Slug: stikked-unerwunschte-eintrage-loschen

Ich mag Stikked. Die Möglichkeit von Pastebin auf eigener Infrastuktur
hat echt seinen Charme. Doch es kommt auch mal vor das sich dort
Einträge finden welche ich so nicht selbst mehr haben möchte. Oder ganz
simpel, Spam. Also muss ein Weg her solche Einträge auch zu löschen.

<!--more-->Kurzer Rückblick: Stikked ist eine selfhosted Variante von
Pastebin.com welche wie dort auch erlaubt kurze Texte, Quellcode und
ähnliches zu verteilen. Stikked ist nun sicherlich nicht so komfortabel
wie Pastebin doch der Gewinn an Datenhoheit ist enorm. Die Einrichtung
auch trivial. Jedoch bietet Stikked keine Administrationstool um
Einträge zu löschen.

So, nun aber zum eigentlichem Thema. Dem Löschen unerwünschter oder
nicht mehr benötigter Einträge. Relevant dafür sind nur zwei Tabellen, `pastes` und `trending`.

In diesen beiden werden zum einen die Pastes abgespeichert und zum
anderen die Beliebtheitsanzeige gesteuert.Um nun einen Eintrag zu
löschen wird die eindeutige ID des Eintrages benötigt. Ist ganz leicht,
das ist die etwas kryptische Zeichenkette in der URL. Uum Beispiel `https://janhkrueger.de/stikked/view/3a07a81d`

Also lautet die ID `3a07a81d`

Mit dieser ist es dann möglich zwei DELETE-Query auf die
Stikked-Datenbank abzusetzen:

    DELETE FROM pastes WHERE pid='3a07a81d';  
    DELETE FROM trending WHERE paste_id='3a07a81d';

Fertig, Eintrag verschwunden. Für immer. Und wenn das DB-Backup aus der
Rotation verschwunden ist, ist der Eintrag auch für immer weg :)
