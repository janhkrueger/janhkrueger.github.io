Title: OwnCloud - nerviger Fehler in der Bookmarkverwaltung
Date: 2013-07-29 18:45
Author: Jan H. Krüger
Category: IT
Tags: Bookmarks, Cloud, ownCloud, SelfHosted
Slug: owncloud-nerviger-fehler-in-der-bookmarkverwaltung

Während ownCloud zwars sehr praktisch ist und im täglichen Arbeiten auch
kaum behindert hat mich eine Sache seit der Installation mächtig
gewurmt. Die Verwaltung der Lesezeichen läuft derzeit nicht rund.
Genauer gesagt ich konnte keine Tags oder Beschreibungen zu Lesezeichen
ändern und hinzufügen.

Erst dachte ich ja das dies eventuell daher kommen könnte das mein
Webhostingangebot nicht für ownCloud ideal wäre. Pustekuchen. Nachdem
ich mir die Fehlermeldungen im Adminpanel angesehen habe sah ich das
immer bei einer bestimmten Funktion ownCloud aussteigt. Konkret wird in
der Datei bookmarks.php in Zeile 299 die Verwendung der Funktion
numRows() beanstandet.

Ein wenig gegrübelt und Lösung gefunden. Die bisherige Zeile 299 mit dem
Inhalt

> if (\$result-\>numRows() == 0) exit();

kann mit den folgenden Zeilen ausgetauscht werden:

> if (\$result == 0) exit();

Und siehe da, die Verwaltung der Lesezeichen funktioniert wieder.

Wie ich mittlerweile erfahren ist dieses Verhalten bereits als Fehler
gemeldet. Es ist daher zu erwarten das in einer der nächsten Versionen
der Fehler ausgebaut ist.
