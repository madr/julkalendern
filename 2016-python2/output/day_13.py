from collections import Counter
from math import inf

from output import D


def solve(data, E=(31, 39)):
    S = (1, 1)
    p1, p2 = bfs(S, E, int(data), inf, 0)
    return p1, p2


def bfs(S, E, z, p1, p2):
    seen = set()
    q = [(S, 0)]
    while q:
        m, w = q.pop(0)
        if m in seen:
            continue
        seen.add(m)

        if m == E:
            p1 = min(w, p1)
        if w <= 50:
            p2 = max(p2, len(seen))

        x, y = m
        g = [
            (x, y)
            for x, y in [(x + c, y + r) for r, c in D]
            if x >= 0 and y >= 0 and valid(x, y, z)
        ]

        for s in g:
            q.append((s, w + 1))
    return p1, p2


def valid(x, y, z):
    n = (x * x + 3 * x + 2 * x * y + y + y * y) + z
    s = Counter(f"{n:b}")["1"]
    return s % 2 == 0


if __name__ == "__main__":
    with open("./input/13.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
