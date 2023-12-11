from itertools import combinations
from output import answer

n = 11
title = "Cosmic Expansion"


@answer(1, "Sum of all galaxy shortest distances is {}")
def part_1(data):
    return data[0]


@answer(2, "Exapanding by 1M, sum is {}")
def part_2(data):
    return data[1]


def presolve(data):
    m = data.splitlines()
    er = set()
    ec = set()
    for i, r in enumerate(m):
        if "#" not in r:
            er.add(i)
    for i, c in enumerate(zip(*m)):
        if "#" not in c:
            ec.add(i)
    h = len(m)
    w = len(m[0])
    g1 = []
    g2 = []
    e = 1e6
    for r in range(h):
        for c in range(w):
            if m[r][c] == "#":
                ro = len(er & set(range(r)))
                co = len(ec & set(range(c)))
                g1.append((r + ro, c + co))
                g2.append((ro * e + r - ro, co * e + c - co))
    p1 = sum(
        abs(rc1[0] - rc2[0]) + abs(rc1[1] - rc2[1]) for rc1, rc2 in combinations(g1, 2)
    )
    p2 = int(
        sum(
            abs(rc1[0] - rc2[0]) + abs(rc1[1] - rc2[1])
            for rc1, rc2 in combinations(g2, 2)
        )
    )

    return p1, p2


if __name__ == "__main__":
    with open("./input/11.txt", "r") as f:
        inp = f.read().strip()

    inp = presolve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 9370588
    assert b == 746207878188
