import re

from output import answer  # , matrix, D, DD, ADJ, ints, mhd, mdbg, vdbg

n = 15
title = "Timing is Everything"


@answer(1, "First time for capsule-giving button press is {}")
def part_1(presolved):
    return presolved[0]


@answer(2, "With the additional disc, first time for capsule-giving button press is {}")
def part_2(presolved):
    return presolved[1]


def solve(data):
    M = [
        tuple(map(int, re.search(r"(\d+) pos.+ion (\d+)", r).groups()))
        for r in data.splitlines()
    ]
    p1 = wait_and_press(M)
    p2 = wait_and_press(M + [(11, 0)])
    return p1, p2


def wait_and_press(M):
    t = 0
    while True:
        if all((ti + lp[1]) % lp[0] == 0 for ti, lp in enumerate(M, start=t + 1)):
            break
        t += 1
    return t


if __name__ == "__main__":
    inp = """
    Disc #1 has 5 positions; at time=0, it is at position 4.
    Disc #2 has 2 positions; at time=0, it is at position 1.
    """.strip()

    with open("./input/15.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 122318
    assert b == 3208583
