Title: Kurze Artikellinks mit Yourls automatisch erzeugen
Date: 2014-03-05 11:44
Author: Jan H. Krüger
Category: IT
Tags: ShortURL, Wordpress, YOURLS
Slug: kurze-artikellinks-mit-yourls-automatisch-erzeugen

Da ich darauf angesprochen wurde das YOURLS ja ganz nett sei, jedoch
gerade bei Blogschreibern immer noch zu einem Zusatzaufwand führt um die
kurze URL zu erhalten, nee eben nicht. Das geht ganz automatisch.

<!--more-->Praktischerweise gibt es dazu direkt ein Plugin, nämlich den
[YOURLS Link Creator][]. Die Installation und Einrichtung ist wie bei
Wordpressplugins gewohnt einfach.

Relevant ist die Angabe zweier Parameter im Plugin[![YOURL
SLinkCreatorSettings][]][YOURL SLinkCreatorSettings]

Das erste ist eben der Pfad zu eurer YOURLS-Installation, das weite der
geheime API Key. Diesen bekommt ihr wenn ihr euch in das Adminpanel von
YOURLS einloggt, dort unter Tools. Sieht dort wie folgt aus:

[![YOURLS SecureAPI][]][YOURLS SecureAPI]Diesen Key eintragen, das war
es. Sobald ihr dann einen neuen Beitrag veröffentlicht wird euch
automatisch ein solcher Link generiert. Leider auch erst wenn ihr auf
"Publish" drückt, dich das ist denke ich verschmerzbar. Ja, das bedeutet
nur für neue Artikel oder Artikel bei denen ihr ein Update vornehmt.
Doch das sollt ja kein Ausschlusskriterium sein, oder? Zumal, bei er
normalen Bedienung landet man als Schreiber ja eh wieder auf der
Edit-Seite zum Artikel und kann sich dann direkt folgende kurze URL
kopieren. So Beispielhaft:

[![YOURLS\_WortpressLinks][]][YOURLS\_WortpressLinks]

Also, die Verbindung Wordpress-\>YOURLS funktioniert wunderbar.

  [YOURLS Link Creator]: http://wordpress.org/plugins/yourls-link-creator/
  [YOURL SLinkCreatorSettings]: http://www.janhkrueger.de/blog/wp-content/uploads/2014/03/YOURLSLinkCreatorSettings.jpg
  [YOURLS SecureAPI]: http://www.janhkrueger.de/blog/wp-content/uploads/2014/03/YOURLS_SecureAPI.jpg
  [YOURLS\_WortpressLinks]: http://www.janhkrueger.de/blog/wp-content/uploads/2014/03/YOURLS_WortpressLinks.jpg
