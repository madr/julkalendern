from output import answer
from output.intcode_computer import execute, parse

n = 5
title = "Sunny with a Chance of Asteroids"


@answer(1, "[intcode-0.2.0] Program diagnostic code, ID 1: {}")
def part_1(o):
    return o[0]


@answer(2, "[intcode-0.2.1] Program diagnostic code, ID 5: {}")
def part_2(o):
    return o[1]


def solve(data):
    program = parse(data)

    _code, _state, _cursorpos, rb, stdout = execute(program, stdin=[1])
    p1 = max(stdout)

    _code, _state, _cursorpos, rb, stdout = execute(program, stdin=[5])
    p2 = stdout[0]

    return p1, p2


if __name__ == "__main__":
    with open("./input/05.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 16434972
    assert b == 16694270
