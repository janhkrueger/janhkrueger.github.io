Title: Sitemap bei Suchmaschinen manuell anmelden
Date: 2015-01-09 19:36
Author: Jan H. Krüger
Tags: Blog, Pelican, Sitemaps, SEO, Ping

Bei meinem Umstieg auf Pelican als Blogsoftware habe ich eine Funktion mit aufgegeben. Die automatische Benachrichtigung von Suchmaschinen über neue Inhalte. Klar, meine sitemap.xml ist in der robots.txt hinterlegt. Google, Bing und Yandex kennen diese auch. Rufen diese jedoch nicht zeitnah ab wenn ich neue Inhalte habe. Sprich, Pelican hat, meines Wissens nach, keine Möglichkeit diese Dienste gezielt anzupingen "Hallo, ich hab was neues".

Allerdings lässt sich das durchaus selbst vornehmen. Alle drei großen Suchmaschinen haben entsprechende Adressen über die eine Sitemap eingereicht werden kann. 

Alle im Stile:
   suchmaschine.org/pfad/sitemap?www.eigenedomain.de



Also flux ein Shell-Skript daraus gebastelt:

<iframe style="border: none; width: 100%;" src="https://janhkrueger.de/stikked/view/embed/d838d058" height="240" width="320"></iframe>


Fertig. Einfach in den Prozess einbinden wenn ein neuer Beitrag erzeugt wird auch das Skript mitläuft.
