Title: Datenaustausch für Insulae (fast) fertig
Date: 2008-04-13 01:10
Author: Jan H. Krüger
Tags: Insulae, Datenaustausch, XML

Nach etwas längerer Zeit habe ich mich mal wieder an Insulae gesetzt. Zuletzt hatte ich dort an einem Satz von Skripten gearbeitet welche es, theoretisch, ermöglichen können Daten zwischen Spielen wie Insulae und Scherbenwelten auszutauschen.
Die letzten Aktionen letztes Jahr waren zwei Perl-Skripte welche eine Insel exportieren und ein anderes welches die in Insulae verwendeten Waren exportiert. Bei beiden Anwendungsfällen liegen die Daten in einer XML-Datei. Für diese XML-Dateien habe ich nun die XSDs, also die Schemadateien erzeugt. So kann ich zum einen meine erzeugen Daten validieren und prüfen, andererseits bin ich nun in der Lage bei Bedarf anderen Entwicklern diese Schemata-Dateien zur Verfügung zu stellen (ok, wird eh nie passieren) woraufhin diese mit ihren Daten Transformationsskripte erstellen können.

Die Tage werde ich mich dran setzten das ganze auch mal für einen kompletten Spieler zu versuchen. Völlig illusorisch, da es keine anderen Spiele wie Scherbenwelten und Insulae dort draussen gibt. Und Insulae ist für mich nur eine technische Spielwiese. Aber das müsste man sich mal überlegen wenn zwischen mehreren solcher Spiele die Daten eines Charakters ausgetauscht werden könnten. Das wäre wirklich mal ein Erlebnis wenn ich mit meinem Charakter von einem Spiel in ein anderes gehen könnte.