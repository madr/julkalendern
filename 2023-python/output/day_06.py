from math import prod, sqrt, ceil, floor
from output import answer, puzzleinput

n = 6
title = "Wait For It"


@answer(1, "The product of all record times for all races is {}")
def part_1(presolved):
    return presolved[0]


@answer(2, "The product of all record times for the single long race is {}")
def part_2(presolved):
    return presolved[1]


@puzzleinput(n)
def parse_input(data):
    return data


def presolve(data):
    values = data.split()
    l = len(values) // 2
    races = list(
        map(
            lambda x: (int(x[0]), int(x[1])), list(zip(values[: l + 1], values[l:]))[1:]
        )
    )
    p1 = prod(sum(bpt * (t - bpt) > d for bpt in range(t)) for t, d in races)
    t = int("".join(values[1:l]))
    d = int("".join(values[l + 1 :]))
    # quadratic formula:
    # https://en.wikipedia.org/wiki/Quadratic_formula
    l = ceil((-t + sqrt(t**2 - 4 * d)) / -2)
    h = floor((-t - sqrt(t**2 - 4 * d)) / -2)
    p2 = h - l + 1
    return p1, p2


if __name__ == "__main__":
    inp = parse_input()

    inp = presolve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 1083852
    assert b == 23501589
