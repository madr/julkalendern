from collections import deque
from output import answer

n = 10
title = "Pipe Maze"


D = (-1, 0), (0, 1), (1, 0), (0, -1)

C = {
    (-1, 0): ["|", "7", "F"],
    (0, 1): ["-", "7", "J"],
    (1, 0): ["|", "L", "J"],
    (0, -1): ["-", "L", "F"],
}

A = {
    "S": [0, 1, 2, 3],
    "-": [1, 3],
    "|": [0, 2],
    "F": [1, 2],
    "L": [0, 1],
    "7": [2, 3],
    "J": [0, 3],
}


@answer(1, "Farthest away pipe is at {}")
def part_1(presolved):
    return presolved[0]


@answer(2, "{} spots are encapsulated by pipes")
def part_2(presolved):
    return presolved[1]


def presolve(data):
    matrix = data.split()
    w = len(matrix[0])
    h = len(matrix)
    q = deque()
    visited = set()

    for r in range(h):
        if "S" in matrix[r]:
            start = (r, matrix[r].index("S"))
            q.append(start)
            break

    while q:
        o = q.popleft()
        visited.add(o)
        for di in A[matrix[o[0]][o[1]]]:
            d = D[di]
            r = o[0] + d[0]
            c = o[1] + d[1]
            if r >= 0 and r < h and c >= 0 and c < w:
                t = matrix[r][c]
                p = (r, c)
                if p not in visited and t != "." and t in C[d]:
                    q.append(p)
    p1 = len(visited) // 2

    p2 = 0
    for y in range(h):
        for x in range(w):
            if (y, x) in visited:
                continue
            crosses = 0
            y2, x2 = y, x
            while y2 < h and x2 < w:
                c2 = matrix[y2][x2]
                if (y2, x2) in visited and c2 not in "L7":
                    crosses += 1
                x2 += 1
                y2 += 1
            if crosses % 2 == 1:
                p2 += 1

    return p1, p2


if __name__ == "__main__":
    with open("./input/10.txt", "r") as f:
        inp = f.read()

    inp = presolve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 6846
    assert b == 325
