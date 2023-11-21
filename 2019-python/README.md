Advent of Code 2023
===================

Solutions for #aoc2023 in Python 3 (3.11.5).

Help scripts
------------

Display all solved puzzles:

    python aoc.py
    
To bootstrap a new puzzle (creates `inputs/<day_no>.txt` and `src/day_<day_no>.py`):

    python aoc.py <dag_no> "<puzzle_name>"

Manually copy the puzzle input from https://adventofcode.com and paste it in `inputs/<day_no>.txt`
to start coding.

Solve separate puzzle (replace `XX` with the puzzle number):

    python -m src.day_XX

Solve separate puzzle using stdin (replace `XX` with the puzzle number):

    xclip -selection clipboard -o | python -m src.day_XX
    cat tmpfile | python -m src.day_XX

Execute separate puzzle on file save (replace `XX` with the puzzle number):

    ls src/*.py | entr -c -s 'xclip -selection clipboard -o | python -m src.day_XX'
    ls src/*.py | entr -c -s 'cat tmpfile | python -m src.day_XX'
    ls src/*.py | entr -c -r python -m src.day_XX

(requires `entr` and `xclip`, Mac users can instead use `pbpaste`)
