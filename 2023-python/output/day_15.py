from collections import OrderedDict, defaultdict

from output import answer

n = 16
title = "Lens Library"


@answer(1, "Sum of HASH algorithm results: {}")
def part_1(presolved):
    return presolved[0]


@answer(2, "Focusing power of the resulting configuration: {}")
def part_2(presolved):
    return presolved[1]


def presolve(data):
    def h(s):
        v = 0
        for a in s:
            if a == "\n":
                continue
            v += ord(a)
            v *= 17
            v = v % 256
        return v

    p1 = sum(h(c) for c in data.split(","))

    b = defaultdict(OrderedDict)
    for lr in data.split(","):
        if "=" in lr:
            l, r = lr.split("=")
            if r == "":
                continue
            k = h(l)
            b[k][l] = r
        if "-" in lr:
            l, _r = lr.split("-")
            k = h(l)
            if l in b[k]:
                del b[k][l]
    p2 = 0
    for i, c in b.items():
        for j, f in enumerate(b[i].values(), 1):
            p2 += (i + 1) * j * int(f)

    return p1, p2


if __name__ == "__main__":
    with open("./input/16.txt", "r") as f:
        inp = f.read().strip()

    inp = presolve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 509784
    assert b == 230197
