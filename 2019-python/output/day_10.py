from collections import OrderedDict, defaultdict, deque
from math import atan2

from output import answer

n = 10
title = "Monitoring Station"


@answer(1, "The monitor station will see {} asteroids at best")
def part_1(o):
    return o[0]


@answer(
    2,
    "The asteroid at y=3 x=17 (checksum {}) will be the 200th lazer vapored asteroid, making some elf happy",
)
def part_2(o):
    return o[1]


def solve(data):
    matrix = data.strip().split()
    pos, visible = _map_visible_asteroids(matrix)

    p1 = len(set(dict(visible).values()))

    targets_upper = defaultdict(list)
    targets_lower = defaultdict(list)
    targets = dict()

    for xy, angle in visible:
        if angle < 0:
            targets_lower[angle].append(xy)
        else:
            targets_upper[angle].append(xy)

    for k, v in OrderedDict(
        sorted(targets_upper.items(), key=lambda x: x[0], reverse=True)
        + sorted(targets_lower.items(), key=lambda x: x[0], reverse=True)
    ).items():
        targets[k] = deque(
            sorted(
                v,
                key=lambda xy: sum(abs(pos[i] - xy[i]) for i in range(2)),
            )
        )

    vapored = 0
    x = 0
    y = 0
    while vapored < 200:
        popped = False
        for tk in targets.keys():
            if targets[tk]:
                x, y = targets[tk].pop()
                vapored += 1
                popped = True
                if vapored == 200:
                    break
        if not popped:
            break

    p2 = x * 100 + y

    return p1, p2


def _map_visible_asteroids(matrix):
    asteroids = []
    visible = defaultdict(int)

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "#":
                asteroids.append((x, y))
    for a, b in asteroids:
        visible[(a, b)] = [
            ((x, y), atan2(x - a, y - b)) for x, y in asteroids if (a, b) != (x, y)
        ]

    return max(visible.items(), key=lambda x: len(set(dict(x[1]).values())))


if __name__ == "__main__":
    with open("./input/10.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 292
    assert b == 317
