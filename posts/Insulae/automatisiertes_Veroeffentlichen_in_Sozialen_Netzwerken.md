Title: Insulae - automatisiertes Veröffentlichen in Sozialen Netzwerken
Date: 2010-05-30 22:30
Author: Jan H. Krüger
Tags: Insulae, Social Network, Automatisierung, Social, Twitter, Forum, Google

Um alle Interessenten stets schnell und einfach ueber Neuerungen in
Insulae informieren zu können, habe ich ein wenig rumprobiert und nun
die erste Version der Netzwerkanbindung fuer Insulae fertig gestellt.  
Konkret: mittels eines neu erstellten Formulares können Ankündigung
und News bequem zentral erfasst werden. Daraufhin wird die Ankündigung
aktuell an fünf Orte eingestellt:  

* News-Seite in Insulae
* Insulae-Forum
* dieses Blog
* Twitter
* Google Buzz

Als nächsten Schritt werde ich versuchen mich mit der API zu Facebook
auseinander zu setzen um auch hier einen direkten Zugang per Skript zu
erlangen. Infoquellen per RSS-Feeds ergeben sich aus den genannten
Quellen ebenfalls.  
  
Dabei ist die Anbindung an die eigene News-Seite und ins Forum trivial,
da Eigenentwicklungen. Daher werde ich hier auch nicht weiter darauf
eingehen.  
  
Die Twitter-API ist dankenswerterweise simpel wie es nur sein kann.  

    :::python
    #!/usr/bin/python
    import os
    import twitter
    E = sys.exit
    ##############################
    # Send message to Twitter
    ##############################
    try:
    # API initialisieren
        client = twitter.Api()
        # Authentifizieren
        client = twitter.Api(username='twitterusername', password='twitterpassword')
        # Nachricht an Twitter senden
        update = client.PostUpdate(message)
    except:
        print ("Keine Anbindung an Twitter moeglich.")
        E(8)


Schwupps, Text bei Twitter gepostet.  

Für Google Buzz sieht es etwas schwieriger aus. Ich habe noch keine
überzeugende API dafuer gefunden. Doch Google hat die Möglichkeit
geschaffen, auch mittels einer E-Mail an Buzz zu senden. Daher ist die
Hauptaufgabe fuer Buzz eigentlich der Versand einer E-Mail.  

    :::python
    #!/usr/bin/python
    import smtplib from email.MIMEMultipart 
    import MIMEMultipart from email.MIMEBase 
    import MIMEBase from email.MIMEText 
    import MIMEText from email 
    import Encodersimport os, getopt, sys

    # Hier die zu veroeffentlichende
    Nachrichtmessage = "Beispielnachricht"

    # Google Buzz Konfiguration
    gmail_user = "username@googlemail.com"
    gmail_pwd  = "password"

    # Ab hier nichts mehr veraendern
    # Derzeit verarbeitet Google Buzz lediglich den Titel einer
    # eingehenden Mail. Daher muss die Nachricht direkt in den# Mailtitel geschrieben werden.
    # so 
    subject = message
    subject = message
    E = sys.exit
    ##############################
    # Send message to Google Buzz
    ##############################
    try:    
        msg = MIMEMultipart()    
        msg['From']    = gmail_user    
        msg['To']      = "buzz@gmail.com"    
        msg['Subject'] = subject    
        msg.attach(MIMEText(message))    
        smptServer = smtplib.SMTP("smtp.gmail.com", 587)    
        smptServer.ehlo()    
        smptServer.starttls()    
        smptServer.ehlo()    
        smptServer.login(gmail_user, gmail_pwd)    
        smptServer.sendmail(gmail_user, to, msg.as_string())
        smptServer.close()
    except: 
        print ("Kein Versand an Google Buzz moeglich")     
        E(8)


Grosser Dank für diesen Teil geht dabei an [samof76 von Megam: Cloud
Buzz][1]. Dort habe ich die Basis für den Mailversand her.  
  
Der Einfachheit halber habe ich hier in den Beispielen zwei separate
Skripte vorgestellt. Für Insulae sind die entsprechenden Schritte im
Portal zentral eingebettet.  
  
Warum der Aufwand? Um schnell und einfach in verschiedenen Kanälen
Informationen ueber Insulae zu verbreiten. In meinen Augen ist es in der
heutigen Zeit notwendig, die zur Verfügung stehen Mittel auch
vollständig zu nutzen. Je breiter die Informationsbasis, umso mehr
potentielle Spieler lassen sich finden. Je mehr Informationskanäle
genutzt werden, umso geringer die Wahrscheinlichkeit einen potentiellen
Spieler nicht zu erreichen. Daher gilt ein meinen Augen: Der Spieler
sucht sich den Informationskanal, der ihm gefällt. Gerade Browsergames
bei denen keine grosse Entwicklungsfirma im Hintergrund steht, können
sich in meinen Augen nicht erlauben, Spielern zu diktieren welchen Kanal
sie zu nutzen haben, erst recht wenn sie erst noch Spieler werden
sollen. Gar nichts zu veröffentlichen ist inakzeptabel.  
  
Wenn wie oben bereits angesprochen auch Facebook in mein Portal
integriert ist, habe ich denke ich eine gute bis sehr gute Abdeckung von
Informationskanälen die ich mit Infos bestücke. Dabei gilt: je mehr,
umso besser. Aber nur relevante Informationen! Zu wenig, und Spieler
koennen den Eindruck gewinnen das ein Projekt eingeschlafen ist. Zu
viele, und wichtige Infos koennen unter der Masse verloren gehen.  
  
Daher: __Spread the word!__ 
  
Interessant wäre es eventuell auch, Google Wave anzusprechen. Doch
derzeit bin ich vom insgesamten Nutzen von Wave nicht überzeugt, daher
steht dieses Kanal auch noch sehr weit hinten an. Ob, ausser Facebook
und eventuelle Google Wave, noch andere Kanäle angebunden werden... das
kann ich zum aktuellen Zeitpunkt noch nicht sagen. Ich wünsche mir
allerdings, das die verbliebenen deutschen Browsergame-Portale
entsprechende Schnittstellen anbieten würden damit auch diese in einem
Schritt gefüttern werden koennen. Aber dies wird wohl niemals
passieren.  
  
Nebenbei: die Suchmaschinen werden mittels Ping-Dienste aus dem Blog
bereits darauf hingewiesen das es neues Futter für sie gibt welches sie
konsumieren können. Also auch dieser Teil erfolgreich abgedeckt.

[1]: http://megam.info/2009/10/28/gmail-pytho/
