from collections import defaultdict
from itertools import permutations

from output import answer
from output.intcode_computer import execute, parse

n = 7
title = "Amplification Circuit"


@answer(
    1,
    "[intcode 0.3.0] The highest achievable signal to the thruster is {}",
)
def part_1(o):
    return o[0]


@answer(
    2,
    "[intcode 0.3.0] By creating a feedback loop, the highest achievable signal to the thruster is {}",
)
def part_2(o):
    return o[0]


def solve(data):
    program = parse(data)

    thruster_signals = []
    for settings in map(list, permutations(range(5))):
        o = 0
        for ps in settings:
            _code, _state, _n, _rb, so = execute(program, stdin=[ps, o])
            o = so.pop(0)
        thruster_signals.append(o)
    p1 = max(thruster_signals)

    thruster_signals = []
    for settings in map(list, permutations(range(5, 10))):
        o = [0]
        finished = set()
        paused = defaultdict(tuple)
        while len(finished) < 5:
            for amp, ps in enumerate(settings):
                if paused[amp]:
                    program, resume_at = paused[amp]
                    del paused[amp]
                    code, state, n, _rb, so = execute(program, stdin=o, n=resume_at)
                else:
                    code, state, n, _rb, so = execute(program, stdin=[ps, *o])
                if code == 3:
                    paused[amp] = (
                        list(state.values()),
                        n,
                    )
                    o = so
                if code == 99:
                    finished.add(amp)
                    o = so
        thruster_signals.append(o[-1])
    p2 = max(thruster_signals)

    return p1, p2


if __name__ == "__main__":
    with open("./input/07.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 398674
    assert b == 39431233
