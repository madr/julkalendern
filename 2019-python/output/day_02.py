from output import answer
from output.intcode_computer import execute, parse

n = 2
title = "1202 Program Alarm"


@answer(1, "[intcode-0.1.0] Value of pos 0 is {} at halt signal")
def part_1(o):
    return o[0]


@answer(2, "[intcode-0.1.1] 100 * noun + verb = {} for output 19690720")
def part_2(o):
    return o[1]


def solve(data):
    program = parse(data)

    program[1] = 12
    program[2] = 2
    _code, state, *_unused = execute(program)
    noun = 76  # found manually by binary search
    verb = 21
    p1 = state[0]

    program[1] = noun
    program[2] = verb
    _code, state, *_unused = execute(program)
    p2 = state[0]
    if state[0] == 19690720:
        p2 = 100 * noun + verb

    return p1, p2


if __name__ == "__main__":
    with open("./input/02.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 3306701
    assert b == 7621
