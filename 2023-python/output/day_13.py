from output import answer

n = 13
title = "Point of Incidence"


@answer(1, "Summarizing the notes gives {}")
def part_1(presolved):
    return presolved[0]


@answer(2, "Summarizing the notes allowing off-by-1 gives {}")
def part_2(presolved):
    return presolved[1]


def presolve(data):
    g = [l.split() for l in data.split("\n\n")]

    p1 = sum(d * n for d, n in _inspect(g))
    p2 = sum(d * n for d, n in _inspect(g, 1))

    return p1, p2


def _inspect(g, a=0):
    af = []
    for m in g:
        for d, n in [(100, m), (1, tuple(zip(*m)))]:
            af.append((d, _compare(n, a)))
    return af


def _compare(l, a=0):
    for i in range(1, len(l)):
        if (
            sum(
                sum(a != b for a, b in zip(x, y)) for x, y in zip(l[i - 1 :: -1], l[i:])
            )
            == a
        ):
            return i
    return 0


if __name__ == "__main__":
    with open("./input/13.txt", "r") as f:
        inp = f.read().strip()

    inp = presolve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 29213
    assert b == 37453
