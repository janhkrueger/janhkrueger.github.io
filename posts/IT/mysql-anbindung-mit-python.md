Title: MySQL-Anbindung mit Python
Date: 2008-11-05 17:35
Author: Jan H. Krüger
Category: IT
Slug: mysql-anbindung-mit-python

<p>
**Um mal ein wenig rumzuspielen habe ich mir einmal die
Datenbankanbindung mittels Python angeschaut. Bzw. eigentlich steht
Python an sich im Vordergrund, jedoch werde ich wenn ich schon ein wenig
rumprobiere mir auch auch Datenbanken anschauen.**  
  
Um mal einen Ueberblick zu erhalten, versuchte ich eine Anbindung an
MySQL zu erstellen. Ich muss sagen, solch Basiskarm geht erstaunlich
einfach. Interessant wird es wenn ich das ganze mal intensiv einsetze
und etwas anspruchloseres probiere. Ich bin mal gespannt und hoffe das
ich am Wochenende dazu komme.  
  

~~~~ {lang="Python" line="1" file="python_dbtest.txt"}
# mysqltest.pyimport MySQLdb# Datenbankverbindung oeffnenconn = MySQLdb.connect (host = "localhost",                        user = "USER",                        passwd = "PASS",                        db = "DNAME")cursor = conn.cursor ()# Abfrage erstellen.cursor.execute ("select aberuf_name from archetyp.beruf order by aberuf_name")# Die Daten Ausgebenfor row in cursor:        print row[0]# Cursor und Verbindung schliessencursor.close ()conn.close ()
~~~~
