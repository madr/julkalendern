import re
from math import prod
from output import answer, puzzleinput
from collections import defaultdict

n = 2
title = "Cube Conundrum"


@answer(1, "Sum of all possible game IDs: {}")
def part_1(data):
    return sum(
        [
            id + 1
            for id, game in enumerate(data.splitlines())
            if not sum(
                any(
                    [
                        c == "red" and int(n) > 12,
                        c == "green" and int(n) > 13,
                        c == "blue" and int(n) > 14,
                    ]
                )
                for n, c in re.findall(r"(\d+) (\w+)", game)
            )
        ]
    )


@answer(2, "Sum of all cube set powers: {}")
def part_2(data):
    def power(game):
        seen = defaultdict(int)
        for n, c in re.findall(r"(\d+) (\w+)", game):
            seen[c] = max([seen[c], int(n)])
        return prod([seen["blue"], seen["red"], seen["green"]])

    return sum(power(game) for game in data.splitlines())


@puzzleinput(n)
def parse_input(data):
    return data


if __name__ == "__main__":
    parsed = parse_input()

    a = part_1(parsed)
    b = part_2(parsed)

    assert a == 2439
    assert b == 63711
