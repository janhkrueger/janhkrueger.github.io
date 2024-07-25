Title: Umstieg auf Pelican
Date: 2014-04-07 12:36
Author: Jan H. Krüger
Category: IT
Tags: Blog, Pelican, Wordpress
Slug: umstieg-auf-pelican


Am Wochenende bin ich mit meiner Blogsoftware ganz umgestiegen. Habe ich bisher viele Jahre lang Wordpress eingesetzt, kommt bei mir nun [Pelican][1] zum Einsatz. Pelican ist eine in Python geschriebene Software welche ein statisches Blog generiert. Ja, genau, statische HTML-Dateien. Ziemlich retro in Zeiten der dynamischen Sprachen oder? Im Grunde jedoch absolut ausreichend.

Zur Installation mag ich gar nichts mehr schreiben. Da gibt es mittlerweile genug Anleitungen im Netz für die verschiedenen Umgebungen. Ob nun aus dem Quellcode selbst, mittels apt, yum oder sonstwie, es gibt denke ich für jede Umgebung mittlerweile genug Anleitungen. Daher hier nur ein paar Zeilen wie ich Pelican bei mir betreibe.

## Generierung des Blogs
Das Blog wird nach erfolgter Installation bei mir per CronJob wie folgt aufgerufen:

```
# Pelican aktualisieren
27 * * * * pelican /var/pelican/content -o /var/pelican/output -s /var/pelican/pelicanconf.py
```

Der erste Parameter ist der Ordner mit den Inhalten im Markdownformat. Der zweite Parameter definiert den Ausgabeort und abschließend wird noch die Konfigurationsdatei von Pelican genannt. Jede valide Eingabedatei im ersten Verzeichnis wird als HTML-Datei im Ausgabeort abgelegt.

## Import der alten Wordpresseinträge
Natürlich will ich keine alten Einträge verlieren sondern diese von Wordpress übernehmen. Praktischerweise bietet Pelican hier auch direkt ein entsprechendes Tool bereit. [Pelican-Import][2]. Bedeuted:

```
pelican-import --wpfile -m markdown -o content jhk.wordpress.2014-04-07.xml
```

Damit habe ich dann alle Einträge in Markdowndateien umgewandelt. Allerdings war der Authorname noch nicht ok. Hier stand der interne Wordpressbenutzer. Also fix korrigiert:

    perl -pi -e 's/Author: olduser/Author: Jan H. Krüger/g' *

Es gibt noch ein paar weitere Anpassungen welche sich im Grunde auf nicht mehr korrekt verlinkte Bilder beziehen. Dies wird auch beim Generieren als Warnung ausgegeben. Fürs erste habe ich eine quick & dirty Lösung gewählt. Die Bilder irgendwann einmal neu zu verlinken, naja, irgendwann einmal.
Nun kann das Blog generiert werden und kann online gehen.

## Plugins
Pelican kann auch sehr gut mit [Plugins][3] erweitert werden.
Bisher habe ich gerne ein paar der PlugIns von Wordpress genutzt. Sie haben mir Tätigkeiten abgenommen und oftmals das Blog frei von Spam gehalten. Betrachte ich die mal genauer fallen mir direkt zwei Kategorien ein. "Nicht mehr benötigt" und "Pelican-Intern". 

### Nicht mehr benötigt.
Die Plugins aus der "Nicht mehr benötigt" Kategorie sind im Grunde all jene welche sich um eventuell Spam kümmern. Ohne Kommentarsystem gibt kann es auch keinen Spam mehr geben. Gleichfalls entfällt die Notwendigkeit die IP von Kommentaren wieder zu entfernen.
Gleichfalls entfällt die Notwendigkeit von Cachify. Da nichts mehr dynamisch generiert wird muss auch nichts in diesem Prozess beschleunigt werden.

### Pelican-intern
Plugins dieser Kategorie habe ich bisher eingesetzt, kann die Funktionalität jedoch mittels Pelican, einem Plugin dort oder über das Theme abbilden.

#### Inhaltslizenz angeben
Die Lizenzangabe zum Beispiel. Das erlaubt mir das hier eingesetzte Theme direkt. Einfach folgende Zeilen in die Konfigurationsdatei schreiben:

```
# Lizenz einstellen
CC_LICENSE = 'CC-BY-NC-SA'
```

#### Sitemap generieren
Eine Sitemap für Suchmaschinen kann auch automatisch angelegt werden. Dazu muss das Plugin in der Konfigurationsdatei aktiviert werden:

```
# Plugin Verwaltun
PLUGIN_PATH = '/var/git/pelican-plugins'
PLUGINS = ['sitemap']
```

## Verwaltung mit ownCloud
### Artikel
Praktischerweise kann ich die Einträge für das Blog auch gleich mittels ownCloud verwalten und auch schreiben. Dazu lege ich in ownCloud einen eigenen Ordner an "Blog". Mittels des integrierten Editors kann ich Textdateien auch direkt bearbeiten. Das trifft auch für Markdowndateien mit der Endung .md zu.
Meine Arbeitsschritte zum Verfassen eines neuen Beitrages sehen nun wie folgt aus:

* Anlegen einer neuen Datei mit der Endung .txt
* Verfassen des Artikes in dieser Datei
* Änderung der Endung auf .md sobald der Artikel fertig ist.

Sobald das regelmäßig laufende Skript zur Erzeugung des Blogs startet wird der Artikel veröffentlicht. Das wars.

Auf die gleiche Weise kann ich auch Artikel aus dem Blog wieder zurück ziehen. Ich ändere einfach die Endung da Pelican nur mit definierten Dateien arbeitet, alle anderen im Verzeichnis stehenden Dateien jedoch ignoriert.

### Konfiguration
Das ganze geht natürlich noch weiter. Auch die Konfigurationsdatei kann ich über das Verzeichnis mit ownCloud im Zugriff halten. Denn da eine .py-Datei ja im Grunde auch nur eine Textdatei ist, kann ich die ebenfalls elegant per ownCloud bearbeiten.
Dank entsprechender Apps für Android kann ich also auch von unterwegs problemlos das Blog (fast) komplett steuern.
Und da Pelican ja keine Datenbank oder ähnliches verwendet kann ich die Konfiguration auch problemlos verteilen:

<iframe src="https://janhkrueger.de/stikked/view/embed/a0e70c43" style="border:none;width:100%"></iframe>

### Hinweis
Bei mir ist es bei der automatischen Generierung erst einmal ständig zu Fehlern gekommen da Pelican sich die falsche Pythonversion zog. Wenn ihr mehrere Pythonversionen gleichzeitig im Einsatz habt: Kontrolliert eure Pade und Settings. Spart Zeit ;)



[1]: http://blog.getpelican.com/        "Pelican"
[2]: http://docs.getpelican.com/en/3.3.0/importer.html        "Pelican-Import"
[3]: https://github.com/getpelican/pelican-plugins "Pelican-Plugins"
