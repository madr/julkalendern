import re
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import chain, combinations, compress, permutations

from output import ADJ, DD, D, ccw, cw, ints, matrix, mdbg, mhd, vdbg


def solve(data):
    grid, H, W = matrix(data)
    S = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == "S"][0]
    E = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == "E"][0]
    p1 = float('inf')
    Q = deque([(0, (S,), 1)])
    seen = set()
    lowest = []
    while Q:
        cost, path, facing = heappop(Q)
        pos = path[-1]
        if (pos, facing) in seen:
            continue
        seen.add((pos, facing))
        if pos == E:
            p1 = min(cost, p1)
            lowest.append(path)
        r, c = pos
        for d, delta in enumerate(D):
            dr, dc = delta
            if grid[r + dr][c + dc] == "#":
                continue
            if abs(facing - d) == 2:
                continue
            if d != facing:
                heappush(Q, (cost + 1000, path, d))
            else:
                heappush(Q, (cost + 1, path + ((r + dr, c + dc),), d))
    return p1, None


if __name__ == "__main__":
    import os

    # use dummy data
    inp = """
    #################
    #...#...#...#..E#
    #.#.#.#.#.#.#.#.#
    #.#.#.#...#...#.#
    #.#.#.#.###.#.#.#
    #...#.#.#.....#.#
    #.#.#.#.#.#####.#
    #.#...#.#.#.....#
    #.#.#####.#.###.#
    #.#.#.......#...#
    #.#.###.#####.###
    #.#.#...#.....#.#
    #.#.#.#####.###.#
    #.#.#.........#.#
    #.#.#.#########.#
    #S#.............#
    #################



    """.strip()

    # uncomment to instead use stdin
    # import sys; inp = sys.stdin.read().strip()

    # uncomment to use AoC provided puzzle input
    with open("./input/16.txt", "r") as f:
        inp = f.read().strip()

    # uncomment to do initial data processing shared by part 1-2
    p1, p2 = solve(inp)

    print(p1)
    os.system(f"echo {p1} | wl-copy")
    print(p2)
    os.system(f"echo {p2} | wl-copy")

    # uncomment and replace 0 with actual output to refactor code
    # and ensure nonbreaking changes
    # assert p1 == 0
    # assert p2 == 0
