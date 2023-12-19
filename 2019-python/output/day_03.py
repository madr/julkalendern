from collections import defaultdict

from output import answer

n = 3
title = "Crossed Wires"

directions = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
}


@answer(
    1, "As the crow flies, closest intersection Manhattan distance is {} units away"
)
def part_1(o):
    return o[0]


@answer(2, "By travel, closest intersection Manhattan distance is {} units away")
def part_2(o):
    return o[1]


def solve(inp):
    wires = [line.split(",") for line in inp.split()]
    seen = defaultdict(dict)

    def follow(instructions, i):
        visited = []
        steps = 0
        pos = (0, 0)
        for instruction in instructions:
            urdl, *l = instruction
            distance = int("".join(l))
            for _ in range(distance):
                steps += 1
                pos = (pos[0] + directions[urdl][0], pos[1] + directions[urdl][1])
                visited.append(pos)
                if i not in seen[pos]:
                    seen[pos][i] = steps
        return set(visited)

    p1w = []
    for i, wire in enumerate(wires):
        p1w.append(follow(wire, i))
    p1 = min(sum(map(abs, i)) for i in p1w[0] & p1w[1])

    p2 = min(sum(v.values()) for v in seen.values() if len(v) > 1)

    return p1, p2


if __name__ == "__main__":
    with open("./input/03.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 1337
    assert b == 65356
