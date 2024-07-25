Title: Bildbearbeitung mit Python
Date: 2009-01-20 01:45
Author: Jan H. Krüger
Category: IT
Slug: bildbearbeitung-mit-python

<p>
**Als Vorbereitung der kommenden Taetigkeiten fuer Insulae, war es
noetig mich damit vertraut zu machen Bilder mit Python zu bearbeiten.
Klaro, nichts grosses. Aber die Basics mit denen ich anfangen kann.**  
  
Letztendlich soll das Ziel sein, Bilder der Spielwelt, also der Karten
zukuenftig nicht mehr mit PHP, sondern mit Python zu generieren. Denn so
kann ich diese Programme unabhaengig vom Apache starten. Wenn ich damit
dann ein wenig geuebt habe, geht es an die Erzeugung der
Statistikbilder. Denn die Auswertungen welche im Adminmenu von Insulae
angezeigt werden sollen, muessen und sollen nicht bei jedem Aufruf neu
erzeugt werden. Nein, da langt es statische Bilder zu verwenden welche
ich einmal taeglich erzeuge. Gegebenenfalls direkt nach dem Lauf von
ermittle\_statistiken.py. Aber das werde ich noch sehen.  
Erst einmal werde ich morgen, besser nachher, die erste Karte mittels
Python erzeugen. Bin mal gespannt. Ich habe noch die alten PHP-Skripte.
Ein Vergleich mit der Laufzeit ist bestimmt interessant.  
  
Was mich allerdings etwas irritiert ist, das es zwars mittels .open()
moeglich ist ein Bild zu oeffnen, es jedoch keine close() Methode zu
geben scheint. Gut, mag so sein. Empfinde ich aber als etwas
ungewoehnlich.  
  

~~~~ python
#! /usr/local/bin/python### Copyright (c) 2009, Jan H. Krueger# All rights reserved.## The contents of this file are subject to the GNU Lesser General Public# License (the "License"); you may not use this file except in# compliance with the License. You may obtain a copy of the License at# http://www.gnu.org/licenses/lgpl.html## Software distributed under the License is distributed on an "AS IS"# basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See# the License for the specific language governing rights and limitations# under the License.### File: testing_image.py# Authors: Jan H. Krueger (game.insulae@googlemail.com)# Created: (19/09/2003)# Last Updated: (19/01/2009)# Version: 1.0# Package: Test### Testprogramm with wie PIL module for image processing# just handle two image files, merge them together into an new image# and resize it.# All just quick and dirty.#import Image# open imagesimf = Image.open("101.gif")ims = Image.open("102.gif")# tell us the image propertiesprint imf.format, imf.size, imf.mode# save the image under a new nameimf.save("ausgabe.gif")# remember, it's width, then heightsize = 128, 64mode = 'RGB'box = (0, 0, 64, 64)# create an new image with the size and color previous definedimn = Image.new(mode, size)# get content of picture oneregion = imf.crop(box)# and past it to the new imageimn.paste(region, box)# after get content of picture tworegion = ims.crop(box)# Zielbereich definieren, ist ja nun um 64 Pixel verschoeben# move picture to an other place in the new picturebox = (64, 0, 128, 64)# and paste it in the new pictureimn.paste(region, box)# finally sage the new imageimn.save("zusammengesetzt.png")# and make it smaller, just half the sizeimn = imn.resize((64, 32))imn.save("kleiner.png")# notice, there are no methods to close an opened image
~~~~
