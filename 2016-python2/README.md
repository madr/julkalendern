# Advent of Code 2016

Solutions for #aoc2016 in Python 3 (3.12.7).

## Setup

Since I want to remember, this is what was used to solve
the puzzles.

- Lenovo Thinkpad x260 laptop with Arch Linux.
- Hyprland with gBar.
- Editor: Zed.
- Terminal: Alacritty.

## Help scripts

Display all solved puzzles:

    python aoc.py

To bootstrap a new puzzle (creates `input/<day_no>.txt` and `output/day_<day_no>.py`):

    python aoc.py <day_no> <puzzle_name>

Manually copy the puzzle input from https://adventofcode.com and paste it in `input/<day_no>.txt`
to start coding.

    wl-paste > input/<day_no>.txt

Solve separate puzzle (replace `XX` with the puzzle number):

    python -m output.day_XX

Solve separate puzzle using stdin (replace `XX` with the puzzle number):

    wl-paste | python -m output.day_XX
    cat tmpfile | python -m output.day_XX

Execute separate puzzle on file save (replace `XX` with the puzzle number):

    ls output/*.py | entr -c -s 'wlpaste | python -m output.day_XX'
    ls output/*.py | entr -c -s 'cat tmpfile | python -m output.day_XX'
    ls output/*.py | entr -c -r python -m output.day_XX

(requires `entr` and `wl-paste`, Mac users can instead use `pbpaste`. If you
prefer X at Linux, use `xclip -selection clipboard -o`).

To lint files:

    ls output/*.py | entr -r -c flake8 output --ignore=E741,E501,E203
