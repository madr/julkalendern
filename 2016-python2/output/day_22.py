import re
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import chain, combinations, compress, permutations

from output import ADJ, DD, D, ints, matrix, mdbg, mhd, vdbg


def solve(data):
    viable = set()
    W = 0
    H = 0
    grid = dict()
    for a, b in permutations([ints(line) for line in data.splitlines()[2:]], r=2):
        x1, y1, size, used, _avail, _pc = a
        x2, y2, _size, _used, avail, _pc = b
        H = max([y1, y2, H])
        W = max([x1, x2, W])
        grid[(y1, x1)] = (used, size)
        if 0 < used <= avail:
            viable.add(((y1, x1), (y2, x2)))
    p1 = len(viable)
    S, E = (0, W), (0, 0)
    H, W = H + 1, W + 1
    dagrid(grid, H, W)
    return p1, p2


def dagrid(grid, H, W):
    for r in range(H):
        for c in range(W):
            u, a = grid[(r, c)]
            print(f"{u}/{a}".rjust(8), end="")
        print("\n")


if __name__ == "__main__":
    # use dummy data
    inp = """
    sdsdsd
    Filesystem            Size  Used  Avail  Use%
    /dev/grid/node-x0-y0   10T    8T     2T   80%
    /dev/grid/node-x0-y1   11T    6T     5T   54%
    /dev/grid/node-x0-y2   32T   28T     4T   87%
    /dev/grid/node-x1-y0    9T    7T     2T   77%
    /dev/grid/node-x1-y1    8T    0T     8T    0%
    /dev/grid/node-x1-y2   11T    7T     4T   63%
    /dev/grid/node-x2-y0   10T    6T     4T   60%
    /dev/grid/node-x2-y1    9T    8T     1T   88%
    /dev/grid/node-x2-y2    9T    6T     3T   66%
    """.strip()

    # uncomment to instead use stdin
    # import sys; inp = sys.stdin.read().strip()

    # uncomment to use AoC provided puzzle input
    with open("./input/22.txt", "r") as f:
        inp = f.read().strip()

    # uncomment to do initial data processing shared by part 1-2
    p1, p2 = solve(inp)

    print(p1)
    print(p2)

    # uncomment and replace 0 with actual output to refactor code
    # and ensure nonbreaking changes
    # assert p1 == 0
    # assert p2 == 0
