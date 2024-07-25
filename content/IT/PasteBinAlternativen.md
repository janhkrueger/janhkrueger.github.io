Title: PasteBin Alternativen
Date: 2015-01-11 02:06
Author: Jan H. Krüger
Tags: PasteBin,Alternativen, SelfHosted


Im Zuge des Umzuges auf selbstgehostete Software habe ich bereits vor Monaten kurz etwas über zwei PasteBin-Alternativen geschrieben. [Stikked][StikkedURL] und [ZeroBin][ZeroBinURL]. Tatsächlich gibt es jedoch noch mehr vergleichbarer Software.

Jedoch vorweg: Ich setze bei mir sowohl Stikked wie auch ZeroBin ein. Für unterschiedliche Anwendungsfälle. Die Zugänge zu beiden Systemen habe ich an ausgewählte Personen weitergegeben. Insbesondere ZeroBin wird hier genutzt. Und: mich interessieren nur Softwareprodukte welche ich selbst bei mir auf einem Server betreiben kann. SelfHosted ist hier das Stichwort.

<!--more-->

Zurück zu weiteren Produkten. Eines welches mir erst kürzlich über den Weg gelaufen ist, nennt sich MarkdownShare.com. Es zielt auf eine recht enge Benutzergruppe ab, nämlich auf Personen welche ihre Texte in [MarkDown-Syntax][MarkDownSyntaxURL] schreiben. Und das liegt ja nun nicht jedem. Für mich persönlich nicht so die Schwierigkeit. Ein Punkt der mich jedoch von einem Einsatz abhält ist die Abhängigkeit zu [Redis][RedisURL]. Nicht das Redis per Definition schlecht ist. Jedoch sehe ich nicht warum ich extra für ein Produkt ein anderes Infrastrukturprodukt installieren sollte.

Ebenfalls denkbar ist noch der Einsatz von [HasteBin][HasteBinURL]. Dieses nutzt [node.js][NodejsURL] welches bei mir allein wegen dem Betrieb von EtherPad Lite und EtherCalc schon im Einsatz ist. Neben Redis kann als Datenablage auch das Dateisystem mit normalen Dateien genutzt werden, oder komplett im Speicher mit Memcached. Der Quellcode ist im entsprechenden [GitHub-Repository][HasteBinRepoURL] verfügbar. Interessant hierbei: die Eingabe erinnert an eine Kommandozeile auf der Konsole. Könnte definitiv eine interessante Spielerei sein, insbesondere da es schnell und einfach möglich ist per cat einen Paste zu erstellen.
Also, zusammengefasst sehe ich derzeit folgende für mich relevante Möglichkeiten einen eigenen Paste-Dienst aufzubauen:

* Stikked
* ZeroBin
* MarkDownShare
* HasteBin
    
HasteBin fällt bei mir jedoch nach den ersten Betrachtungen direkt wieder raus. [node.js][NodejsURL] läuft zwars bei mir wegen den Pads, doch wirklich zufrieden bin ich damit nicht. Es kommt mir... dick und aufgebläht vor. Bei den Pads habe ich keine Alternative, hier bei den PasteBinalternativen jedoch schon. Und im Zweifel habe ich gerne lieber weniger Dienste auf meinem Server laufen.

MarkdownShare scheint mir keine Übersicht über bereits geteilte Inhalte zu bieten. Für mich vergesslichen Menschen doch sehr wichtig um auch mal alte Inhalte nachschlagen zu können.

Es gibt im Netz noch zahlreiche andere Dienste. Oft ist jedoch keine Möglichkeit gegeben die Software selbst auf einem Server zu betreiben. Und die fallen, wie eingangs schon geschrieben, allesamt für mich weg.

[StikkedURL]: https://github.com/claudehohl/Stikked
[ZeroBinURL]: http://sebsauvage.net/wiki/doku.php?id=php:zerobin
[MarkDownShareURL]: http://MarkdownShare.com
[MarkDownSyntaxURL]: http://daringfireball.net/projects/markdown/syntax
[RedisURL]: http://redis.io/
[HasteBinURL]: http://www.hastebin.com
[HasteBinRepoURL]: https://github.com/seejohnrun/haste-server
[NodejsURL]: http://nodejs.org
