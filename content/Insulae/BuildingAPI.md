Title: Gebäude nun auch per API verfügbar
Date: 2019-07-29 22:55
Author: Jan H. Krüger
Tags: Insulae, Zwischenstand, PBBG, Browsergame
Category: Insulae
Slug: insulae-building-api
Series: Insulae-Stand

Heute konnte ich wieder einen großen Teil modernisieren und fit für die Zukunft gestalten als Plan Insulae in der Zukunft OpenSource zu stellen.

Die Gebäude sind nun alle gleichförmig gestaltet und können von mir fast vollständig über die Datenbank gesteuert und parametrisiert werden. Produktionsgebäude sogar völlig.

Das erlaubt es mir Gebäude im Zeitrahmen von Minuten einzuführen oder zu verändern. Während die große Masse bereits früher einheitlich die die Datenbank gesteuert wurde ist nun alles auch in über die API abrufbar und damit für mich und die Spieler leichter zugänglich.

Das Herz bilden vier Tabellen in welchen ich ein Gebäude sowie seine Ausbauten definiere.

* building
* building_upgrades
* building_upgrade_goods
* building_upgrade_productiongoods

![Buildingtabellen](images/Tables.png)

Dies ist die Grundsätzliche Definition eines Gebäudes. Sein Name, der Baugrund, das oder die Ökosysteme in welchen das Gebäude gebaut werden kann, ob es in einer Stadt gebaut werden kann und oder außerhalb unter freiem Himmel und so weiter.

![BuildingUpgrades](images/building_upgrades.png)

Hier definiere ich welche Ausbauten ein Gebäude haben kann. Ein Ausbau bestimmt welche Ware der Ausbau produziert, die Produktionsformel, der benötigte Skill zum Produzieren und wie sich der Verbrauch an Vorräten berechnet.
Dabei ist zu beachten das dies hier die reguläre Zuordnung Ausbau zu Gebäude definiert ist. Wenn, zum Beispiel durch ein Quest oder eine göttliche Intervention ein Gebäude einen untypischen Ausbau erhält kann das Gebäude auch diesen verwenden ohne das es technisch Komplikationen gibt.
Gleichzeitig konnte ich so bei einem Bauernhof die vier Waren, Getreide, Wolle, Pferde und Kühe in separate Ausbauten aufteilen was den Bürgermeistern die Möglichkeit bietet selbst eine Priorität in der Produktion zu erhalten.

![BuildingUpgradeGoods](images/building_upgrade_goods.png)

Ein Ausbau kann auch durch den Besitzer gesteigert werden um den Ertrag zu erhöhen. Die Angaben hier sind die Grundlage um von Level 0 auf Level 1 zu gelangen. Die Kosten steigen linear.


![BuildingUpgradeProductionGoods](images/building_upgrade_productiongoods.png)

Benötigt ein Gebäude für die Produktion andere Waren werden sie hier definiert. Einträge hier sind optional. Sind sie jedoch gesetzt müssen die Rohstoffe vorhanden sein. Sofern gesetzt besteht hier eine Kardinalität von 1:n.
Die Angabe ist keine gerade Zahl und kann damit auch Werte wie 0.5 umfassen. Dies ist primär für Großbetriebe wie Manufakturen vorgesehen.

Mittels dieser vier Tabellen kann ich flexibel und vollständig ohne Codeänderungen neue Gebäude hinzufügen, die Ausbauten von Gebäuden verändern, die Formel zur Produktion bzw. zum Verbrauch verändern. Die derzeit benötigten Variablen sowie noch weitere nicht genutzte werden bereits in die Formeln eingesetzt.

Für einen Bauernhof, konkret die Felder, sieht die Formel wie folgt aus:
```
"RoundDown( (changeSkillLevelByValue + 1) * (changeBuildingUpgradeLevelByValue +1) * (changeFieldValueByValue / 8) * changeProductionBuildingByPercentage * changeProductionWeatherByPercentage * changeProductionGlobalByPercentage * changeProductionPhaseByPercentage) * 5"
```

Da Getreide eine Massenware ist und von mir auch so vorgesehen ist, wird der Ertrag hier noch einmal um den Faktor 5 erhöht wie durch die * 5 dargestellt wird. In dieser Formel kann ich wie in Excel schnell und unkompliziert Änderungen vornehmen. Innerhalb von kurzer Zeit, ohne Änderungen am Quellcode der Zugrundeliegende Basis.
Für Gebäude in Städten oder Produktionen welche nicht durch den Feldwert beeinflusst werden, fehlt zum Beispiel die Variable "changeFieldValueByValue".

In der [Building-API][1] sieht das dann wie folgt aus:

![APIBuildingListing](images/API_BuildingListing.png)

Ein [konkretes Gebäude][2] wird wie folgt dargestellt:

![APIBuildingDetails](images/API_BuildingDetails.png)

Diese Angabe ist es auch welche ich nun in Insulae für alle Belange der Produktionsgebäude verwende. Ein direkter Datenbankzugriff findet so nicht mehr statt.

Die Bereitstellung über eine öffentliche API hat für mich zwei Vorteile. Spieler und ich nutzen dieselbe Basis. Und ich muss nur einmal den Zugriff implementieren während alle anderen Bereiche den Endpunkt verwenden.


Für Gebäude welche nichts produzieren wird zur Steuerung das Effektsystem verwendet. Das ist noch nicht in der API reflektiert und steht als nächstes auf der ToDo-Liste.

[1]: https://api.insulae.janhkrueger.de/building
[2]: https://api.insulae.janhkrueger.de/building/46
