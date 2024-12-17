from collections import deque
from heapq import heappop, heappush

from output import D, matrix


def solve(data):
    grid, H, W = matrix(data)
    S = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == "S"][0]
    E = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == "E"][0]
    Q = deque([(0, S, 1)])
    p1 = float("inf")
    SE = dict()
    ES = dict()
    seen = set()
    while Q:
        cost, pos, dir = heappop(Q)
        r, c = pos
        if grid[r][c] == "#":
            continue
        if (r, c, dir) in seen:
            continue
        seen.add((r, c, dir))
        if (r, c, dir) not in SE:
            SE[(r, c, dir)] = cost
        if pos == E:
            p1 = min(p1, cost)
            continue
        for inc, delta, facing in [
            (1, D[dir], dir),
            (1000, (0, 0), (dir + 1) % 4),
            (1000, (0, 0), (dir - 1) % 4),
        ]:
            nc = cost + inc
            dr, dc = delta
            heappush(Q, (nc, (r + dr, c + dc), facing))
    Q = deque([(0, E, 0), (0, E, 1), (0, E, 2), (0, E, 3)])
    seen = set()
    while Q:
        cost, pos, dir = heappop(Q)
        r, c = pos
        if grid[r][c] == "#":
            continue
        if (r, c, dir) in seen:
            continue
        seen.add((r, c, dir))
        if (r, c, (dir + 2) % 4) not in ES:
            ES[(r, c, (dir + 2) % 4)] = cost
        if pos == S:
            continue
        for inc, delta, facing in [
            (1, D[dir], dir),
            (1000, (0, 0), (dir + 1) % 4),
            (1000, (0, 0), (dir - 1) % 4),
        ]:
            nc = cost + inc
            dr, dc = delta
            heappush(Q, (nc, (r + dr, c + dc), facing))
    p2 = set()
    for r in range(H):
        for c in range(W):
            for d in range(4):
                if (
                    (r, c, d) in SE
                    and (r, c, d) in ES
                    and SE[(r, c, d)] + ES[(r, c, d)] == p1
                ):
                    p2.add((r, c))
    return p1, len(p2)


if __name__ == "__main__":
    with open("./input/16.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
