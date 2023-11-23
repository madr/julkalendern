from output import answer, puzzleinput

from output.intcode_computer import execute

n = 5
title = "Sunny with a Chance of Asteroids"


@puzzleinput(n)
def parse_input(data):
    return list(map(int, data.split(",")))


@answer(1, "[intcode-0.2.0] Program diagnostic code, ID 1: {}")
def part_1(program):
    _, stdout = execute(program, stdin=1)
    return max(stdout)


@answer(2, "[intcode-0.2.1] Program diagnostic code, ID 5: {}")
def part_2(program):
    _, stdout = execute(program, stdin=5)
    return stdout[0]


if __name__ == "__main__":
    parsed = parse_input()
    part_1(parsed)
    part_2(parsed)
