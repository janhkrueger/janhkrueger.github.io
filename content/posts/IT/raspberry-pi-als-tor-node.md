Title: Raspberry Pi als Tor Node
Date: 2013-04-02 16:19
Author: Jan H. Krüger
Category: IT
Tags: Anonymous, Linux, Raspberry Pi
Slug: raspberry-pi-als-tor-node

Seit längerem betreibe ich auf meinem Macbook bereits ein [Tor-Relay][].
Allerdings gehöre ich zu der Spezies welche den Rechner regelmäßig
ausschaltet, erst recht wenn ich das Haus verlasse. Der Tor-Node lief
daher immer nur abends und manchmal auch Nachts wenn ich zu Hause war.
Ein solcher On-/Off-Node ist für das Tornetzwerk natürlich nicht
optimal. Meine eigentlichen Arbeitsmaschinen wollte ich allerdings nicht
für einen 24/7-Betrieb zweckentfremden. Also habe ich, nicht aktiv nur
immer wieder mal, nach Alternativen umgesehen. Da bei uns auf der Arbeit
das Thema [Raspberry Pi][] hoch kam dachte ich mir ich könnte ja mal
einen Blick drauf werfen. Gesagt getan.

Zur Einrichtung habe ich als System ein Macbook Air mit MacOSX 10.8.3
genutzt. Aufgrund des Unix-Unterbaus waren die Schritte zur Einrichtung
unkompliziert und mit Hausmitteln zu erledigen.

### Hardware

Natürlich ein relevanter Punkt gerade da der Raspberry ja immer als
günstige Alternative für zum Beispiel MediaCenter genannt wird.

> Raspberry Pi (ca. 45 €)  
>  Stromadapter (ca. 7,5 €)  
>  Netzwerkkabel (ca. 13 €)  
>  SDHC Karte (8GB, ca 8€)  
>  Gehäuse (ca. 9 €)

Macht also insgesamt knapp 80 €. Geht billiger, gerade beim Netzteil.
Doch für das erste Gerät bin ich zufrieden. Und die Lieferzeit von einem
Tag bei Amazon war es mir wert :)

Eine separate Maus und Tastatur ist nicht erforderlich, das Raspberry
wird lediglich per SSH angesprochen.

### Image besorgen

Da der Raspberry ohne Betriebssystem nicht läuft muss eines organisiert
werden. Genutzt habe ich dafür die auf Debian basierende Distribution
“[Raspbian][]” Nach dem Download die Prüfsumme überprüfen und los geht
es. Für meine Zwecke habe ich mich an das aktuelle Image vom 09.02.2013
gehalten.

#### Entpacken

<div>
> <span>unzip \~/2013-02-09-wheezy-raspbian.zip</span>

<div>
#### Auf die SD-Karte schieben

