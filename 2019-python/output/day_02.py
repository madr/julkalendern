from output import answer, puzzleinput
from collections import defaultdict

n = 2
title = "1202 Program Alarm"


@puzzleinput(n)
def parse_input(data):
    return list(map(int, data.split(",")))


@answer(1, "Value of pos 0 is {} at halt signal")
def part_1(program):
    state = dict(zip(range(len(program)), program))
    state[1] = 12
    state[2] = 2

    for i in range(0, len(state), 4):
        opcode, *args = list(state.values())[i : i + 4]
        if opcode == 1:
            a, b, p = args
            state[p] = state[a] + state[b]
        if opcode == 2:
            a, b, p = args
            state[p] = state[a] * state[b]
        if opcode == 99:
            break
    return state[0]


@answer(2, "100 * noun + verb = {} for output 19690720")
def part_2(program, noun=76, verb=21):
    state = dict(zip(range(len(program)), program))
    state[1] = noun
    state[2] = verb

    for i in range(0, len(state), 4):
        opcode, *args = list(state.values())[i : i + 4]
        if opcode == 1:
            a, b, p = args
            state[p] = state[a] + state[b]
        if opcode == 2:
            a, b, p = args
            state[p] = state[a] * state[b]
        if opcode == 99:
            break
    if state[0] == 19690720:
        return 100 * noun + verb
    return state[0]


if __name__ == "__main__":
    parsed = parse_input()
    part_1(parsed)
    part_2(parsed, 76, 21)  # found manually by binary search
