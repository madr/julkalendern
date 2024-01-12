Advent of Code 2019
===================

Solutions for #aoc2019 in Python 3 (3.11.5).

Help scripts
------------

Display all solved puzzles:

    python aoc.py
    
To bootstrap a new puzzle (creates `input/<day_no>.txt` and `output/day_<day_no>.py`):

    python aoc.py <dag_no> "<puzzle_name>"

Manually copy the puzzle input from https://adventofcode.com and paste it in `input/<day_no>.txt`
to start coding.

Solve separate puzzle (replace `XX` with the puzzle number):

    python -m output.day_XX

Solve separate puzzle using stdin (replace `XX` with the puzzle number):

    xclip -selection clipboard -o | python -m output.day_XX
    cat tmpfile | python -m output.day_XX

Execute separate puzzle on file save (replace `XX` with the puzzle number):

    ls output/*.py | entr -c -s 'xclip -selection clipboard -o | python -m output.day_XX'
    ls output/*.py | entr -c -s 'cat tmpfile | python -m output.day_XX'
    ls output/*.py | entr -c -r python -m output.day_XX

(requires `entr` and `xclip`, Mac users can instead use `pbpaste`)
