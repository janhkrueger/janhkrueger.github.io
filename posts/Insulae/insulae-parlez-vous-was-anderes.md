Title: Insulae - Parlez-vous ... was anderes?
Date: 2009-07-14 22:45
Author: Jan H. Krüger
Category: Insulae
Slug: insulae-parlez-vous-was-anderes

In den letzten Wochen war es etwas still um Insulae. Das liegt
mitnichten daran das ich nichts getan habe, sondern eher daran das ich
viel mehr Hintergrundarbeiten erledigt habe. Ein großer Teil davon ist
die Lokalisierung.

Konkret bin ich an drei "Meilensteinen" dran:

-   Umstellung von Insulae auf Python mittels Django als Web-Framework
-   Entwicklung eines reinen Admin- und Moderatorenpanels zur
    Spielsteuerung
-   Nutzung der von Django bereitgestellten Mittel um gemäß i18N zu
    arbeiten

<p>

Also doch schon drei große Teile. Im Adminpanel ich ich derzeit am
weitesten, wobei die Entwicklung hierbei Hand in Hand mit dem driten
Punkt geht. Ist auch eine gute Übung bevor ich das ganze mit dem
eigentlichen Spiel vorrantreibe. Die Anpassungen an die Django-Templates
sind hierbei auch sehr einfach zu sehen. Zu Beginn eines Templates muss
Django mitgeteilt werden das für dieses Template eine Übersetzung
versucht werden soll.
<p>


Nun ja, und danach ist eigentlich alles genauso einfach. An jede Stelle
an die ich bisher einen festen String mit einem Wort eingegeben habe,
ersetze ich eine bestimmte Codezeile im Template. Will ich zum Beispiel
das der auf deutsch benannte Link "`Eigene Nachrichten`" je nach
unterstützter Sprache übersetzt wird, teile ich dies dem Template wie
folgt mit


<p>


Das kann ich direkt während der Erstellung eines neuen Templates
angeben. So sehe ich in dieser Phase was ich an dieser Stelle bezwecken
will, ohne weitere Anpassungen.

Schön und gut, aber wie kann ich nun dafür sorgen das die Zeichenkette
"Eigene Nachrichten" für einen englischsprachigen Benutzer eben in
Englisch angezeigt wird? Zu erst muss eine Liste mit den zu
übersetzenden Texten erstellt werden. Dazu ist ein klein wenig Vorarbeit
zu leisten. Im Verzeichnis meines Django-Projelktes, Insulae, habe ich
einen weiteren Ordner mit dem Namen "`locale`" angelegt. Dies muss
manuell getan werden. Die Verzeichnisstruktur sieht dann also wie folgt
aus, nun nachdem ich den Ordner angelegt habe:

![Verzeichnisstruktur Djangp-Projekt][]
Wobei das nur die Struktur auf meinem Ausweichrechner ist.

Nachdem das Verzeichnis angelegt ist, kann Django angewiesen werden alle
Quelldateien zu durchsuchen und alle wie oben gekennzeichneten Strings
auszugeben. Beim Aufruf von django-admin.py sind noch ein paar Parameter
zu beachten. Der wichtigste ist sicherlich makemessages, welcher Django
anweist überhaupt die Liste zu erzeugen. Weiterhin noch die Sprache für
die die Übersetzung angelegt werden soll. Dies geschieht mittels
`-l [Ländercode]`. Dann kann noch optional mittels des Parameters
`-e `angegeben werden, dass nicht nur die üblichen Quelldateien
analysiert werden sollen, sondern eben alle mit den angegebenen
Endungen. Der Parameter `-a` gibt an, das ich eine bereits bestehende
Liste aktualiseren will, und nicht immer wieder eine leere.

<p>


Daraufhin entstehen neue Unterverzeichnisse in locales. Bei mir konkret
habe ich dann `$PROJECTPATH/locale/de/LC_MESSAGES/` Dort liegt nun eine
Datei namens django.po bzw. auch für englisch ein entsprechender
en-Unterordner. Diese .po-Datei ist im Grunde nur eine Textdatei in der
alle Strings welche ich für eine Übersetzung vorgesehen habe enthalten
sind in folgendem Format.
<p>


msgid gibt den zu übersetzenden String an, msgstr den Zielstring. Wird
dieser leer gelassen, wird einfach msgid ausgegeben. So brauche ich
keine doppelten Nennungen vorhalten. In der .po-Datei für die englischen
Seiten trage ich nun die Übersetzung ein.


Nun ist diese Vorlage noch umzusetzen. Dies wird wieder von django-admin
erledigt, bis auf den ersten Parameter sind keine weiteren notwendig. Es
werden grundsätzlich alle Sprachen die wie oben angelegt wurden
verarbeitet.
django-admin.py compilemessages
Dies erzeugt nun in zusätzlich zu den .po-Dateien Dateien mit der Endung
.mo. Nun ja, das wars. Da meine Browser hier persönlich immer deutsch,
also deDE als Locale liefern, ich aber ggf. eine englische Übersetzung
auch testen will, kann dies in der settings.py des Django-Projectes auch
eingestellt werden. Dort trage ich ind er Regel
`LANGUAGE_CODE = 'de-DE'` ein. Will ich jedoch die englischen Texte
lesen, ändere ich dies einfach auf `LANGUAGE_CODE = 'en-EN'`. Fertig.

Das ist nun alles was als Basis notwendig ist. Wenn eine neue Sprache
eingepflegt werden soll, kann einfach eine neue wie oben beschrieben
angelegt werden und einem übersetzungswilligen Spieler / Mitarbeiter
gegeben werden. Wenn diese zurückkommt, einfach mittels compilemessages
bearbeiten und schon steht eine neue Sprache zur Verfügung.

Ok, war jetzt mehr ein Ausflug wie in Django i18N genutzt wird. Macht
aber nichts. Für alle die Fragen, in Insulae tut soch noch was, aber
eben eher im Hintergrund. Einzig eine Sache wird schon partiell genutzt.
Ich habe die Datenbankgrundlagen für ein System mit mehreren Postfächern
gelegt. Jeder Spieler kann prinzipiell mehrere Postkörbe zugewiesen
bekommen. Dies ist erst einmal der persönliche wie er auch aus
Scherbenwelten bekannt ist. Gleichzeitig bekommt auch jede Stadt einen
Postkorb. Zum einen werden so die Nachrichten von Spieler und Stadt
ordentlicher voneinander getrennt, gleichzeitig gehen somit auch die
Nachrichten einer Stadt bei einem Besitzerwechel mit. Ich kann nun
spezielle Admin- bzw. Support-Postkörbe einrichten welche der Support
bzw. ich als Admin lesen und bearbeiten können ohne einen besonderten
LogIn zu nutzen. Weitergehend, ein solcher Postkorb ist nun streng
genommen nicht mehr Spiel-gebunden sondern kann auch über andere Dienste
gefüllt werden.

  [Verzeichnisstruktur Djangp-Projekt]: http://www.janhkrueger.de/blog/wp-content/uploads/2009/07/Verz_Struktur_Insulae_Python.png
    "Verzeichnisstruktur Djangp-Projekt"
