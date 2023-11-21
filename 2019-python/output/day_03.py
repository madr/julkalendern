from collections import defaultdict
from output import answer, puzzleinput

n = 3
title = "Crossed Wires"

directions = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
}


@puzzleinput(n)
def parse_input(data):
    return [line.split(",") for line in data.split()]


@answer(
    1, "As the crow flies, closest intersection Manhattan distance is {} units away"
)
def part_1(wires):
    def follow(instructions):
        seen = []
        pos = (0, 0)
        for instruction in instructions:
            urdl, *l = instruction
            distance = int("".join(l))
            for _ in range(distance):
                pos = (pos[0] + directions[urdl][0], pos[1] + directions[urdl][1])
                seen.append(pos)
        return set(seen)

    wa = follow(wires[0])
    wb = follow(wires[1])

    return min(sum(map(abs, i)) for i in wa & wb)


@answer(2, "By travel, closest intersection Manhattan distance is {} units away")
def part_2(wires):
    seen = defaultdict(dict)

    def follow(instructions, i):
        steps = 0
        pos = (0, 0)
        for instruction in instructions:
            urdl, *l = instruction
            distance = int("".join(l))
            for _ in range(distance):
                steps += 1
                pos = (pos[0] + directions[urdl][0], pos[1] + directions[urdl][1])
                if i not in seen[pos]:
                    seen[pos][i] = steps

    for i, wire in enumerate(wires):
        follow(wire, i)

    return min(sum(v.values()) for v in seen.values() if len(v) > 1)


if __name__ == "__main__":
    parsed = parse_input()
    part_1(parsed)
    part_2(parsed)
