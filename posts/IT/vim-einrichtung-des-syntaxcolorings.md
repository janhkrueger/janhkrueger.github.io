Title: Vim - Einrichtung des Syntaxcolorings
Date: 2013-06-28 16:24
Author: Jan H. Krüger
Category: IT
Tags: Editor, Syntaxcoloring, VIM
Slug: vim-einrichtung-des-syntaxcolorings

Bei meiner Arbeit mit Linux führt es mich trotz allem Komforts den es
mittlerweile für Linux gibt immer wieder zurück zur Konsole.

Mein bevorzugter Editor dort nennt sich VIM. Große Teile von Insulae
sind in ihm entstanden.

<!--more-->

Also schnell installiert:

> sudo apt-get install vim

VIM ist allerdings mitnichten nur ein einfacher Editor für die Konsole.
Er lässt sich gut mittels Skripten erweitern und anpassen. Zum Beispiel
mit Syntaxeinfärbung für Python und PHP.

Um die Syntaxeinfärbung auch gleich beim Laden einer Datei zu starten
müssen die Quelldateien in einem speziellen Verzeichnis liegen sowie in
der Konfigurationsdatei von Vim eine Zeile eingetragen werden. Alles
schnell angelegt:

> mkdir \~/.vim  
>  mkdir \~/.vim/syntax

Normalerweise liegt die Konfigurationsdatei .vimrc direkt im
Homeverzeichnis. Ich ziehe es allerdings vor die Dateien einer
Anwendung, in diesem Falle eben VIM, unter einem Verzeichnis zu
konzentrieren. Also lege ich sie im oben bereits angelegten Verzeichnis
an und erstelle dann einen Symlink an den eigentlichen Ort damit VIM sie
dennoch findet. Wenn ich gezwungen werde eine Sicherung meiner
VIM-Einstellungen durchzuführen muss ich nur ein Verzeichnis anpacken.
Also:

> touch \~/.vim/vimrc

In diese muss noch die Zeile "syntax on" eingetragen werden. Um
eventuelle Inkompatibilitäten gleich zu umgehen schadet ein "set
term=ansi" ebenfalls nicht.

Nun noch den schon erwähnten Symlink anlegen:

> ln -s \~/.vim/vimrc \~/.vimrc

Fertig. Theoretisch ist VIM nun (für mich) einsatzbereit. Fehlen nur
noch die Definitionen für die Farbschemata von Python und PHP.

Für Python nutze ich folgendes
Skript:[http://www.vim.org/scripts/script.php?script\_id=79][], für PHP
nutze ich folgendes:
[http://www.vim.org/scripts/script.php?script\_id=4159][]

Beide .vim-Dateien müssen in den Ordner \~/.vim/syntax abgelegt werden.
Das war es auch schon.

In der Konfiguration kann natürlich noch mehr abgelegt werden. Zum
Beispiel wie weit ein Tab sein soll. Beispielhaft meine derzeitige
Konfiguration:

<iframe style="border: none; width: 100%;" src="https://janhkrueger.de/stikked/view/embed/bd8013ac" height="240" width="320"></iframe>

  [http://www.vim.org/scripts/script.php?script\_id=79]: http://www.vim.org/scripts/script.php?script_id=790
  [http://www.vim.org/scripts/script.php?script\_id=4159]: http://www.vim.org/scripts/script.php?script_id=4159
