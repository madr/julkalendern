from collections import Counter
from textwrap import wrap
from output import answer, puzzleinput

n = 8
title = "Space Image Format"


@puzzleinput(n)
def parse_input(data):
    return data


@answer(1, "The product of all 1s and 2s in the layer with fewest 0s is {}")
def part_1(data):
    layers = sorted(map(Counter, wrap(data, 25 * 6)), key=lambda c: c["0"])
    a = layers[0]["1"]
    b = layers[0]["2"]
    return a * b


@answer(2, "The message is CYUAH, the decoded image looks like this:\n\n{}")
def part_2(data, width=25, height=6):
    layers = wrap(data, width * height)
    l = len(layers)
    pixels = zip(*layers)
    lit = map(
        lambda s: s.replace("0", ".").replace("1", "#"),
        map(lambda p: next(filter(lambda x: x != "2", p)), pixels),
    )
    matrix = "\n".join(wrap("".join(lit), width))
    return matrix


if __name__ == "__main__":
    parsed = parse_input()
    part_1(parsed)
    part_2(parsed)
