Title: Owncloud - Token expired
Date: 2014-11-28 12:17
Author: Jan H. Krüger
Category: IT
Tags: Owncloud, Session, Token
Slug: Owncloud_Token_expired

Seit ich Owncloud nutze stolpere ich regelmäßig über einen nervigen Fehler welcher mich, natürlich immer wenn ich mobil unterwegs bin, sehr nervt.

    Token expired. Please reload page.


Die Ursache ist an sich sehr einfach. In meiner **PHP.ini** ist hinterlegt so die Sessioncookies auf meinem Server abgelegt werden sollen. Zum Beispiel 


    /Ordner/Unterordner/php/session

Aus mir noch nicht ersichtlichen Gründen fliegen die Berechtigungen regelmäßig weg. Was zur Folge hat das eben keine Sessioncookies dort gespeichert werden können. Woraufhin Owncloud irritierender Weise die obige Meldung auswirft. Völliger Unfug. Wie auch immer. Mit einem passendem chmod auf **/Ordner/Unterordner/php/session** hat sich die Sache geklärt.