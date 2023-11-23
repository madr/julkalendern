from collections import defaultdict, deque
from output import answer, puzzleinput

n = 6
title = "Universal Orbit Map"


@puzzleinput(n)
def parse_input(data):
    heritage = defaultdict(str)
    for parent, child in [line.split(")") for line in data.split()]:
        heritage[child] = parent
    return heritage


@answer(1, "{} direct and indirect orbits")
def part_1(heritage):
    return sum(len(ancestry(heritage, v)) for v in heritage.keys())


@answer(2, "Orbit transfers needed for you to share orbit with Santa: {}")
def part_2(heritage):
    a = ancestry(heritage, "YOU")
    b = ancestry(heritage, "SAN")
    shared = len(set(a) & set(b))
    return sum(
        [
            len(a) - shared,
            len(b) - shared,
        ]
    )


def ancestry(parents, child):
    k = child
    lineage = []
    while k in parents:
        lineage.append(parents[k])
        k = parents[k]
    return lineage[::-1]


if __name__ == "__main__":
    parsed = parse_input()
    part_1(parsed)
    part_2(parsed)
