Title: Kaspersky Installation mit Huerden
Date: 2008-03-09 13:18
Author: Jan H. Krüger
Category: IT
Slug: kaspersky-installation-mit-huerden

**Prinzipiell bin ich der Meinung das die Produkte von Kaspersky
durchaus zu gebrauchen sind. Gestern wurde ich jedoch davon ueberzeugt
das, tritt dabei einmal ein Fehler auf, dies fuer Nicht Technikversierte
Benutzer eine massive Huerde sein kann.**  
  
Was ist passiert? Nun, meine Schwester hat fuer sich und meinen Schwager
die Kaspersky Internet Security Suite gekauft. An sich kein Problem.
Allerdings hatten sie von frueher noch Alt-Lasten, sprich: alte
Versionen installiert. Trotz einer Deinstallation blieben Rueckstaende
in der Registry was dazu fuehrte das das neue Produkt der Meinung war
stets den Rechner erst neu zu starten anstatt die Installation
durchzufuehren. Viel rumprobiert, die Registrz gesaeuber, doch das
Verhalten blieb.  
  
Fuendig wurde ich dann auf einer Webseite welche genau dieses Beschrieb.
Ursache war schlicht ein nicht ordnungsgemaess entfernter Eintrag in der
Registry. DIeser muss manuell entfernt werden, danach kann KIS wie
gewollt installiert werden.  
  
Schluessel:  
  
Nach **HKEY\_LOCAL\_MACHINE \\ SOFTWARE \\ Microsoft \\ Windows \  
CurrentVersion \\ Run** navigieren. Dort gibt es einen Ordner namens
**avp6\_post\_uninstall**. Wenn dieser geloescht wird, steht der
Installation nichts mehr im Wege.  
  
[Raymonds Webseite][]

  [Raymonds Webseite]: http://www.raymond.cc/blog/archives/2007/10/15/kaspersky-installation-ended-prematurely-because-of-an-error/de/
