from functools import cache
from collections import defaultdict


def solve(data):
    patterns, designs = data.split("\n\n")
    patterns = sorted(patterns.split(", "), key=lambda s: -len(s))
    designs = designs.split()

    hashed = defaultdict(list)
    for p in patterns:
        hashed[p[0]].append(p)
    hashed = tuple([(k, tuple(v)) for k, v in hashed.items()])

    possible = sum(ispossible(d, hashed) > 0 for d in designs)
    every_possibility = sum(ispossible(d, hashed) for d in designs)
    return possible, every_possibility


@cache
def ispossible(remaining, patterns):
    if not remaining:
        return 1
    selected = dict(patterns).get(remaining[0], [])
    return sum(
        ispossible(remaining.removeprefix(pattern), patterns)
        for pattern in selected
        if remaining.startswith(pattern)
    )


if __name__ == "__main__":
    with open("./input/19.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
