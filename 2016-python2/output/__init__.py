import functools
import re

# Directions/Adjacents for 2D matrices, in the order UP, RIGHT, DOWN, LEFT
D = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

# Directions for 2D matrices, as a dict with keys U, R, D, L
DD = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
}

# Adjacent relative positions including diagonals for 2D matrices, in the order NW, N, NE, W, E, SW, S, SE
ADJ = [
    (-1, -1),
    (-1, 0),
    (1, -1),
    (0, -1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
]


def ints(s):
    """Extract all integers from a string"""
    return [int(n) for n in re.findall(r"\d+", s)]


def mhd(a, b):
    """Calculates the Manhattan distance between 2 positions in the format (y, x) or (x, y)"""
    ar, ac = a
    br, bc = b
    return abs(ar - br) + abs(ac - bc)


def matrix(d):
    """Transform a string into an iterable matrix. Returns the matrix, row count and col count"""
    m = [tuple(r) for r in d.split()]
    return m, len(m), len(m[0])


def mdbg(m):
    """Print-debug a matrix"""
    for r in m:
        print("".join(r))


def vdbg(seen, h, w):
    """Print-debug visited positions of a matrix"""
    for r in range(h):
        print("".join(["#" if (r, c) in seen else "." for c in range(w)]))


def bfs(S, E=None):
    """BFS algorithm, equal weighted nodes"""
    seen = set()
    q = [(S, 0)]
    g = {}  # graph, required to be provided at some point
    while q:
        m, w = q.pop(0)
        if m in seen:
            continue
        seen.add(m)
        # investigate here
        for s in g[m]:
            q.append((s, w + 1))
    # return insights
