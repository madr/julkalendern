from output import answer, puzzleinput
from collections import defaultdict

n = 2
title = "Cube Conundrum"


@answer(1, "Sum of all possible game IDs: {}")
def part_1(data):
    ids = []
    for id, game in enumerate(data.splitlines()):
        possible = True
        for round in game.split(";"):
            for cubes in round.split(","):
                if cubes.startswith("Game "):
                    _, cubes = cubes.split(": ")
                n, c = cubes.split()
                n = int(n)
                if c == "red" and n > 12:
                    possible = False
                    break
                if c == "green" and n > 13:
                    possible = False
                    break
                if c == "blue" and n > 14:
                    possible = False
                    break
        if possible:
            ids.append(id + 1)

    return sum(ids)


@answer(2, "Sum of all cube set powers: {}")
def part_2(data):
    powers = []
    for id, game in enumerate(data.splitlines()):
        seen = defaultdict(set)
        for round in game.split(";"):
            for cubes in round.split(","):
                if cubes.startswith("Game "):
                    _, cubes = cubes.split(": ")
                n, c = cubes.split()
                n = int(n)
                seen[c].add(n)
        powers.append(max(seen["blue"]) * max(seen["red"]) * max(seen["green"]))

    return sum(powers)


@puzzleinput(n)
def parse_input(data):
    return data


if __name__ == "__main__":
    parsed = parse_input()

    a = part_1(parsed)
    b = part_2(parsed)

    assert a == 2439
    assert b == 63711
