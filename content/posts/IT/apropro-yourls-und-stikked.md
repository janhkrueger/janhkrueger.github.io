Title: Apropro YOURLS und Stikked...
Date: 2014-03-05 17:46
Author: Jan H. Krüger
Category: IT
Tags: SelfHosted, Stikked, YOURLS
Slug: apropro-yourls-und-stikked

Wo ich gerade dabei bin ... auch diese beiden Tools lassen sich mit
einander verbinden. Wie das geht findet ihr im Artikel.

Möglich wird dies durch eine Anpassung in Stikked welche mit der Version
0.8.6 eingeführt wurde. Im Changelog finden wir:

<!--more-->

-   New translations: Portuguese, Norwegian, Turkish, French
-   New theme: Snowkat
-   **YOURLS support ([http://yourls.org/][])**
-   There is now a stikked.php.dist. You may copy that to config.php and
    have your own settings
-   The API has more possibilities, see API doc
-   Captcha must be entered only once, no more for further pastes
-   Bugfixes and improvements

Der YOURLS Support ist endlich da. Die Einrichtung ist auch schnell
erledigt. Im Ordner stikked/application/config/stikked.php müssen zwei
Zeilen hinzugefügt werden bzw. angepasst. Ich musste sie hinzufügen da
ich meine Konfigurationsdatei aus Version 0.8.5 einfach übernommen habe.
Dort sind jedoch die notwendigen Zeilen noch nicht enthalten.

> \$config['yourls\_url'] = '';  
>  \$config['yourls\_signature'] = '';

Der erste Parameter ist die URL zu eurer YOURLS Installation, der zweite
der API-Key welcher unter YOURLS-\>admin-\>Tools zu finden ist. Diese
kryptische Zeichenkette:

[![YOURLS SecureAPI][]][YOURLS SecureAPI]

 

Eingerichtet findet sich nun bei der Erstellung eines neuen Pastes unten
Rechts der Punkt "Kurzurl generieren". Wird das Häkchen aktiviert
erstellt Stikked automatisch im Hintergrund eine neue Kurzurl. Wie diese
lautet wird auch auch direkt nach dem Speichern angezeigt. Also kein
umständliches rumflriemeln zwischen den Systemen.

Alles in allem eine Sache von nur zwei Minuten sofern Stikked bereits in
der Version 0.8.6 vorliegt. Wenn nicht, wie bei mir, werden es noch ein
paar Minuten mehr zum Upgrade von Stikked.

  [http://yourls.org/]: http://yourls.org/
  [YOURLS SecureAPI]: http://www.janhkrueger.de/blog/wp-content/uploads/2014/03/YOURLS_SecureAPI.jpg
