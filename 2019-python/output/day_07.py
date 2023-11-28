from collections import defaultdict
from itertools import permutations

from output import answer, puzzleinput
from output.intcode_computer import execute, parse

n = 7
title = "Amplification Circuit"


@puzzleinput(n)
def parse_input(data):
    return parse(data)


@answer(
    1,
    "[intcode 0.3.0] The highest achievable signal to the thruster is {}",
)
def part_1(program):
    thruster_signals = []
    for settings in map(list, permutations(range(5))):
        o = 0
        for ps in settings:
            _code, _state, _n, _rb, so = execute(program, stdin=[ps, o])
            o = so.pop(0)
        thruster_signals.append(o)
    return max(thruster_signals)


@answer(
    2,
    "[intcode 0.3.0] By creating a feedback loop, the highest achievable signal to the thruster is {}",
)
def part_2(program):
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
    return max(thruster_signals)


if __name__ == "__main__":
    parsed = parse_input()
    part_1(parsed)
    part_2(parsed)
