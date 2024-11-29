from output import answer  # , matrix, D, DD, ADJ, ints, mhd, mdbg, vdbg

n = 16
title = "Dragon Checksum"


@answer(1, "The checksum to the state to fill first disc is {}")
def part_1(presolved):
    return presolved[0]


@answer(2, "The checksum to the state to fill second disc is {}")
def part_2(presolved):
    return presolved[1]


def solve(data):
    p12 = []
    for DS in [272, 35651584]:
        s = [int(c) for c in data]
        while len(s) < DS:
            b = [abs(int(c) - 1) for c in s[::-1]]
            s = s + [0] + b
        s = s[:DS]
        p = len(s)
        while p % 2 == 0:
            s = [int(a == b) for a, b in zip(s[::2], s[1::2])]
            p = len(s)
        p12.append("".join(map(str, s)))
    return p12


if __name__ == "__main__":
    with open("./input/16.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == "10011010010010010"
    assert b == "10101011110100011"