> <span>sudo dd bs=4M if=\~/2013-02-09-wheezy-raspbian.img
> of=/dev/**sdd\***</span>

Bei diesem Schritt ist Vorsicht angesagt. Wer hier das falsche Gerät
erwischt kann sich problemlos die Datei eines anderen Datenträgers
vernichten. Die Zahl welche beim **\*** eingetragen werden muss ist
daher genau zu kontrollieren.

</div>
<div>
Dieser Schritt kann gerne einmal mehrere Minunten dauern. dd gibt
darüber hinaus auch keine Zwischeninfos heraus sondern meldet sich erst
wieder wenn der gesamte Vorgang abgeschlossen ist.

</p>
Im Grunde steht damit das Basissystem. Das Image wurde für DHCP
vorbereitet was bedeutet das je nach eigener Netzwerkinfrastruktur keine
weiteren Schritte mehr notwendig sind. Ich schiebe also die SD-Karte nun
in den Raspberry, schließe das Netzwerkkabel an und gebe Saft auf die
Buchse. Die Kontrolllampen blinken und nichts explodiert. Der erste
Schritt ist damit erledigt.

In der Rückbetrachtung war dieser Schritt auch jener welche die meiste
Zeit verbrauchte. Ich denke mit einer schnelleren SD-Karte, Class 10
anstatt meiner Class 4 zum Beispiel, lässt sich da noch ordentlich was
rausholen.

</div>
<div>
</div>
### Router konfigurieren

<div>
In meinem Router muss ich jedoch noch ein paar Einstellungen vornehmen.
Zum einen sage ich dem Gerät das mein neuer Raspberry immer die selbe
IP-Adresse bekommen soll. Zum anderen schalte ich die beiden von Tor
verwendeten Ports frei. Dies sind in der Regel 9001 und 9030. Bei diesen
Einstellungen habe ich es auch belassen. Als drittes erlaube ich dem
Raspberry allgemein sich in meinem Netzwerk zu bewegen und mit dem
Internet Kontakt aufzubauen. In der Regel wird dies bei mir unbekannten
Geräten verweigert. Da die Konfiguration im Einzelnen von Router zu
Router unterschiedlich ist spare ich mir hier eine Anleitung.

</div>
<div>
### Erste Kontaktaufnahme

</div>
<div>
Raspberry-Image geladen, Router entsprechend eingestellt, nun kann der
erste Kontakt hergestellt werden. Terminal gestartet und mittels SSH der
Raspberry angesprochen

</p>
> <span>ssh pi@192.168.0.01</span>

</div>
</div>
Die IP-Adresse ist hier nur als Beispiel anzusehen und spiegelt nicht
mein Netzwerk wieder. "**pi**" ist der Standardbenutzer mit welchem das
Raspbianimage ausgeliefert wird. Das Standardpasswort dieses Benutzers
lautet "**raspberry**". Auf y und z beim Tastaturlayout achten ;)

> **Ab hier erfolgen alle weiteren Schritte lediglich per
> SSH-Terminal.**

#### Passwort neu setzen

Als erstes wird das Passwort neu gesetzt. Das alte **passwd** hilft hier
weiter. Nun kann ich die folgenden Schritte in "Ruhe" angehen.

#### Neuen Rootbenutzer anlegen

Jede Person welche die Information besitzt das ein Raspbian zur
Einrichtung genutzt wurde kennt auch den Standardbenutzer und dessen
Passwort. Also lege ich mit den üblichen Werkzeugen einen neuen
Benutzer. Die konkrete Durchführung erspare ich mir daher an dieser
Stelle.

#### Partitionierung anpassen

Das vorher auf die SD-Karte geschobene Image ist natürlich kleiner wie
der maximal auf der Karte verfügbare Platz. Um diesen auch nutzen zu
können muss die Partition der Karte erweitert werden. Dazu dient das
übliche Tool **parted**.

### System aktualisieren

Das Image war ja nun "ein paar" Tage alt. Also sorge ich erst einmal für
eine Aktualisierung:

> <span>sudo apt-get update</span><span>sudo apt-get upgrade</span>

<div>
Fertig, System aktualisiert. Da mein Raspbian selbstverständlich auch in
Zukunft noch aktuell sein soll setze ich direkt mehrere Cronjobs hierzu
auf.

</div>
<div>
</div>
> <span>\# Das System aktuell und sauber halten</span>  
>  <span>0 1 \* \* 1 apt-get update -y</span>  
>  <span>0 3 \* \* 1 apt-get upgrade -y</span>  
>  <span>0 5 \* \* 1 apt-get clean -y</span>  
>  <span>0 7 \* \* 1 apt-get remove -y</span>  
>  <span>0 2 1 \* \* apt-get dist-upgrade -y </span>

<div>
<div>
Thema erledigt. System wird nun an jedem Montag aktualisiert.

</p>
<div>
### Locate

</div>
<div>
Reine Bequemlichkeit und an sich kein Thema um den Server abzusichern.
Der Befehl **locate** damit ich schnell Dateien im gesamten System
auffinden kann.

</div>
<div>
> <span>sudo apt-get install locate</span>

Fertig.

</div>
### Tor installieren

Nun die eigentliche Anwendung, Tor.

> <span>sudo apt-get install tor</span>

Da ich ab und an dann dochmal einen Blick auf den Server werfen möchte
um mir den Status des Tor-Relays anzusehen wird auch gleich noch das
Tool ARM installiert

> <span>sudo apt-get install tor-arm</span>

Tor ist nun theoretisch einsatzbereit. Doch auch hier sind noch ein paar
Anpassungen an der Konfiguration unter **/etc/tor/torrc** erforderlich.
Also ein schnelles

