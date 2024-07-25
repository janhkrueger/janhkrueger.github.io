Title: Dokuwiki 
Date: 2013-11-04 12:35
Author: Jan H. Krüger
Category: IT
Tags: Dokuwiki, uberspace, Wiki
Slug: dokuwiki

Nach meinem Umzug zu Uberspace habe ich gleich noch ein paar weitere
Dienste wieder aktiviert. Unter anderem ein Wiki, basierend auf
[Dokuwiki][].

Dokuwiki hat für mich einen gewissen Charme. Die Einträge liegen in
Dateien vor was eine Sicherung erleichtert. Einfach das gesamte
Wikiverzeichnis sichern und die Einträge sind gleich enthalten.

Zur Installation: mittels ssh am Server anmelden wie gewohnt und dann in
das HTML-Verzeichnis wechseln. Dokuwiki laden und entpacken.

> cd html/
>
> wget http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz
>
> tar xvfz dokuwiki-stable.tgz

Schon steht Dokuwiki unter deinedomain.tld/dokuwiki bereit.

In meinem Falle will ich das Wiki jedoch unter einer eigenen Subdomain
ansprechen. Also noch zwei Zeilen eingetippt:

> cd /var/www/virtual/[USER]
>
> ln -s html/dokuwiki wiki.deinedomain.tld

Tja, das war es auch schon mit der Installation, fehlt nur noch die
Einrichtung. Diese wird mittels der install.php im Wikiverzeichnis
gestartet. Einfach im Browser aufrufen, zum Beispiel:

> deinedomain.tld/dokuwiki/install.php

Die dortigen Angaben waren (für mich) selbsterklärend. Wer es gerne
schön haben möchte, insbesondere mit den URLs, den verweise ich an
dieser Stelle auf [Netzleben][]. Dort hat Florian Schmidt bereits etwas
dazu geschrieben.

Für Bastler unter interessierte gibt es dann noch das umfangreiche
Pluginarchiv für Dokuwiki zu durchforsten. Was ich mir bei Gelegenheit
ansehen werde ist wie ich die Formatierung von Mediawiki auch in
Dokuwiki anwenden kann. Das wird es mir erleichtern meine Inhalte von
verschiedenen Wikis hier bei mir zentral zu archivieren.

Quellen: [Dokuwiki][], [Uberspace][]

  [Dokuwiki]: https://www.dokuwiki.org/start?id=de:dokuwiki "Dokuwiki"
  [Netzleben]: http://netzleben.com/2013/09/dokuwiki-installieren/
    "Dokuwiki installieren / URL"
  [Uberspace]: https://uberspace.de/ "Uberspace"
