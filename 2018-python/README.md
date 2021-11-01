Advent of Code 2018
===================

Lösningar för #aoc2018 i Python 3 (testat mot 3.7.1).

Hjälpscript
-----------

För att köra alla lösningar:

    python aoc.py
    
För att starta en ny dag (skapar och populerar filerna `inputs/<dagnummer>.txt`, `solutions/day_<dagnummer>.py` och
`tests/day_<dagnummer>_tests.py`):

    python aoc.py <dagnummer_utan_nolla> "<namn på dag>"

Öppna puzzle input manuellt och kopiera innehållet till `inputs/<dagnummer>.txt` som ett sista manuellt steg.

För att köra separat lösning (ersätt `XX` med dagens nummer):

    PYTHONPATH=$(pwd) python solutions/day_XX.py
    
Starta automatisk testkörare (ersätt `XX` med dagens nummer):

    export PYTHONPATH=$(pwd)
    ls solutions/**/*.py | entr -c -r python tests/day_XX_tests.py

Logg
----

 * Dag 1: Insikten när en for-loop kan ersättas med en `sum`. xD Dagens `itertools`: `cycle()`
 * Dag 2: Dagens `itertools`: `combinations()`, efter många försök att vara för smart med `zip()`.
 * Dag 3: Dagens `itertools` (ja, det verkar vara ett tema!): `product()`. Två nästlade for-loopar kändes trist.
 * Dag 4: Mycket text och mycket kod. Dagens `itertools`: `chain()`.
 * Dag 5: Krånglade till saker genom att köra listor istället för strängar, skrev om till att istället använda en 
   `reduce`. Inga `itertools`. :(
 * Dag 6: Längsta körtiden hittills och kan högst troligtvis optimeras.
 * Dag 7: Svårtolkad uppgift. Otäckt med workers. Rant i [kodkommentar om icke hjälpsamt 
   exempel](https://github.com/madr/redesigned-system/blob/master/solutions/day_07.py#L63-L70).
 * Dag 8: Rekursion! Invigning av `sys.setrecursionlimit()`.
 * Dag 9: Harakiri.
 * Dag 10: Kult med visualisering! Fick tipset att leta efter minsta bounds, och kom då fram till den magiska siffran 
   `10391`. Det krävdes en hel del optimering, då första versionen var slö.
 * Dag 11: [Summed-area table](https://en.wikipedia.org/wiki/Summed-area_table). Lösning 2 behöver refaktoriseras för
   att använda partial sum och summed-area table, den tar 8-12h att köra med brute force.
 * Dag 12: Otydliga instruktioner. [Inte bara enligt mig](https://www.reddit.com/r/adventofcode/comments/a5gt7h/day12_part_1_explanation_for_the_example/),
    [vad det verkar](https://www.reddit.com/r/adventofcode/comments/a5eztl/2018_day_12_solutions/).
 * Day 13: Ännu en dag med ett exempel som var vilseledande för att testa ens kod. 
   [Rant i kodkommentar](https://github.com/madr/redesigned-system/blob/master/solutions/day_13.py#L108-L141).
 * Day 14:
 * Dag 15: 