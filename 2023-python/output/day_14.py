from output import answer

n = 14
title = "Parabolic Reflector Dish"


@answer(1, "Total initial load on the northern beams: {}")
def part_1(presolved):
    return presolved[0]


@answer(2, "After some humble load testing, the northern beam load is {}")
def part_2(presolved):
    return presolved[1]


BAEST = 1000_000_000


def presolve(data):
    m = [list(l) for l in data.split()]
    s = len(m[0])
    m1 = _tilt(m)

    p1 = sum(sum((s - w) * o.count("O") for o in r) for w, r in enumerate(m1))

    def impl(rc):
        return "".join(["".join(r) for r in rc])

    i = 0
    seen = []
    while True:
        i += 1
        for _ in range(4):
            m = _tilt(m)
            m = _rotate(m)
        im = impl(m)
        if im in seen:
            break
        else:
            seen.append(im)
    m2 = m
    c = seen.index(im) + 1
    for _ in range((BAEST - i) % (i - c)):
        for j in range(4):
            m2 = _tilt(m2)
            m2 = _rotate(m2)
    p2 = sum(sum((s - w) * o.count("O") for o in r) for w, r in enumerate(m2))
    return p1, p2


def _rotate(m):
    return [list(l) for l in zip(*m[::-1])]


def _tilt(m):
    m = [list(l) for l in zip(*m)]
    h = len(m[0])
    for c in m:
        u = True
        while u:
            u = False
            for i in range(h - 1):
                j = i + 1
                if c[i] == "#" or c[j] == "#":
                    continue
                if c[i] < c[j]:
                    c[j], c[i] = c[i], c[j]
                    u = True
    return [list(l) for l in zip(*m)]


if __name__ == "__main__":
    with open("./input/14.txt", "r") as f:
        inp = f.read().strip()

    inp = presolve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 109596
    assert b == 96105
