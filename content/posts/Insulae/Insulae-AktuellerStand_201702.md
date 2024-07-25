Title: Insulae - Aktueller Stand Februar 2017
Date: 2017-02-28 14:50
Author: Jan H. Krüger
Tags: Insulae, Zwischenstand, PBBG, Browsergame
Category: Insulae
Slug: insulae-stand-februar2017
Series: Insulae-Stand

Moin Moin,

ganz knapp zum Ende des Monats hin noch der Stand für Februar eingereicht.

Der Monat war technisch sehr... nervig für mich verbunden mit einem Ausfall von ca. einem Tag für Insulae.
Aus naivität habe ich gedacht, ich könnte ja mal eine neue Version der C++-Klassen für PostGres einsetzen. Gemäß der [alten Webseite][2] wird die Entwicklung nun in einem [Git Repository][1] vorran getrieben. An sich ja auch prima.
Also, Repository geklont, gebaut und installiert. Ausprobiert und... jede Menge Fehler vom Compiler. Hm, ok, nach und nach ran gehen.

Ich hab alles mir mögliche ausprobiert. Klassen neu installiert. PSQL_DEV Libs neu. PostGres deinstalliert. Am Ende hab ich auch PostGres deinstalliert und gleich die 9.6er Version (Yeah, Upserts!) installiert.
Hat alles nichts gebracht. Am Ende habe ich wieder die letzte Version von libpqxx welche noch auf der Webseite war genommen. Und tada... funktioniert. Ohne Murren.

Resultat: alte Klassen mit neuer Datenbank und zwei Wochen Zeit "verloren". Egal.


Die Umstellung der API auf C++ ist gut vorran gekommen. Der API-Server ist fast fertig. Die Stadt-API ist bereits fertig und produktiv. Eine [Beispielausgabe][3] steht auch bereit.

Der Server wird wie letzten Monat bereits berichtet von [Pistache][4] angetrieben. Als Logginframework nutze ich [gabime/spdlog][5]. Läuft auch fast anstandslos. Bin nur auf eine Stelle ziemlich auf die Nase gefallen, doch das konnte ich mit ein wenig debugging via gdb konnte ich dahinter kommen. Ein fieser "Segementation Fault".

Die Ursache war an sich recht einfach. mittels gabime/spdlog kann ich einen neuen Logger wie folgt anlegen:

```
auto rotating_logger = spd::rotating_logger_mt("insulae_api", "/var/log/insulae/insulae_api", 1048576 * 5, 3);
```

Soweit so gut. Den kann ich dann direkt ansprechen mit:

```
rotating_logger->info("Server gestartet");
```

Alles shiny.

Wenn ich diesen Logger nun irgendwo anders nutzen will, kann ich ihn auch mir dort wo ich ihn brauche direkt holen:

```
spd::get("insulae_api")->info("Endpoint getStaedte aufgerufen");
```

Sieht gut aus. Wenn jetzt allerdings der Logger, in diesem Falle "insulae_api", nicht bereits vorher angelegt wurde, raucht das Programm direkt ab.

```
(gdb) run
Starting program: /home/insulae/insulae-private/api/apiserver/api_server
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x0000555555570563 in void spdlog::logger::log<>(spdlog::level::level_enum, char const*) [clone .lto_priv.119] ()
```
Unschön. Ich bin mir noch nicht sicher ob ich da einen Issue einstelle oder ob ich das unter "mach es richtig und es tut" abhake.


Wie auch immer. Offen im Server ist jetzt noch eine vernünftige JSON-generierung. Da habe ich noch nicht das mir zusagende Framework gefunden. Und dann die Dokumentation der API mittels [swagger.io][6]. Aber halt eines nach dem anderen.

Wenn der API-Server steht werde ich den Rest der reinen PHP-Klassen auch gegen C++ ablösen und dann in PHP einbinden. Das wird jedoch nicht ganz so einfach sein da ich hier keine Eins-zu-Eins-Umstellung angehen kann sondern auch vom Aufbau Umstellungen vornehmen muss. Die alten PHP-Klassen fragen zB zum Teil selbst Daten von der Datenbank ab und bekommen nicht alles was sie benötigen von aussen. Jugendsünde und so halt.
Doch damit sollte die bisherigen 9% C++ auch deutlich ansteigen. und PHP ordentlich sinken. Wobei ich etwas überrascht bin das PLpgSQL auf 13.6% steht.

Bezüglich swagger: ich bin immer noch zwiegespalten. Auf der einen Seite: genial und will ich eigentlich auch nutzen. Andererseits: node.js... das wird noch ein Kampf mit mit selbst.


Ansonsten:
Eigene Portale durch Spieler zu errichten: da bin ich auf Grund der oben beschriebenen Punkte nicht zu gekommen, daher Status unverändert.

Eine Sache vielleicht noch am Rande. Mittlerweile gefällt mir GitHub immer besser. Über die Projekte kann ich meine Aufgaben und Issues auch in Kanbanboards organisieren. Am Anfang etwas ungewöhnlich und gerade für mich als Soloentwickler vielleicht etwas oversized. Doch damit ist eine super einfache visualisierung der aktuellen Aufgaben möglich.
Da ich das Repository auf Github auch mit dem Insulae-Slack verbunden habe, können die Spieler dort auch sofort sehen wenn ich dort twas bearbeite. Oder generell leichter sehen woran ich gerade arbeite.
Ich habe das nun ungefährt sechs Monate so am laufen und bisher ist das Handling für mich entspannt und die Spieler genießen eine höhere Transparenz woran derzeit gearbeitet wird.

Ursprünglich hatte ich auch überlegt ob dich meine C++-Programme mittels Travis bauen und testen lasse. Da Insulae jedoch in einem privaten Repository liegt, geht es für Travis nicht mehr als Open Source durch. Bedeuted: es würde mich $69 pro Monat kosten.
Das sind kosten welche ich derzeit nicht bereit bin für Insulae auszugeben. Der Server mit seinen 60€ sind kein Problem. Den nutze ich rund um die Uhr, die Spieler haben einen Nutzen und ich kann ihn zur Weiterbildung gebrauchen.
Die $69 für etwas das ich nur an gewissen Tagen im Monat nutze, dann auch noch alleine. Nein. Dann lieber irgendwann einen dickeren Server für Insulae. Da haben dann auch alle etwas davon.

Ingame: Der Krieg der Götter ist immer noch dabei.
Ansonsten hatte ich im Februar nicht so viel Zeit dem ganzen Treiben zu folgen oder auch Updates zu twittern. Da haben mich andere Themen zu sehr abgeholen.

[1]: https://github.com/jtv/libpqxx/
[2]: http://pqxx.org/development/libpqxx/
[3]: https://gist.github.com/janhkrueger/9127a29221cee5ee41fedb41101790c4
[4]: https://github.com/oktal/pistache
[5]: https://github.com/gabime/spdlog
[6]: http://swagger.io/

[3]: http://tgwnn.rpgame.de/
[4]: http://inselpioniere.de/
[5]: http://karasan.de/
[6]: http://www.joscha2k.de/
[7]: http://www.scherbenwelten.net/