> <span>sudo nano /etc/tor/torrc</span>

und los geht es.

</div>
<div>
</div>
#### Tor konfigurieren

<div>
Interessant sind hier für mich nur eine handvoll von Einstellungen:

</div>
<div>
> <span>Nickname AliasName</span>  
>  <span>RelayBandwidthRate 100 KB</span>  
>  <span>RelayBandwidthBurst 200 KB</span>  
>  <span>ContactInfo your@email.com</span>  
>  <span>ExitPolicy reject \*:\*</span>

<div>
Diese Einstellungen bedeuten im Einzelnen:

</div>
<div>
Der **Nickname** beschreibt den Namen des Nodes und dient lediglich zur
einfacheren Identifikation. Tatsächlich nebensächlich da jeder Node
einen eigenen Fingerprint besitzt. Mit **RelayBandwidthRate** und
**RelayBandwithBurst** sage ich Tor im Grunde wieviel meiner Bandbreite
zur Verfügung steht. Die vorgegebenen 100 KB sind mit 8 zu
multiplizieren. Konkret bedeutet die Angabe also das ich 800 kb/s
erlaube. Schaft meine Leitung locker und ich nutze sie sowieso nie aus.
"Burst" ist für die temporären Spitzen gedacht wenn Tor gerade ein hohes
Volumen schaufelt. So kann ggf. noch eine Verbindung bearbeitet werden
bevor runter geregelt wird ohne direkt eine Verbindung abzulehnen.
**ContactInfo** dient dazu damit mit mir bei Bedarf Kontakt aufgenommen
werden kann. Ich empfehle hierfür eine eigene Adresse anzulegen. Denn
diese Adresse ist durch diverse Übersichtsseiten auch von Google lesbar.
Und zuletzt noch die wichtige **ExitPolicy**. Diese regelt wir mein Node
genutzt werden kann. Das von mit vergebene "reject \*:\*" bedeutet im
Klartext das mein Noden nur als Relay arbeitet und kein Ausgang für das
Tor-Netzwerk ist.

</p>
Torserver neu starten und alles läuft wie geplant:

> <span>sudo /etc/init.d/tor restart</span>

</div>
</div>
</div>
Meine vollständige Konfigurationsdatei ist unter ~~Pastebin.com~~ meiner
Stikked-Instanz abgelegt:

<iframe style="border: none; width: 100%;" src="https://janhkrueger.de/stikked/view/embed/3a07a81d" height="240" width="320"></iframe>

<div>
Nun kann ich bereits einen ersten Blick auf meinen Node werfen. Dazu
wird nun das vorhin installiert Tool Tor-Arm aufgerufen:

</p>
> <span>sudo -u debian-tor arm</span>

</div>
### <span> Das wird nun mit ein paar bunten Bildern quittiert.</span>

<div>
[![Tor-Status-Graph][]][]

</div>
<div>
</div>
<div>
[![Tor-Node-Connections][]][]

</div>
<div>
<span> </span>

</div>
Nachdem nun der Tornode steht kann ich mich um den Rest des Servers
kümmern.

#### Nodestatus per Email

Selbstverständlich kann ich nicht rund um die Uhr auf den Server blicken
um den Status zu überprüfen. Hier springt eine externe Webseite namens
[Tor Weather][] ein. Sobald mein Node einmal nicht erreichbar ist werde
ich fortan per Email informiert. Das sieht dann beispielhaft so aus:

<div>
[![Tor-Weather-Statusmail][]][]

</div>
#### Nodestatus per Webseite

