Title: Metadaten in Dokumenten bereinigen
Date: 2013-06-29 14:58
Author: Jan H. Krüger
Category: IT
Tags: Anonymisation, Clean, Metadata, Privacy, Script
Slug: metadaten-in-dokumenten-bereinigen

Nicht nur Dokumente oder die Kommunikation an sich können
zurückverfolgbare Spuren hinterlassen, auch die Metadaten in einem
Dokument an sich enthalten potentiell Inhalte welche den Ersteller
identifizieren können.

Um sich dieses Themas anzunehmen gibt es mittlerweile genügend Software.
Ein Tool dafür ist mat, kurz für Metadata Anonymisation Toolkit.
Einziger Haken, es kann immer nur eine Datei bearbeiten. Da ich
allerdings oft auch mehrere Onlineartikel hintereinander als PDF
abspeichere will ich nicht jedes Mal mat explizit aufrufen. Also habe
ich mir noch ein kleines Shellskript drumherum gebastelt welches für
mich alle Dateien eines vorgegebenen Dateityps in einem Verzeichnis
bearbeitet. Gleichzeitig werden im Dateinamen eventuelle Leerzeichen
gegen Unterstriche ausgetauscht.

Die Benutzung ist, wenn mat an sich im System bereits vorhanden ist,
simpel. Einfach ein

> strip\_metadata [Dateityp]

eingeben und alle Dokumente des mit [Dateityp] spezifizierten Typs
werden von mat bereinigt. Fertig.

<iframe style="border: none; width: 100%;" src="https://janhkrueger.de/stikked/view/embed/6327b6be" height="240" width="320"></iframe>

Die ganze Thematik wird auch noch einmal auf [mat.boum.org][] oder auch
bei den [Reporters without Borders][].

  [mat.boum.org]: https://mat.boum.org/
  [Reporters without Borders]: https://www.wefightcensorship.org/article/metadata-your-files-talk-youhtml.html
