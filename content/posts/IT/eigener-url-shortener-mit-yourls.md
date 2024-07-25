Title: Eigener URL-Shortener mit YOURLS
Date: 2013-07-29 14:52
Author: Jan H. Krüger
Category: IT
Tags: bit.ly, goo.gl, SelfHosted, Shortener, URL-Shortener, YOURLS
Slug: eigener-url-shortener-mit-yourls

Im Zuge der Trennung von externen Dienstleistern, insbesondere
auskunftsfreudigen Vertretern bin ich noch über einen weiteren Dienst
gestolpert welchen ich ab und an einmal nutze. Einen URL-Shortener. Nach
einer kurzen Recherche hab ich auch eine Lösung gefunden selbst einen
Shortener zu hosten. Und zwar YOURLS.

Eigentlich ist das Prozedere schnell erklärt. [YOURLS][] kann direkt von
der Webseite aus bezogen werden. Dann flux eine Datenbank dafür
eingerichtet, in der Konfiguration eingetraten, per FTP die Quelldateien
hochgeladen und fertig. Danach kann unter http://deinedomain.de/admin
das Adminpanel gestartet werden über welches die weitere Installation,
anlegen und füllen der benötigten Tabellen in der Datenbank sowie
erstellen der .htaccess-Datei erfolgt. Das Aufsetzen kann innerhalb
weniger Minuten erledigt sein.

Wenn ich nun das Adminpanel bei mir aufrufe erscheint derzeit folgende
Anzeige. [![YOURLS\_AdminPanel][]][]Kurz und übersichtlich. Nun kann ich
mich an die Migration der von mir auf bit.ly und goo.gl  gekürzten URLs
ransetzen.

Zu jedem gekürzten Link gibt es noch eine kurze Statistikseite. Kann
wohl hilfreich sein. Mich persönlich interessiert allerdings nicht wie
oft, aus welchen Ländern und wann ein Kurzlink aufgerufen wurde. Ich
denke hier werde ich noch mal recherchieren ob ich diese Statistiken
ausschalten kann.

[![YOURLS\_Statistiken][]][]  
Bei mir hat es noch ein wenig länger gedauert. Ein URL-Shortener kann
seine Aufgabe natürlich nur dann effizient erledigen. Nun ist meine
eigentliche Domain, janhkrueger.de, dafür in meinen Augen nicht mehr
geeignet. Also habe ich, da noch freie Domains in meinem Paket über,
nach einer neuen, kurzen Domain gesucht. Leider ist jhk.de bereits
vergeben. Noch ein paar Minuten Recherche bin ich dann auf jhk.li
gestoßen und habe sie direkt registriert. j.hk wäre natürlich auch
klasse doch diese bietet mein Hoster all-inkl.com leider nicht an.

Wie auch immer, ab sofort kann ich mit einem eigenen Dienst meine Links
abkürzen. Wie hier mit einem Link zu meinem öffentlichem GPG-Schlüssel:
[http://jhk.li/1][]

  [YOURLS]: http://yourls.org/
  [YOURLS\_AdminPanel]: http://www.janhkrueger.de/blog/wp-content/uploads/2013/07/YOURLS_AdminPanel-300x149.jpg
  [![YOURLS\_AdminPanel][]]: http://www.janhkrueger.de/blog/wp-content/uploads/2013/07/YOURLS_AdminPanel.jpg
  [YOURLS\_Statistiken]: http://www.janhkrueger.de/blog/wp-content/uploads/2013/07/YOURLS_Statistiken-300x182.jpg
  [![YOURLS\_Statistiken][]]: http://www.janhkrueger.de/blog/wp-content/uploads/2013/07/YOURLS_Statistiken.jpg
  [http://jhk.li/1]: http://jhk.li/1
