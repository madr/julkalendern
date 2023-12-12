from functools import cache
from output import answer

n = 12
title = "Hot Springs"


@answer(1, "sum of all possible combinations is {}")
def part_1(presolved):
    return presolved[0]


@answer(2, "sum of all possible combinations is {} when unfolded")
def part_2(presolved):
    return presolved[1]


def presolve(data):
    lines = [
        (a, list(map(int, b.split(","))))
        for a, b in (line.split() for line in data.splitlines())
    ]
    p1 = sum(_inspect(a, tuple(b)) for a, b in lines)
    p2 = sum(_inspect("?".join([a] * 5), tuple(b * 5)) for a, b in lines)
    return p1, p2


@cache
def _inspect(s, cs):
    r = len(s)
    csl = len(cs)
    if r == 0:
        return 1 if csl == 0 else 0
    o, *f = s
    f = "".join(f)
    if o == ".":
        return _inspect(f, cs)
    if o == "?":
        return _inspect("." + f, cs) + _inspect("#" + f, cs)
    if not csl:
        return 0
    g = cs[0]
    if g > r or "." in s[0:g]:
        return 0
    elif csl > 1:
        if g + 1 > r or s[g] == "#":
            return 0
        else:
            return _inspect(s[g + 1 :], cs[1:])
    elif csl == 1:
        return _inspect(s[g:], ())


if __name__ == "__main__":
    with open("./input/12.txt", "r") as f:
        inp = f.read().strip()

    inp = presolve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 7118
    assert b == 7030194981795
