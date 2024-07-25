Title: Unsinnige Fehlerklassen
Date: 2008-06-16 13:16
Author: Jan H. Krüger
Category: Allgemein
Slug: unsinnige-fehlerklassen

**Da kaempft man monatelang im Unternehmen damit auch fuer die C++ und
Java-Welt einheitliche, zeitgemaessige Klassen eingefuehrt werden mit
denen die Entwickler arbeiten koennen und sollen, und dann stellt sich
bei der Benutzung raus das sie effektiv unnuetz sind. Klinge ich
genervt? Ja.**  
  
Warum werden eigentlich solch wichtige Dinge nur peripher mit jenen
Besprochen welche auch direkt beteiligt sind? Mir ein raetsel. Worueber
aergere ich mich gerade? Ueber unsere einheitlichen Klassen welche unter
anderem dafuer sorgen sollen im Fehlerfall ein Protokoll zu erstellen.
Nun, ein Protokoll wird erstellt, ohne Zweifel. Konkret tritt der untere
Fehler auf sobald im Batchprogramm eine Verbindung zur Datenbank
aufgebaut werden soll. Tuts nicht. Warum nicht wird auch angegeben und
ist von mir schon behoben worden, war ein Tippfehler im Benutzernamen.
Was ein Glueck weiss ich in der Regel was in meinen Programmen vor sich
geht, denn ein Kollege haette mit der folgenden Meldung seinen Spass
gehabt.  
  
2008-06-16:10:53:20:000707 Error
Meldungszeit:TIMESTAMP('2008-06-16-11.54.21.707000') /
`Meldungskategorie:T / Meldungstyp:11 / Objekt-Id:DBConnector::getDbVerbindung(string dbName, string userName, string passWort) / Einzel-RC:11 / Meldung:[IBM][CLI Driver] SQL30082N  Attempt to establish connection failed with security reason "15" ("PROCESSING FAILURE").  SQLSTATE=08001`  
  
Zur Erlaeuterung: Mein Programm oeffnet Verbindungen nicht nur zu einer
Datenbank, sondern dreie an der Zahl. Da in der obigen Meldung ja
effizienterweise nicht angegeben wird in welcher Zeile der Fehler
auftrat oder zu welcher Datenbank nun der Connect durchgefuehrt wurde
beginnt das Raten. \*grmpf\* Was fuer eine Ueberraschung wenn diejenigen
welche diese Basisklassen erstellen nicht jene sind welche die Klassen
nutzen oder eben die Protokolle welche davon erstellt werden durchlesen
im produktiven Betrieb.
