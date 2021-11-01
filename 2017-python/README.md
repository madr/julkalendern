Advent of Code 2017
===================

Lösningar för #aoc2017 i Python 3 (testat mot 3.5.2).


Logg
----

 * Särskilt svåra dagar (tidsåtgång mer än 60 min) vid kodtillfället:
   * Dag 3,
   * Dag 6,
   * Dag 7,
   * Dag 14,
   * Dag 18 och
   * Dag 21.
 * Dag 3: del 2 kopierades från en [färdig sekvens](https://oeis.org/A141481). Restpunkt är att faktiskt
   implementera den.
 * Dag 5: del 2 tar väldigt lång tid att exekvera. Restpunkt är att optimera denna!
 * Dag 11: Allt som behövs finns beskrivet på
   [Hexagonal Grids](https://www.redblobgames.com/grids/hexagons/).
 * Dag 13: del 2 misslyckande att hitta något som var snabbt nog att exekvera. 
   Restpunkt är skriva något som inte tar en timme att köra!
 * Dag 14 del 2: Läs på om [Union-find algoritmen](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)
 * Dag 15: borde skrivas om att använda generatorer för att snabbas upp.
 * Dag 18 del 2: ["värdet av" kan betyda flera saker](https://www.reddit.com/r/adventofcode/comments/7kj35s/2017_day_18_solutions/dreth75/) ... jävla etta.
 * Dag 21: Blocken ska divergera och ska därmed testas separat mot reglerna. Detta missade jag, och antog istället att samma regel applicerade på alla block ...


Hjälpscript
-----------

För att köra alla lösningar:

    python aoc.py
    

För att starta en ny dag (skapar och populerar filerna `inputs/<dagnummer>.txt`, `solutions/day_<dagnummer>.py` och
`tests/day_<dagnummer>_tests.py`):

    python aoc.py <dagnummer> "<namn på dag>"

Öppna puzzle input manuellt och kopiera innehållet till `inputs/<dagnummer>.txt` som ett sista manuellt steg.


För att köra separat lösning (ersätt `XX` med dagens nummer):

    PYTHONPATH=$(pwd) python solutions/day_XX.py

    
Starta automatisk testkörare (ersätt `XX` med dagens nummer):

    export PYTHONPATH=$(pwd)
    ls solutions/**/*.py | entr -c -r python tests/day_XX_tests.py
