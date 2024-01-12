from collections import defaultdict

from output import answer

n = 6
title = "Universal Orbit Map"


@answer(1, "{} direct and indirect orbits")
def part_1(o):
    return o[0]


@answer(2, "Orbit transfers needed for you to share orbit with Santa: {}")
def part_2(o):
    return o[1]


def solve(data):
    heritage = defaultdict(str)
    for parent, child in [line.split(")") for line in data.split()]:
        heritage[child] = parent

    p1 = sum(len(ancestry(heritage, v)) for v in heritage.keys())

    a = ancestry(heritage, "YOU")
    b = ancestry(heritage, "SAN")
    shared = len(set(a) & set(b))
    p2 = sum(
        [
            len(a) - shared,
            len(b) - shared,
        ]
    )

    return p1, p2


def ancestry(parents, child):
    k = child
    lineage = []
    while k in parents:
        lineage.append(parents[k])
        k = parents[k]
    return lineage[::-1]


if __name__ == "__main__":
    with open("./input/06.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 271151
    assert b == 388
