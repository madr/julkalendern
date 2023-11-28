from collections import defaultdict
from output.intcode_computer import execute, parse
from output import answer, puzzleinput

n = 11
title = "Space Police"


@puzzleinput(n)
def parse_input(data):
    return parse(data)


DIRS = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]

COLORS = [".", "#"]

CL = ["black", "white"]
DL = ["UP", "LEFT", "BOTTOM", "RIGHT"]
TL = ["RIGHT", "LEFT"]


@answer(1, "[intcode 0.3.2] Robot paints {} panes at least once")
def part_1(program):
    path, pos, d = _paint(program)
    return len(path)


@answer(
    2,
    '[intcode 0.3.2] The hull has registration identifier "JZPJRAGJ" freshly painted, see below: \n\n{}',
)
def part_2(program):
    path, pos, d = _paint(program, 1)
    return _inspect(path.copy(), pos, d)


def _paint(program, initial=0):
    pos = (0, 0)
    d = 0
    path = defaultdict(int)
    path[pos] = initial
    n = 0
    rb = 0
    code = 0
    while True:
        code, program, n, rb, outputs = execute(program, n=n, rb=rb, stdin=[path[pos]])
        if code == 99:
            break
        if outputs:
            paint, turn_to = outputs
            path[pos] = paint
            d = (d - 1 if turn_to == 1 else d + 1) % 4
            pos = (pos[0] + DIRS[d][0], pos[1] + DIRS[d][1])
    return path, pos, d


def _inspect(path, p, d):
    pk = path.keys()
    startx = min(map(lambda yx: yx[1], pk)) - 1
    endx = max(map(lambda yx: yx[1], pk)) + 2
    starty = min(map(lambda yx: yx[0], pk)) - 1
    endy = max(map(lambda yx: yx[0], pk)) + 2

    matrix = [
        [COLORS[path[(y, x)]] for x in range(startx, endx)] for y in range(starty, endy)
    ]
    y, x = p
    matrix[abs(starty) + y][abs(startx) + x] = "^<v>"[d]

    return "\n".join(["".join(line) for line in matrix])


if __name__ == "__main__":
    parsed = parse_input()
    part_1(parsed)
    part_2(parsed)  # JZPJRAGJ
