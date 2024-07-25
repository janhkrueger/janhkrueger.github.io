Title: Google im eigenen Browsergame verwenden
Date: 2009-03-22 11:49
Author: Jan H. Krüger
Category: Insulae
Slug: google-im-eigenen-browsergame-verwenden

Auf http://buildingbrowsergames.com/ war die Tage ein recht
interessanter Artikel darueber wie die Google-Dienste innerhalb und fuer
das eigene Browsergame genutzt werden koennen. Ich kann dem ganzen zwars
nur partiell etwas abgewinnen, anderes jedoch halte ich durchaus fuer
einen erwaehnenswerten Ansatz.  
  
Das erste worauf verwiesen wird, sind die [Google Apps][]. Also die
Nutzung der Google Infrastruktur fuer das Mailhosting, Wikis, Kalender
etc. Wie einige vielleicht wissen, ist es moeglich die eigenen
mx-Eintraege auf Google zu leiten so das zum Beispiel
google@janhkrueger.de dann tatsaechlich auf Google Mail gehen wuerde.  
  
Diesem Teil des Artikels kann ich jedoch nichts abgewinnen. Sicher, die
Infrastruktur ist schnell und sehr ausfallsicher. Aber die Frage der
Datenhoheit liegt doch etwas im Magen.  
  
Der zweite Aspekt ist jedoch wesentlich interessanter. Dort wird auch
darauf eingegangen das Google mittlerweile recht umfassende und
verlaessliche AJAX Bibliotheken entwickelt hat. Da muss ich zustimmen,
da hat Google ein paar nette Spielereien durch die Vereinigung der
populaersten freien Bibliotheken. Auch sehr nett ist sicherlich die  
  
[Google Visualization API][]. Genauer gesagt finde ich die Ergebnisse
welche sich damit erzielen lassen sogar sehr genial. Aktuell pruefe ich
sogar ob ich die dortigen Tools auch fuer Insulae verwenden kann. Die
grafische Darstellung zB der Statistiken welche fuer die Moderatoren und
Administratoren bereit gestellt werden, koennte ich so komplett mittels
der APIs von Google ersetzen. Kein regelmaessiges Erstellen von Bildern
mehr, sondern die Darstellung findet komplett innerhalb des Browsers
statt. Allerdings nutze ich bereits jetzt partiell "natives"  jQuery,
daher koennte ich am Ende auch zu dem Schluss kommen das die AJAX API
von Google mir nicht wirklich viel bringt.  
  
Einziger Punkt der mich derzeit etwas stoert, ist das ich die Google
APIs derzeit wohl nur mit aktiver Internetverbindung nutzen kann. Sprich
wenn ich einmal wieder unterwegs bin und nicht gerade im ICE so das ich
die HotSpots nutzen kann... dann sieht es Mau aus. Da ist dann die von
mir ja bereits verwendete jQuery-Loesung sinnvoller, denn das kann ich
auch auf meinem Notebook ablegen und so auch ohne Netzverbindung nutzen.
Immer wenn ich will.  
  
Trotzdem kann ich dem zweiten Teil des Artikels zustimmen. Die APIs sind
genial und koennen ein Browsergame durchaus bereichern. Und zwar auf
zweierlei. Zum einen kann das Spiel sehr aufgepeppt werden, funktionell
wie auch ggf. grafisch. Andererseits muss ich als Entwickler selbst
nicht noch zusaetzlich Zeit investieren diese Dinge selbst zu erstellen
sondern kann direkt auf bereits etablierte APIs zugreiffen.  
  
Andererseits kann ich als Entwickler natuerlich auch hier ein etwas
mulmiges Gefuehl bekommen.  

-   Google koennte diesen Dienst jederzeit einstellen.
-   Ich habe keine Kontrolle ob die von Google gelieferten Versionen
    tatsaechlich dem entsprechen was die Entwickler veroeffentlicht
    haben und nicht ggf. modifiziert sind.

  
Werden im Aufruf der Bibliotheken nur die Laderoutinen geboten oder kann
Google damit durchaus auch das Nutzungsverhalten ermitteln?  
  
Schwieriges Thema welches denke ich wohl auch nie voellig aus der Welt
zu schaffen ist.  
  
   
  
Quelle: [Buildingbrowsergames][], [Google Visualization API][], [Google
AJAX Libraries API][]

  [Google Apps]: http://www.google.com/apps/intl/en/group/index.html
  [Google Visualization API]: http://code.google.com/intl/de-DE/apis/visualization/
  [Buildingbrowsergames]: http://buildingbrowsergames.com/2009/03/02/using-google-in-your-game/
  [Google AJAX Libraries API]: http://code.google.com/intl/de-DE/apis/ajaxlibs/
    "Google AJAX Libraries API"
