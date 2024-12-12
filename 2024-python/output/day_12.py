import re
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import chain, combinations, compress, permutations

from output import ADJ, DD, D, ccw, cw, ints, matrix, mdbg, mhd, vdbg


def solve(data):
    grid, H, W = matrix(data)
    p1 = 0
    seen = set()
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if (r, c) in seen:
                continue
            areas = 0
            perimeters = 0
            q = deque([(r, c)])
            while q:
                rc = q.popleft()
                if rc in seen:
                    continue
                seen.add(rc)
                areas += 1
                y, x = rc
                for dy, dx in D:
                    if (0 <= y + dy < H and 0 <= x + dx <W) and grid[y + dy][x + dx] == col:
                        q.append((y + dy, x + dx))
                    else:
                        perimeters += 1
            p1 += areas*perimeters
    p2 = None
    return p1, p2


if __name__ == "__main__":
    import os

    # use dummy data
    inp = """
    RRRRIICCFF
    RRRRIICCCF
    VVRRRCCFFF
    VVRCCCJFFF
    VVVVCJJCFE
    VVIVCCJJEE
    VVIIICJJEE
    MIIIIIJJEE
    MIIISIJEEE
    MMMISSJEEE
    """.strip()

    """
    A region of R plants with price 12 * 18 = 216.
    A region of I plants with price 4 * 8 = 32.
    A region of C plants with price 14 * 28 = 392.
    A region of F plants with price 10 * 18 = 180.
    A region of V plants with price 13 * 20 = 260.
    A region of J plants with price 11 * 20 = 220.
    A region of C plants with price 1 * 4 = 4.
    A region of E plants with price 13 * 18 = 234.
    A region of I plants with price 14 * 22 = 308.
    A region of M plants with price 5 * 12 = 60.
    A region of S plants with price 3 * 8 = 24.
    """

    # uncomment to instead use stdin
    # import sys; inp = sys.stdin.read().strip()

    # uncomment to use AoC provided puzzle input
    with open("./input/12.txt", "r") as f:
        inp = f.read().strip()

    # uncomment to do initial data processing shared by part 1-2
    p1, p2 = solve(inp)

    print(p1)
    os.system(f"echo {p1} | wl-copy")
    # print(p2)
    # os.system(f"echo {p2} | wl-copy")

    # uncomment and replace 0 with actual output to refactor code
    # and ensure nonbreaking changes
    assert p1 == 1446042
    # assert p2 == 0
