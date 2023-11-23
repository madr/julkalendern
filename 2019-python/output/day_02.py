from output import answer, puzzleinput
from collections import defaultdict

from output.intcode_computer import execute

n = 2
title = "1202 Program Alarm"


@puzzleinput(n)
def parse_input(data):
    return list(map(int, data.split(",")))


@answer(1, "[intcode-0.1.0] Value of pos 0 is {} at halt signal")
def part_1(program):
    state, _ = execute(program, noun=12, verb=2)
    return state[0]


@answer(2, "[intcode-0.1.1] 100 * noun + verb = {} for output 19690720")
def part_2(program, noun=76, verb=21):
    state, _ = execute(program, noun, verb)
    if state[0] == 19690720:
        return 100 * noun + verb
    return state[0]


if __name__ == "__main__":
    parsed = parse_input()
    part_1(parsed)
    part_2(parsed, 76, 21)  # found manually by binary search
