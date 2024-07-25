Title: Bots fuer Browsergames mittels Python
Date: 2009-01-28 15:14
Author: Jan H. Krüger
Category: IT
Slug: bots-fuer-browsergames-mittels-python

<p>
Eher durch Zufall bin ich die Tage auf ein Pythonpaket aufmerksam
geworden, welches sich als enorm maechtig erwiesen hat. Das Paket
Mechanize gibt sich wenn es Webseiten einliest, dabei also Browser aus.
Ja, es verwaltet die Cookies sogar selbststaendig. Was ist die
Konsequenz daraus? Es ist damit sehr leicht moeglich sich in
Browsergames einzuloggen und direkt Automatismen zu realisieren.  
  
Gesagt getan, ein wenig rumprobiert und ich konnte mich mit einem kurzen
Testskript in Insulae einloggen und meine aktuellen AP auslesen. Doch,
Insulae ist ja "nur" ein Klon von Scherbenwelten. Ob ich damit auch in
Scherbenwelten agieren konnte? Zugegeben, es war spaet und meine Neugier
geweckt. Also habe ich dies einmal ausprobiert und siehe da, auch in
Scherbenwelten konnte ich mich ohne Widerstand einloggen und meine AP
auslesen. Ich muss sagen, ich war schockiert wie einfach es doch
moeglich ist. Schlimmer noch. In Spielen wie Insulae und Scherbenwelten
findet die Steuerung ueber Links und Formulare statt. Und genau dies,
das bestuecken von Formularen und Absenden eben dieser wird bereits mit
der Anmeldung erledigt. Konkret sind ein nur ein paar Befehle relevant
um Daten aus einem Spiel auszulesen und dann zu verwerten.  
  

~~~~ python
br.open("http://www.example.de/example.php")
~~~~

<p>
  
Macht nichts anderes wie eine Webseite zu oeffnen bzw. zu laden.
Mechanize verarbeitet es automatisch wenn der Webserver direkt auf eine
andere Seite weiterleitet.  
  

~~~~ python
br.open("http://www.example.de/example.php")
~~~~

<p>
  
Traegt in ein Formular, in diesem Beispiel das erste Formular auf der
Webseite, in die angegebenen Felder FORMFELD1 und FORMFELD2 die Werte
aus usern und passw ein. Und dann wird mittels der Methode submit() das
ganze abgeschickt und das Ergebnis in response2 geladen. Absolut simpel.
Allerdings auch etwas Quick and Dirty, denn sobald sich an der
Reihenfolge der Formulare aendert waere hier ein Anpassung notwendig.
Dafuer kann man allerdings die gelesene Seite parsen und sich dann den
Index des gewuenschten Formulaeres ermitteln. Kann, aber fuer den
einfachen Funktionstest reicht es.  
  

~~~~ python
br.open("http://www.example.de/example.php")
~~~~

<p>
  
Damit laesst sich eine Webseite komplett einlesen. Wihlgemerkt, der
Quellcode einer Webseite. Seite, nicht Site. Welche dies ist, das hat
man vorher mit dem oben bereits gezeigten br.open() angegeben. Das ist
ideal wenn ich dann anschliessend htmlinhalt mittels Regular Expressions
auswerte.  
  

~~~~ python
br.open("http://www.example.de/example.php")
~~~~

<p>
  
Dieser kleine Aufruf kann recht hilfreich sein um zu ermitteln, auf
welcher Seite das Programm sich gerade befindet. Gerade wenn bekannt ist
das es Weiterleitungen gibt kann ich hiermit pruefen ob ich noch auf der
erwarteten Seite bin oder anders reagieren muss.  
  
Alles in allem kein Hexenwert, aber dennoch die Grundelemente um Spiele
wie Insulae oder Scherbenwelten mittels eines Bots zu automatisieren.
Gerade die Behandlung der Formulare ist sehr komfortabel.  
  
Ich habe gestern die Spielleitung von Scherbenwelten darauf hingewiesen
das es eben eine solche Schwäche gibt. Bisher jedoch ohne Antwort. Mal
schauen wann da was kommt.  
  
Unterdessen probierte ich ein wenig in Insulae rum wie ich dort einen
solchen Bot blockieren kann. Erster Ansatz: Captchas. Widerlich und
nervig. Und leider erfolglos. Die simplen Captcas welche einen Text
darstellen der in ein Formular eingegeben werden muss sind mittels des
Pythonpaketes pytessa auszuhebeln. Pytessa nutzt das Programm Tesseract
um eben den Text aus Bildern zu extrahieren. Verwandt mit OCRad. Fuer
die fiesen DInger, die Bilder mit den Kreisen in bei denen in den nicht
geschlossenen Kreis geklikt werden muss, dafuer gibt es cdetect. Habe
dies gestern kennengelernt als jemand einen Manager (Bot) fuer
Pennergame schreiben wollte und dann eben an diese Captchas gelangt ist.
Fazit: Captchas doof. Aergern nach aktuellem Stand der Technik nur die
menschlichen Benutzer und sind fuer Bots bzw. deren Entwickler lediglich
einmaliger Mehraufwand.  
  
Eine intensive Nutzung von Ajax, also JavaScript, scheint soetwas zu
erschweren, aber keine dauerhafte Huerde zu sein. Faellt also auch weg.
Scheint fast nur noch Flash ueber zu bleiben. Und da habe ich mal dezent
meine Vorbehalte gegen.  
  
Keine wirkliche Loesung, aber zeitweise eine Blockade waere die
Formularnamen zu veraendern. Ist aber auch doof. Oder gibt es einen Weg
Forumulardaten benutzerbezogen zu gestalten? Bestimmt, aber das wuerde
erst dann greiffen nachdem sich ein Benutzer bereits angemeldet hat. Die
Erkennung eines solchen Bots laesst sich auch noch elegent erschweren.
Da sich mechanize also Browser ausgibt, kann ich ihm auch mitgeben als
welcher Browser es sich ausgibt.  
  

~~~~ python
br.open("http://www.example.de/example.php")
~~~~

  
Simpel und auf der Seite des Webservers somit nicht mehr zu erkennen.
Schoene Scheisse.  
  
Aber um mal wieder auf ein Thema von vorhin zurueck zu kommen: Alles ist
komplett frei und fuer jeden verfuegbar. Auch die Texterkennung von den
Captchas, direkt per Google zu finden. Ein solches Pythonprogramm
welches die AP in Scherbenwelten ausliest war in 20 Minunten
geschrieben. Wer also wirklich vor hat einen Bot zu schreiben, der
findet die besten Vorraussetzungen in Python, ist bereits alles da und
muss nur genutzt werden.  
Lediglich die Dokumentation von mechanize ist etwas duerftig, aber
Versuch und Fehler, nach ein paar Iterationen hat man sich
durchgehangelt.  
  
Verwendete Software:  
Python 2.5, Stackless  
Mechanize 0.1.10  
  
Das wars. Am laengsten hat es gedauert das ganze zum Laufen zu bringen,
da unter Windows Vista bei mir mechanize nicht sauber seine
Abhaengigkeit, ClientForm, mit installierte. Aber nach einer manuellen
Nachinstallation lief es dann.  
  
Quelle: [Mechanize][], [Scherbenwelten][]

  [Mechanize]: http://wwwsearch.sourceforge.net/mechanize/
  [Scherbenwelten]: http://www.scherbenwelten.de/
