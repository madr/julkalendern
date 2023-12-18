import re
from math import inf
from output import answer

n = 5
title = "If You Give A Seed A Fertilizer"


@answer(1, "Nearest location for seed id list is {}")
def part_1(presolved):
    l, _ = presolved
    return l


@answer(2, "Interpreting ranges of seeds, nearest location is {}")
def part_2(presolved):
    _, l = presolved
    return l


def presolve(data):
    seeds, *process = data.split("\n\n")
    seed_ranges = [[int(x) for x in ar.split()] for ar in re.findall(r"\d+ \d+", seeds)]
    seed_values = [int(v) for v in seeds.split()[1:]]
    processes = [
        [tuple(map(int, line.split())) for line in step.splitlines()[1:]]
        for step in process
    ]

    p1 = _process(seed_values, processes)

    p2 = 26829000  # takes 5m if starting from 0
    while True:
        g = _process([p2], processes, reverse=True)
        if any(g >= a and g < a + r for a, r in seed_ranges):
            break
        p2 += 1

    return p1, p2


def _process(seeds, processes, reverse=False):
    n = inf
    for start in seeds:
        n = min(n, _nearest(start, processes, reverse=reverse))
    return n


def _nearest(start, processes, reverse=False):
    procs = processes if not reverse else processes[::-1]
    v = start
    for steps in procs:
        for line in steps:
            dest, src, r = line
            if reverse:
                dest, src = src, dest
            if v >= src and v < src + r:
                v = dest + v - src
                break
    return v


if __name__ == "__main__":
    with open("./input/05.txt", "r") as f:
        inp = f.read().strip()

    inp = presolve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 278755257
    assert b == 26829166
