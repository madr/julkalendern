from output import answer
from output.intcode_computer import execute, parse

n = 13
title = "Care Package"


@answer(1, "When game exists, {} block tiles are on the screen")
def part_1(o):
    return o[0]


@answer(2, "Score when all blocks are broken: {}")
def part_2(o):
    return o[1]


def solve(data):
    program = parse(data)
    _code, _s, _n, _rb, outputs = execute(program)
    p1 = sum(outputs[i + 2] == 2 for i in range(0, len(outputs), 3))

    p2 = None

    return p1, p2


if __name__ == "__main__":
    with open("./input/13.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    # b = part_2(inp)

    assert a == 355
