from collections import Counter

from output import answer

n = 4
title = "Secure Container"


@answer(1, "{} combinations of valid passwords")
def part_1(o):
    return o[0]


@answer(2, "{} combinations of valid passwords, including important detail")
def part_2(o):
    return o[1]


def solve(data):
    a, b = data.split("-")

    def v1(s):
        return "".join(sorted(s)) == s and any(x == y for x, y in zip(s, s[1:]))

    def v2(s):
        return "".join(sorted(s)) == s and 2 in Counter(s).values()

    p1 = sum(v1(str(pw)) for pw in range(int(a), int(b) + 1))
    p2 = sum(v2(str(pw)) for pw in range(int(a), int(b) + 1))

    return p1, p2


if __name__ == "__main__":
    with open("./input/04.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 544
    assert b == 334
