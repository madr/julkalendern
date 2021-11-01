Advent of Code 2020
===================

Solutions for #aoc2020 in Python 3 (3.7+).

Help scripts
------------

Solve all puzzles:

    python aoc.py
    
To bootstrap a new puzzle (creates `inputs/<day_no>.txt`, `solutions/day_<day_no>.py` och
`tests/test_day_<day_no>.py`):

    python aoc.py <dag_no> "<puzzle_name>"

Manually copy the puzzle input from https://adventofcode.com and paste it in `inputs/<day_no>.txt`
to start coding.

Solve separate puzzle (replace `XX` with the puzzle number):

    python -m solutions.day_XX

Run tests (replace `XX` with the puzzle number):

    python -m unittest --locals -v
    # or, if `pytest` is preferred:
    pytest