from collections import Counter
from math import inf

from output import D, answer  # , matrix, D, DD, ADJ, ints, mhd, mdbg, vdbg

n = 13
title = "A Maze of Twisty Little Cubicles"


@answer(1, "Fewest number of steps required to reach (31, 39) are {}")
def part_1(presolved):
    return presolved[0]


@answer(2, "{} distinct locations can be reached by traversing at most 50 steps")
def part_2(presolved):
    return presolved[1]


def solve(data, E=(31, 39)):
    S = (1, 1)
    p1, p2 = bfs(S, E, int(data), inf, 0)
    return p1, p2


def bfs(S, E, z, p1, p2):
    seen = set()
    q = [(S, 0)]
    while q:
        m, w = q.pop(0)
        if m in seen:
            continue
        seen.add(m)

        if m == E:
            p1 = min(w, p1)
        if w <= 50:
            p2 = max(p2, len(seen))

        x, y = m
        g = [
            (x, y)
            for x, y in [(x + c, y + r) for r, c in D]
            if x >= 0 and y >= 0 and valid(x, y, z)
        ]

        for s in g:
            q.append((s, w + 1))
    return p1, p2


def valid(x, y, z):
    n = (x * x + 3 * x + 2 * x * y + y + y * y) + z
    s = Counter(f"{n:b}")["1"]
    return s % 2 == 0


if __name__ == "__main__":
    with open(f"./input/{n}.txt", "r") as f:
        inp = f.read().strip()

    t, _ = solve("10", (7, 4))
    assert t == 11

    ab = solve(inp)

    a = part_1(ab)
    b = part_2(ab)

    assert a == 90
    assert b == 135
