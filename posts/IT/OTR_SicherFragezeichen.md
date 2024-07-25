Title: Warum soll OTR sicher sein?
Date: 2015-01-05 01:48
Author: Jan H. Krüger
Tags: OTR, NSA, Off-the-Record, Private, Chat,

Etwas das mich die letzten Tage in den Berichterstattungen schon gewurmt ist die Behauptung das [OTR][1] sicher sei. Anhand der mir bekannten Informationen ist diese Behauptung in keinster Weise haltbar.

Schauen wir mal an was wir haben. Wir haben ein Datenpaket welches eine Datei enthält, die [media-35552.pdf][4]

<!--more-->

In dieser findet sich eine arg seltsam formatierte Ansicht einer vermeintlichen Kommunikation eines Zieles und eines anderen Kommunikationspartners. Die Kommunikation fand laut dem Dokument am 16. März 2012 zwischen 13:35 Uhr und 13:39 Uhr (GMT) statt. Eine weitere vin 13:40 bis 13:44 Uhr. Soweit so gut.
Dazu finden sich, geschwärzt, nicht lesbare Kommunikationsinhalte. Weiterhin die dort angehängte Information 

```[OC: No decrypt available for this OTR encrypted message.]```

Dies **kann** bedeuten das OTR zum damaligen Zeitpunkt nicht entschlüsselt werden konnte. Es kann jedoch auch bedeuten das zum Zeitpunkt als der Bericht(?) angefertigt wurde diese spezifische Nachricht nicht entschlüsselt werden konnte. Oder der Klartext noch nicht vorlag. Vielleicht lief ein entsprechender Job noch nicht.

Kern ist jedoch: dieser eine Satz alleine gibt inhaltlich keine Gewissheit das jenes Verfahren an sich sicher noch nicht geknackt wurde.

Der [Spiegel][2] schreibt dazu:
> "Größere" Probleme hat die NSA auch mit Truecrypt, einem Programm zur Verschlüsselung von Dateien auf Computern, und mit dem sogenannten Off-the-record-Protokoll (OTR) zur Codierung von Chats. 

Das ist, wenn man diese Folie liest, daraus nicht zu lesen. Wir wissen lediglich das im März 2012 die Inhalte einer Kommunikation nicht entschlüsselt waren. Wir können daraus nicht lesen das es allgemein für das Verfahren gilt. Zugegeben, ein paar Sätze weiter wird dies dann auch wie ich finde korrekter dargestellt:

> „Zumindest manchmal scheitert die NSA also an OTR.“

Die [Zeit][3] schreibt dies auch etwas undeutlicher:

> „Die Verfahren PGP zum Schutz von E-Mails sowie die "Off-the-record"-Verschlüsselung von Chats (OTR) sind nach Ansicht von Experten diesbezüglich sicher.“

Laut der Zeit hat Jacob Applebaum am 31C3 angeblich gesagt das diese Verfahren (PGP und OTR) sicher seinen. Ich kann nicht wirklich glauben das er dies gesagt haben soll. Auch @ioerror müsste bewusst sein das dies nicht in der Folie zu sehen ist.

Vielleicht gibt es ja noch weitere Folien in denen das näher erläutert wird. Im letzten Datenpaket jedoch nicht. Umso eher ein Punkt für die Forderung von Cryptome die gesamten Dokumente frei zu geben, nicht nur immer Häppchenweise für die Klickraten (ok, zu  platt ausgedrückt, ganz so einfach ist es ja dann doch nicht).

Quellen:<br>
[Off-the-Record Messaging (Wikipedia)][1]<br>
[Spiegel Online][2]<br>
[Zeit][3]

[1]: http://de.wikipedia.org/wiki/Off-the-Record_Messaging
[2]: http://www.spiegel.de/netzwelt/netzpolitik/snowden-dokument-so-unterminiert-die-nsa-die-sicherheit-des-internets-a-1010588.html
[3]: http://www.zeit.de/news/2014-12/29/internet-woran-die-nsa-spione-scheitern-29143405
[4]: https://janhkrueger.de/gitpup/nsa-spiegel-14-1228.git/blob/master/media-35552.pdf

