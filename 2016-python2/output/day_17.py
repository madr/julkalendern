from collections import deque
from hashlib import md5

from output import DD


def solve(data):
    paths = list(bfs(data))
    p1 = "".join(paths[0])
    p2 = len(paths[-1])
    return p1, p2


def bfs(code):
    q = deque([((0, 0), [])])
    T = (3, 3)
    K = "UDLR"
    while q:
        m, d = q.popleft()
        U, D, L, R, *_ = md5((code + "".join(d)).encode()).hexdigest()
        y, x = m
        for udlr in [K[k] for k, n in enumerate([U, D, L, R]) if isopen(n)]:
            dy, dx = DD[udlr]
            if (y + dy, x + dx) == T:
                yield d + [udlr]
            elif 0 <= y + dy < 4 and 0 <= x + dx < 4:
                q.append(((y + dy, x + dx), d + [udlr]))


def isopen(c):
    return c in "bcdef"


if __name__ == "__main__":
    with open("./input/17.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
