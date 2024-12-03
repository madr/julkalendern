from collections import Counter
from textwrap import wrap

from output import answer

n = 8
title = "Space Image Format"


@answer(1, "The product of all 1s and 2s in the layer with fewest 0s is {}")
def part_1(o):
    return o[0]


@answer(2, "The message is {}, the decoded image looks like above")
def part_2(o):
    return o[1]


def solve(data):
    layers = sorted(map(Counter, wrap(data, 25 * 6)), key=lambda c: c["0"])
    width, height = 25, 6
    a = layers[0]["1"]
    b = layers[0]["2"]
    p1 = a * b

    layers = wrap(data, width * height)
    pixels = zip(*layers)
    lit = map(
        lambda s: s.replace("0", ".").replace("1", "#"),
        map(lambda p: next(filter(lambda x: x != "2", p)), pixels),
    )
    matrix = "\n".join(wrap("".join(lit), width))
    print(matrix)
    p2 = "CYUAH"

    return p1, p2


if __name__ == "__main__":
    with open("./input/08.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 2500
    assert b == "CYUAH"
