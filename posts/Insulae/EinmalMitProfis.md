Title: Einmal mit Profis...
Date: 2015-02-02 00:38
Author: Jan H. Krüger
Tags: Insulae, C++, Entwicklung, Fehlerbehandlung

Kennt ihr das wenn euch nach mehreren Tagen etwas wie Schuppen von den Augen fällt? Genau das ist mir eben passiert.

Der Grund ist auch <s>"eigentlich"</s> einfach. Absolut meine eigene Schuld, kommt davon wenn ich spät in der Nacht noch anfange zu programmieren.
Aktuell bin ich ja dabei meine Hintergrundskripte von Insulae auf C++ umzustellen. Derzeit ist der Teil dran welcher sich um die Stadtauswertung kümmert. Und seit mehreren Tagen hatte ich jetzt das Problem das der bisher umgesetzte Teil ein wichtiges Update auf der Datenbank nicht festschreibt. Konkret: nach Berechnung der benötigten Waren um die Stadtbevölkerung zu ernäheren wurde in der Datenbank der Warenvorrat der betreffenden Stadt nicht wie vorgesehen reduziert. Etwas ratlos saß ich vor dem Bildschirm.

* Query wurde erfolgreich ausgeführt, ReturnCode sah super aus
* keine geworfene Ausnahme weit und breit
* Programm lief augenscheinlich auch erfolgreich durch.

Also hin und her überlegt. Geprüft ob ich explizit nach dem Query ein Commit absetzen kann. Ging nicht, die Verarbeitung läuft ja in einer Transaktion. Ein Commit und die Transaktion wird beendet und die weiteren Tätigkeiten werden nicht mehr ausgeführt. Verschachtelte Transaktionen? Technisch möglich. Jedoch nicht zwingend das was ich eigentlich will.
Heute vormittag, bevor ein Parteitermin startete, habe ich dann das Queryprotokoll von PostGres aktiviert mit folgendem Ergebnis:

<iframe src="https://janhkrueger.de/stikked/view/embed/82bb9d6a" style="border:none;width:100%"></iframe>

Vordergründig sah es in Ordnung aus.

Dann fiel mir die folgende Zeile auf:
    
    LOG:  unexpected EOF on client connection with an open transaction

Moment, warum ein EOF? Das Programm ist doch angeblich korrekt beendet? Eben, um Mitternacht, ist es mir dann gekommen. Die Phase __1000000000__, also auch jene welche ich bewußt verarbeiten wollte, wurde sogar korrekt abgearbeitet. Im Programm wurde dann versucht zur nächsten Phase, der __1000000001__ zu wechseln. Ja Moment! Dort sind aktuell ja gar keine Städte angesiedelt?

Um das ganze abzukürzen, ich habe zwei Punkte nicht beachtet welche ich sonst sogar unseren Auszubildenden mit auf den Weg gebe.

* Die Verarbeitungen der Städte einer Phase muss nur dann erfolgen wenn in der Abfrage der zu dieser Phase gehörenden Städte auch mindestens eine Stadt gefunden wurde.
* Korrekte Ausnahmenbehandlung ist Gold wert!

Es wurde die erste Phase erfolgreich und richtig abgearbeitet. Bei der zweiten ist ein Fehler aufgetreten, das Programm hat nicht weiter gearbeitet und sich beendet. Gleichzeitig wurde der Abbruch nicht erfolgreich gefangen und somit auch nicht vernünftig behandelt. Dadurch wurde der Commit am Ende meiner Transaktion auch nicht ausgefürhrt. Ergo: keine Aktualisierungen auf der Datenbank. Ganz oder gar nicht halt. So wie es bei dieser kritischen Verarbeitung auch sein soll.

Beim ersten Punkte hat mir ein __if ( RStaedte.size() > 0)__ geholfen hier nicht notwendige Bearbeitungen zu überspringen. Die Bearbeitungen erfolgen nun so wie ich mir das vorgestellt habe. Das zweite, die nicht korrekte Behandlung der Ausnahme, ist noch nicht gelöst. Aktuell blicke ich auf den betreffenden Abschnitt und bin immer noch der Meinung das er in einem try und catch-Block eingewickelt ist und auch die möglichen Ausnahmen definiert sind. Ganz offen warum auch der ReturnCode nicht auf einen Fehler hinwies. Wie auch immer, nicht mehr heute.

Memo an mich: _"Mach es richtig, dann funktioniert es auch!"_

Erspart mehrere Abende überflüssiger Fehlersuche.