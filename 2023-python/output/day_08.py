import re
from math import lcm
from output import answer

n = 8
title = "Haunted Wasteland"


@answer(1, "One can reach Z in {} steps")
def part_1(presolved):
    steps, _ = presolved
    return steps


@answer(2, "Ghost path takes {} steps before all ghosts are at a Z positon")
def part_2(presolved):
    _, ghost_meet_point = presolved
    return ghost_meet_point


def presolve(data):
    d, els = data.split("\n\n")
    r = len(d)
    e = dict()
    for el in els.splitlines():
        k, *lr = re.match(r"(\w+) = \((\w+), (\w+)\)", el).groups()
        e[k] = lr

    p1 = 0
    pos = "AAA"
    while pos != "ZZZ":
        i = 0 if d[p1 % r] == "L" else 1
        pos = e[pos][i]
        p1 += 1

    p2 = 0
    z = list()
    for spos in [p for p in e.keys() if p.endswith("A")]:
        s = 0
        pos = spos
        while not pos.endswith("Z"):
            i = 0 if d[s % r] == "L" else 1
            pos = e[pos][i]
            s += 1
        z.append(s)
    p2 = lcm(*z)

    return p1, p2


if __name__ == "__main__":
    with open(f"./input/08.txt", "r") as f:
        inp = f.read().strip()

    inp = presolve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 17141
    assert b == 10818234074807
