Title: Datenbankoptimierungen gehen voran
Date: 2010-01-06 00:38
Author: Jan H. Krüger
Tags: Insulae, Datenbank, Optimierung

In den letzten Wochen habe ich mich bei Insulae damit beschäftigt die
Zugriffe zu optimieren. Auslöser ist schlicht und ergreiffend das
Insulae für einen, von mehreren gewünschten produktiven Start, derzeit
noch nicht geeignet ist.  
  
Ich habe also damit angefangen sehr oft gelesene Werte in zusätzliche
Relationen auszulagern um die zu durchsuchende Menge zu verringern. Bei
fast allen Objekten welche auf der Karte dargestellt werden und mit
x/y/w-Koordinaten angesprochen werden ist dies bisher schon umgesetzt.
Da ich oft auch nur auf die Existenz abfrage und nicht die tatsächlichen
Werte oder die Objektindividuellen Kennzeichen, sind hier bereits ein
paar Millisekunden bei herumgekommen.  
  
Danach, und das ist meine derzeitige Baustelle, ist eine Optimierung im
Aufbau des Gruppenschirmes vorgesehen. Aktuell teste ich dafür
Möglichkeit Abfragen welche häufig genutzt werden einmal vorzubereiten
und dann nur noch mit Parametern zu füllen. Prepared Statements also.
Obwohl ich bereits einen Teil umgesetzt habe, kann ich, rein subjektiv,
noch keine Verbesserungen spüren. Mal sehen wie sich das ganze Verhaelt
wenn ich alle relevanten Abfragen umgestellt habe.