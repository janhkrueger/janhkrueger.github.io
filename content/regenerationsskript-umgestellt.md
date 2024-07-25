Title: Regenerationsskript umgestellt
Date: 2009-01-08 01:14
Author: Jan H. Krüger
Category: Insulae
Slug: regenerationsskript-umgestellt

<p>
Nachdem ich die Tage dann endgueltig entschieden habe das die
BackEnd-Skripte in Python entstehen sollen, habe ich mich nun daran
gemacht das erste umzustellen. Das Regenerationsskript, wachstum.php ist
fortan nicht mehr notwendig. Die Aufgaben uebernimmt nun wachstum.py.  
  
Zugegeben, das ganze sieht noch etwas holprig aus und laesst sich
bestimmt noch sauberer schreiben, aber was sollst. Mein erstes
Pythonskript mit Postgresanbindung. Um genau zu sein, ich empfinde den
Quellcode derzeit noch stark als unsauber. Aber das kommt mir der Praxis
von alleine. Erste Erkenntnisse: es laefut schneller. Dabei habe ich
bereits die Optionen romod1 bis romod4 mit enthalten, was das bisherige
PHP-Skript noch nicht konnte. Weiterhin werde ich mir definitiv etwas
basteln muessen um die Abfragen auszufuehren. Der rohe Code wirkt doch
etwas viel und somit unuebersichtlicht.  
Nun steht noch der Einbau der Phasenoptionen an und dann ists endgueltig
fertig.  
  
Wie auch immer. Es geht vorran. Und warum funktioniert wp\_codebox nicht
mehr?  
  

~~~~ {lang="python" line="1"}
#! /usr/local/bin/python### Copyright (c) 2009, Jan H. Krueger# All rights reserved.## The contents of this file are subject to the GNU Lesser General Public# License (the "License"); you may not use this file except in# compliance with the License. You may obtain a copy of the License at# http://www.gnu.org/licenses/lgpl.html## Software distributed under the License is distributed on an "AS IS"# basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See# the License for the specific language governing rights and limitations# under the License.### File: wachstum.py# Authors: Jan H. Krueger (game.insulae@googlemail.com)# Created: (07/01/2009)# Last Updated: (08/01/2009)# Version: 1.0# Package: Insulae# Category: Insulae-Backend# Todos: use the phasing options ### Let the land grow and produce new ressources at the farmable places.#import psycopg2import psycopg2.extensionsimport datetimeimport timeimport sysE = sys.exit### Connect to the postgresql database.con = psycopg2.connect(    database = "insulae",    host = "localhost",    user = "",    password = ""    )varskriptname = 'wachstum.py'### open cursorcu=con.cursor()### log the start of wachstum.pytry:    varstatus = 'beginn'    zeit = time.mktime(time.localtime(time.time()))    vartime = str(zeit)[0:-2]    sql = """insert into daten.skriptlog (skriptname, zeitstempel,              verarbeitungsstatus) values (%s, %s, %s)          """    cu.execute(sql, (varskriptname, vartime, varstatus))    con.commit()except psycopg2.ProgrammingError, errval:     print errval     E(8)### den romod_1 auslesentry:    sql = """select wert from optionen.einstellungen              where einstellung = 'romod_1'          """    cu.execute(sql)    romod1 = cu.fetchone()except psycopg2.ProgrammingError, errval:     print errval     E(8)### den romod_2 auslesentry:    sql = """select wert from optionen.einstellungen              where einstellung = 'romod_2'          """    cu.execute(sql)    romod2 = cu.fetchone()except psycopg2.ProgrammingError, errval:     print errval     E(8)### den romod_3 auslesentry:    sql = """select wert from optionen.einstellungen              where einstellung = 'romod_3'          """    cu.execute(sql)    romod3 = cu.fetchone()except psycopg2.ProgrammingError, errval:     print errval     E(8)### den romod_4 auslesentry:    sql = """select wert from optionen.einstellungen              where einstellung = 'romod_4'          """    cu.execute(sql)    romod4 = cu.fetchone()except psycopg2.ProgrammingError, errval:     print errval     E(8)# TODO: read the modificators for the phases### build and execute the updatetry:    sql = """update welt.karte_phase set              karte_rohstoff1 = (karte_rohstoff1+karte_landwert)*%s,              karte_rohstoff2 = (karte_rohstoff2+karte_landwert)*%s,              karte_rohstoff3 = (karte_rohstoff3+(karte_landwert / 2))*%s,              karte_rohstoff4 = (karte_rohstoff4+(karte_landwert / 2))*%s           """    cu.execute(sql, (romod1, romod2, romod3, romod4 ))    con.commit()except psycopg2.ProgrammingError, errval:     print errval     E(8)# Generate an entry in the history table to show the playerstry:    zeit = time.mktime(time.localtime(time.time()))    vartime = str(zeit)[0:-2]    histart = 1000000001    histeintrag = 'Das Land regeneriert sich.'    histprivat = 'n'    histphase = 1000000000    sql = """insert into sonstiges.historie              (historie_datum, historie_art, historie_eintrag,              historie_privat, historie_phase) values (%s, %s, %s, %s, %s)          """     cu.execute(sql, (vartime, histart, histeintrag, histprivat, histphase))     con.commit()except psycopg2.ProgrammingError, errval:     print errval     E(8)# Log the ending of wachstum.py.try:    varstatus = 'ende'    zeit = time.mktime(time.localtime(time.time()))    vartime = str(zeit)[0:-2]    sql = """insert into daten.skriptlog (skriptname, zeitstempel,              verarbeitungsstatus) values (%s, %s, %s)"""    cu.execute(sql, (varskriptname, vartime, varstatus))     con.commit()except psycopg2.ProgrammingError, errval:     print errval     E(8)# Close the cursor and connection, end the script.cu.close() con.close()E(0)
~~~~
