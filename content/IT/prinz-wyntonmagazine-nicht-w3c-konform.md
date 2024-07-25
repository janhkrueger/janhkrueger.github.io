Title: PRiNZ WyntonMagazine nicht W3C-konform
Date: 2008-09-12 23:58
Author: Jan H. Krüger
Category: IT
Slug: prinz-wyntonmagazine-nicht-w3c-konform

**Durch reinen Zufall, ich habe eigentlich etwas anderes versucht, habe
ich mal den Markup Validation Service vom W3C aufgerufen und auf mein
Blog losgelassen. Ergebnis: Grauenhaft.**  
  
Einen Teil der Fehler konnte ich zwars relativ leicht beheben weil
gewisse Ende-Kennzeichnungen nicht gesetzt waren, aber nun, nach der
Bereinigung bleiben noch 7 Fehler uebrig welche ich so wie ich das sehe
nicht beheben kann. Diese sieben stammen so wie ich das gerade sehe von
dem bei mir verwendeten Theme. Dabei sind fuenf plus zwei aus derselben
Kategorie. Bzw, nach genauerem Hinsehen muss ich mich korrigieren. Nur
drei der hier aufgelisten Meldungen stammen tatsaechlich aus dem Theme.  
  
Vier davon kommen sogar direkt aus Wordpress selbst. Genauer gesagt aus
der Tagcloud. Ok dachte ich erst, da wurde was beim drumrumbauen im
Theme falsch gemacht. Aber auf der Dokumentation wie wp\_tag\_cloud() zu
verwenden ist muss ich sehen, [PRiNZ WyntonMagazine][] haelt sich genau
an das was auch in der [Dokumentation][] steht.  

1.    

        document type does not allow element "h2" here; assuming missing "li" start-tag

    <p>
      

2.    

        document type does not allow element "li" here; missing one of "ul", "ol", "menu", "dir" start-tag

    <p>
      

3.    

        document type does not allow element "a" here; assuming missing "li" start-tag

    <p>
      

4.    

        document type does not allow element "li" here; missing one of "ul", "ol", "menu", "dir" start-tag

    <p>
      

5.    

        end tag for "li" omitted, but OMITTAG NO was specified

    <p>
      

6.    

        end tag for "li" omitted, but OMITTAG NO was specified

    <p>
      

  
Ich fuerchte ich muss da die Tage mal intensiver nach suchen wie ich in
den Griff bekommen kann.  
  
Quellen: [PRiNZ WyntonMagazine][], [Markup Validation Service][],
[Dokumentation wp\_tag\_cloud()][Dokumentation]

  [PRiNZ WyntonMagazine]: http://www.wp-themes.der-prinz.com/magazine/
  [Dokumentation]: http://codex.wordpress.org/Template_Tags/wp_tag_cloud
  [Markup Validation Service]: http://validator.w3.org/check?uri=http%3A%2F%2Fwww.janhkrueger.de%2Fblog%2F2008%2F09%2F11%2Fwow-collectors-edition-eingetragen%2F&charset=(detect+automatically)&doctype=Inline&group=0
