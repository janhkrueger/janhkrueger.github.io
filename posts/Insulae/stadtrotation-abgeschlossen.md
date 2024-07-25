Title: Stadtrotation abgeschlossen
Date: 2009-01-18 01:10
Author: Jan H. Krüger
Category: Insulae
Slug: stadtrotation-abgeschlossen

<p>
Heute habe ich nur ein kleines PHP-Skript umgestellt. Jenes welches
meine wandernden Staedte bewegt hat. Also nichts grosses, da auch hier
in dem Pythonprogramm nicht wirklich viel gemacht wird. Reines
abarbeiten ohne viel drumrum. Aber egal, es laeuft. Und laut meiner
Logtabelle sogar fast doppelt so schnell wie das alte PHP-Skript. Wobei
ich diesen massiven Unterschied wohl eher auf ein mieses PHP-Skript oder
einen nicht ordnungsgemaessen Apache zurueckfuehren moechte.  
  
Was macht das ganze? Es laest Staedte in Insulae um einen festen Punkt
auf der Karte "kreisen" innerhalb eines frei definierbaren Abstandes und
einer frei definierbaren Anzahl von Schritten. So gelangt ein wenig
dynamik mit in die Welt, die Spieler koennen nicht fest davon ausgehen
das eine Stadt sich genau dort befindet wo sie zuletzt war.  
  

~~~~ python
#! /usr/local/bin/python### Copyright (c) 2009, Jan H. Krueger# All rights reserved.## The contents of this file are subject to the GNU Lesser General Public# License (the "License"); you may not use this file except in# compliance with the License. You may obtain a copy of the License at# http://www.gnu.org/licenses/lgpl.html## Software distributed under the License is distributed on an "AS IS"# basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See# the License for the specific language governing rights and limitations# under the License.### File: rotieren_stadt.py# Authors: Jan H. Krueger (game.insulae@googlemail.com)# Created: (18/01/2009)# Last Updated: (18/01/2009)# Version: 1.0# Package: Insulae# Category: Insulae-Backend### Let the wandering towns wander over the map. The here processed towns have# a fix point in the center of the circle-shaped rotating#import psycopg2import psycopg2.extensionsimport conn as dbimport mathimport sysE = sys.exit### Connect to the postgresql database.con = psycopg2.connect(    database = db.dbdatabase,    host = db.dbhost,    user = db.dbuser,    password = db.dbpassword    )cu=con.cursor()pi = math.pi# get all rotating townstry:    sql = """          SELECT rotierung_id, rotierung_x, rotierung_y, rotierung_w,           rotierung_radius, rotierung_schritte, rotierung_aktueller_schritt           FROM sonstiges.rotierung where rotierung_art ='Stadt'          """    cu.execute(sql)    rotationsdaten = cu.fetchall()except psycopg2.ProgrammingError, errval:     print errval     E(8)# let the towns wander aroundfor (rotierung_id, rotierung_x, rotierung_y, rotierung_w, rotierung_radius,      rotierung_schritte, rotierung_aktueller_schritt) in rotationsdaten:    neu_x = rotierung_x+rotierung_radius * math.cos(2 * pi /             rotierung_schritte * rotierung_aktueller_schritt)    neu_y = rotierung_y+rotierung_radius * math.sin(2 * pi /             rotierung_schritte * rotierung_aktueller_schritt)    neu_x = math.floor(neu_x)    neu_y = math.floor(neu_y)    rotierung_aktueller_schritt+=1    # beginn to count from zero if the max setppings    if rotierung_aktueller_schritt == rotierung_schritte:        rotierung_aktueller_schritt = 0    try:        # update the actual rotating step        sql = """              UPDATE sonstiges.rotierung SET rotierung_aktueller_schritt=%s               WHERE rotierung_id=%s AND rotierung_art='Stadt'              """        cu.execute(sql, (rotierung_aktueller_schritt, rotierung_id))        con.commit()        # set the new position for the town        sql =     """              Update stadt.stadt SET stadt_x = %s, stadt_y = %s               WHERE stadt_id=%s              """            cu.execute(sql, (neu_x, neu_y, rotierung_id))        con.commit()    except psycopg2.ProgrammingError, errval:         print errval         E(8)    # Close the cursor and connection, end the script.cu.close() con.close()E(0)
~~~~
