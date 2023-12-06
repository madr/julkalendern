from math import prod
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
    d = len(values) // 2
    races = list(
        map(
            lambda x: (int(x[0]), int(x[1])), list(zip(values[: d + 1], values[d:]))[1:]
        )
    )
    p1 = prod(
        sum(bpt * (time - bpt) > distance for bpt in range(time))
        for time, distance in races
    )
    time = int("".join(values[1:d]))
    distance = int("".join(values[d + 1 :]))
    p2 = prod([sum(bpt * (time - bpt) > distance for bpt in range(time))])
    return p1, p2


if __name__ == "__main__":
    inp = parse_input()

    inp = presolve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 1083852
    assert b == 23501589
