Title: EVE - Wöchentliches Auslesen der KillMails
Date: 2014-03-16 15:52
Author: Jan H. Krüger
Category: Games
Tags: Datenanalyse, Datensammlung, EVE, EVE Online, Killmails, zKillboard
Slug: eve-wochentliches-auslesen-der-killmails

Nachdem nun recht viel in der Vorbereitung erledigt ist bin ich aktuell
dabei die letzten Schritte für eine Automatisierung zu unternehmen. Ich
will ja nicht regelmäßig die Shellskripte anpassen. Also ein wenig mit
den date() Funktionen in der Shell rumgeschoben und schon passt alles.

<iframe style="border: none; width: 100%;" src="https://janhkrueger.de/stikked/view/embed/10c7500b" height="240" width="320"></iframe>

Damit hole ich mir nun jede Woche die letzten Einträge zu diesen
Kategorien. Jeden Montag um 18:30 Uhr startet das ganze. Der Output wird
mir per Mail zugesandt damit ich direkt sehen kann ob etwas schief
gegangen ist. Das sieht dann Beispielhaft wie folgt aus:

<iframe style="border: none; width: 100%;" src="https://janhkrueger.de/stikked/view/embed/e282bd96" height="240" width="320"></iframe>

Tjo, das einzige was nun noch fehlt ist ein entsprechender Export der so
gelesenen Daten damit diese dann wieder allen zur Verfügung gestellt
werden können. Aktuell wird immer das volle Jahr 2014 exportiert,

Das Skript selbst ist wie üblich im öffentlichen [Git-Repository][]
enthalten.

  [Git-Repository]: http://janhkrueger.de/gitpup/?p=KillReporter.git