Was per Email geht ist natürlich auch auf Webseiten möglich. Eine,
welche mir aufgrund ihrer Einfachheit zusagt,
ist [http://torstatus.blutmagie.de/][]. Der Vorteil ist das ich anhand
des Fingerprints meines Nodes diesen auch unter einer [festen Adresse][]
ansprechen kann.  
Doch dazu eine Warnung. Es gibt Webfilter welche die Seite blockieren.
Der häufigste Grund welchen ich sehen konnte ist "**Proxy Avoidance**".
Also Sperrung wegen vermeintlicher Umgehung eines Proxys. Trifft zwar
nicht zu doch ich vermute das hier generell Tor geflaggt ist.

### 

### Logdateien entsorgen

Warum mögen sicherlich nun einige Fragen sollte man denn Logs klein
halten und löschen? Nun, aus zwei einfachen Gründen. Zum einen ist der
Platz auf der von mir verwendeten SD-Karte begrenzt. Zum anderen kann
ich, wenn das Tor-Log gar nicht erst da ist auch keine Infos dazu
herausgeben.

Also wird ein neuer Cronjob angelegt:

> <span>\# Tor Log klein halten</span><span> 0/10 \* \* \* \* truncate
> -s 9 /var/log/tor/log</span>

Dies sorgt dafür das alle 10 Minuten das Log auf die letzten 9 Einträge
gekürzt wird. Zu überlegen ist hier noch ob ich das Log direkt nach
/dev/null umleiten kann. Das wird jedoch zu einem späteren Zeitpunkt
noch geprüft.

Daneben gibt es noch ein paar andere Logs welche ich nicht gerne
entsorgt sehen möchte. Also werden auch diese alle 10 Minuten komplett
geleert.

> <span>\# Sonstige Logs des Systemes leeren  
>  1/10 \* \* \* \* \* truncate -s 0 /var/log/user.log</span>

### Prüfung auf Rootkits

Bei einem System welches quasi rund um die Uhr mit dem Internet
verbunden ist sehe ich es als notwendig an die Sicherheit weiter
aufzudrehen. Ein Schritt dazu ist überprüfen zu können ob ein Angreifer
es ggf. geschafft hat ein Rootkit zu installieren. Also wird wieder apt
bemüht:

<div>
#### Programm chkrootkit installieren

> <span>sudo apt-get install chkrootkit</span>

<div>
Selbstverständlich soll das ganze täglich laufen. Dies kann zum einen in
der Datei **/etc/chkrootkit.conf** eingestellt werden. Dazu muss der
Parameter RUN\_DAILY wie folgt gesetzt werden:

</p>
> <span>RUN\_DAILY="true"</span>

</div>
</div>
<div>
Das ganze kann natürlich auch mittels Cronjob gelöst werden. Und da ich
nicht jeden Tag auf dem Raspberry einloggen will lasse ich mir die
Protokolle hiervon direkt zusenden:

</div>
<div>
> <span>0 3 \* \* \* root (cd /usr/sbin; ./chkrootkit 2\>&1 | mail -s
> "chkrootkit output" your@email.com)</span>

<div>
</div>
<div>
Da ich allerdings ungern nur einem Programm vertraue wird gleich noch
ein zweites zur Suche nach Rootkits genutzt. Die Wahl viel dann auf
**RKHunter**.

</p>
#### Programm RKHunter installieren und aktualisieren

</div>
> <span>sudo apt-get install rkhunter  
>  </span><span>sudo rkhunter --update</span>

Ein erster Scan kann nie schaden, daher:

> <span>sudo rkkunter -c --sk</span>

RKHunter gab mir bei der
Datei **/usr/lib/arm-linux-gnueabihf/libcofi\_rpi.so** eine Warning.
Schnell recherchier kam ich zu dem Schluss das diese Datei nicht für
meine Zwecke benötigt wird. Also weg damit:

> <span>apt-get remove raspi-copies-and-fills</span>

Da rkhunter aus den Paketquellen installiert wurde gibt es sofort einen
Eintrag unter **/etc/cron.daily/** Täglich wird nun also auch mittels
RKHunter überprüft ob das System kompromittiert wurde.

Anschließend wird noch eingestellt das nette Mails versandt werden
**/etc/rkhunter.conf** nach der Einstellung “MAIL\_ON\_WARNING”.
Anpassung simpel, einfach die eigene Mailadresse eintragen.

> <span>MAIL-ON-WARNING="your@email.com"</span>

RKHunter sollte nach der Installation noch antrainiert werden damit es
nicht zu Falschmeldungen kommt. Dies ist jedoch ein eigenes Thema für
sich. Ich verweise daher an dieser Stelle auf die Seite

### Mitteilung wenn ein Root Login erfolgt

Ein einfacher Weg festzustellen wenn ein Login durch den Adminbenutzer
erfolgt ist in diesem Moment eine Email zu verwenden.  
Also schreibe ich in die Datei **\~.bash\_profile** folgende Zeile:

</div>
<div>
> <span>echo 'ALERT - Root Shell Access on:' \`date\` \`who\` | mail -s
> "Alert: Root Access from \`who | awk '{print \$6}'\`"
> your@email.com</span>

Erledigt. Und schon erhalte ich bei einem Log-In eine Benachrichtigung.
Da ich davon aus gehe das ich noch soweit fit im Kopf bin das ich
zuordnen kann ob ein Login von mir erfolgt oder nicht sollte ich eine
gute Info darüber erhalten ob sich jemand unbefugt Zugang zum Raspberry
verschafft.

### SSH-Logins absichern

</div>
<div>
Auch dieser Punkt ist schnell abgehakt durch eine Anpassung in der Datei
**/etc/ssh/sshd\_config** Hier passen wir die folgende Zeile wie folgt
an:

</p>
> <span>\#PermitRootLogin yes</span>

</div>
auf

> <span>\#PermitRootLogin no</span>

<div>
Erledigt.

</p>
### 

### Brute Force Detection Installation

</div>
<div>
Manchmal kann natürlich auch die Situation auftreten das rohe Gewalt
verwendet wird um Zugang zu erlangen. Auch hierfür gibt es Wege dieses
zu entdecken. **[Brute Force Detection][]** nennt sich das Tool. Dieses
habe ich nicht im Repository gefunden daher erfolgt die Installation
"manuell".

</p>
> <span>cd <span>\~</span></span>  
>  <span>wget
> http://www.rfxnetworks.com/downloads/bfd-current.tar.gz</span>  
>  <span>tar -xvzf bfd-current.tar.gz</span>  
>  <span>cd bfd-1.5</span>  
>  <span>./install.sh</span>

</div>
Auch hier ist die Konfiguration entscheidend welche
unter <span>**/usr/local/bfd/conf.bfd** abgelegt ist. Auch hier
empfiehlt es sich eine Mailbenachrichtigung zu aktivieren.</span>  
<span>  
</span><span>Also wie gehabt die sudo nano-Kombination</span>

> <span><span>sudo nano /usr/local/bfd/conf.bfd</span></span>

und folgende Einstellungen anpassen:

> <span>\# send email alerts for all events [0 = off; 1 = on]</span>

> <span>EMAIL\_ALERTS="1"</span>

> <span>  
>  </span><span>\# local user or email address alerts are sent to
> (separate multiple with comma)</span>

> <span>EMAIL\_ADDRESS="your@email.com"</span>

<span>  
</span><span>Während der Installation wird auch gleich ein Cronjob
unter </span><span>**/etc/cron.d/bfd** </span><span>angelegt welcher
alle drei Minuten aktiviert wird. Ein weiterer Eintrag in der
Crontabelle ist daher nicht mehr notwendig.</span>

### Emailversand ermöglichen

Jetzt habe ich bei so vielen Schritten angegeben das ich eine
Benachrichtigung per Email erhalten möchte und mein System ist noch gar
nicht dafür vorbereitet. Also ran:

<div>
Notwendige Pakete installieren

</p>
> <span>sudo apt-get install exim4-daemon-light mailutils</span>

</div>
Danach zur Konfiguration:

> <span>dpkg-reconfigure exim4-config</span>

<div>
Und fertig.

</div>
<div>
</div>
Hierzu habe ich auf die Anleitung unter [linode.com][] zurück gegriffen.

### Nachwort zum Thema Sicherheit

Mir ist klar das ich hier sicherlich noch kein bombensicheres System
geschaffen habe. Das kann es wie ich denke auch nie geben.

Ein weiterer großer Nachteil ist natürlich der Raspberry an sich. Sollte
sich jemand Zugang zum Raspberrystandort verschaffen ist die SD-Karte
und damit das System nicht mehr sicher. Vielleicht kann ich zu einem
späteren Zeitpunkt einmal darüber nachdenken das Dateisystem auf der
SD-Karte zu verschlüsseln. Das ist jedoch für meinen Anwendungsfall
paranoide Zukunftsmusik. Zumal ich wohl auch ernstere Sorgen haben werde
wenn sich jemand sogar Zugang zu meinen Räumlichkeiten verschaffen
sollte. Da ist dann der Raspberry wohl auf einer niedrigeren Priorität.

Weiterhin habe ich bei sehr vielen Komponenten eine
Emailbenachrichtigung aktiviert. Hier wird die Zeit zeigen ob das
derzeitige Level in Ordnung ist oder das Mailaufkommen zu viel wird.
Wenn dem so ist kann ich immer noch die Konfigurationen anpassen.

### Offene Punkte

<div>
</div>
#### Software ausmisten

In der regulären Installation von Raspbian ist auch sehr viel enthalten
was ich zum Betrieb des Tornodes nicht benötige. Hier werde ich in der
nächsten Zeit noch die Liste filzen um nicht benötigte Komponenten zu
entfernen. Insbesondere der Blick auf die derzeit noch vorhandenen
Entwicklungssprachen und-werkzeuge wird wichtig sein. Wenn das System
einmal eingerichtet ist werde ich hier kräfitig entsorgen können.

#### Tor-Logs weiter einschränken

Offen ist ebenfalls ob ich die Logdateien von Tor direkt
nach**/dev/null** umleiten kann. So könnte der Node keine Infos
verraten. Doch hier muss ich erst prüfen ob es möglich ist und was als
"best practise" empfohlen wird. Doch eines nach dem anderen.

#### Nodestatus sichern

Regelmäßig die [Infoseite][festen Adresse] des Nodes sichern und als PDF
ablegen. Dient für mich rein zu Infozwecken.

#### Abgehende Emails signieren

Interessant, und auch eher eine Spielerei, ist die Frage ob ich die
Emails automatisch mittels GPG signieren kann. Geht sicherlich. Wird
dann eines der langfristigen Projekte.

#### Image sichern

Wenn ich irgendwann einmal der Meinung bin nun einen vernünftigen Stand
erreicht zu haben werde ich die SD-Karte als neues Image sichern. Das
wird mir die Einrichtungsarbeit bei zukünftigen Raspberrys, insbesondere
bei jenen welche dauerhaft mit dem Internet verbunden sind, erleichtern.
Und eine Sicherung kann nie schaden.

### Ausblick

Wenn die bisherigen positiven Erfahren auch nach vier Wochen immer noch
andauern werde ich mir noch mindestens einen weiteren Raspberry Pi
zulegen. So ein eigenen [yacy][]-Node reizt mich ja schon.

<div>
</div>

  [Tor-Relay]: https://www.torproject.org/
  [Raspberry Pi]: http://www.raspberrypi.org/
  [Raspbian]: http://www.raspbian.org/
  [Tor-Status-Graph]: http://www.janhkrueger.de/blog/wp-content/uploads/2013/06/Tor-Status-Graph-150x150.jpg
  [![Tor-Status-Graph][]]: http://www.janhkrueger.de/blog/wp-content/uploads/2013/06/Tor-Status-Graph.jpg
  [Tor-Node-Connections]: http://www.janhkrueger.de/blog/wp-content/uploads/2013/06/Tor-Node-Connections-150x150.jpg
  [![Tor-Node-Connections][]]: http://www.janhkrueger.de/blog/wp-content/uploads/2013/06/Tor-Node-Connections.jpg
  [Tor Weather]: https://weather.torproject.org/
  [Tor-Weather-Statusmail]: http://www.janhkrueger.de/blog/wp-content/uploads/2013/06/Tor-Weather-Statusmail-300x67.jpg
  [![Tor-Weather-Statusmail][]]: http://www.janhkrueger.de/blog/wp-content/uploads/2013/06/Tor-Weather-Statusmail.jpg
  [http://torstatus.blutmagie.de/]: http://torstatus.blutmagie.de/
  [festen Adresse]: http://torstatus.blutmagie.de/router_detail.php?FP=cf0a98de988abad55a166a5b7828efe2fa6226cd
  [Brute Force Detection]: http://www.rfxn.com/projects/brute-force-detection/
  [linode.com]: http://library.linode.com/email/exim/send-only-mta-debian-6-squeeze
  [yacy]: http://yacy.net/de/index.html
