import re
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import chain, combinations, compress, permutations

from output import ADJ, DD, D, ints, matrix, mdbg, mhd, vdbg


def solve(data):
    grid, H, W = matrix(data)
    dests = {
        v: (y, x) for y, r in enumerate(grid) for x, v in enumerate(r) if v.isdigit()
    }
    S0 = dests["0"]
    del dests["0"]
    p1 = travel(dests, grid, H, W, S0)
    p2 = travel(dests, grid, H, W, S0, goback=True)
    return p1, p2


def travel(dests, grid, H, W, S0, goback=False):
    shortest = float("inf")
    for goals in permutations(dests.items()):
        goals = list(goals)
        if goback:
            goals += [("0", S0)]
        t = 0
        S = S0
        for _, E in goals:
            seen = set()
            q = [(S, 0)]
            while q:
                pos, w = q.pop(0)
                if pos == E:
                    t += w
                    break
                if pos in seen:
                    continue
                seen.add(pos)
                y, x = pos
                for dy, dx in D:
                    if not (0 <= dy + y < H and 0 <= dx + x < W):
                        continue
                    if grid[dy + y][dx + x] != "#":
                        q.append(((dy + y, dx + x), w + 1))
            S = E
        shortest = min(shortest, t)
    return shortest


if __name__ == "__main__":
    with open("./input/24.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
