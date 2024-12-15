import functools
import re

# Directions/Adjacents for 2D matrices, in the order UP, RIGHT, DOWN, LEFT
D = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

Di = [
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
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


def cw(y, x):
    """Flip a (y, x) direction counterwise: U->R, R->D, D->L, L->U.

    >>> cw(-1, 0)
    (0, 1)
    >>> cw(0, 1)
    (1, 0)
    >>> cw(1, 0)
    (0, -1)
    >>> cw(0, -1)
    (-1, 0)
    """
    return (x, y) if y == 0 else (x, -y)


def ccw(y, x):
    """Flip a (y, x) direction counterwise: U->L, L->D, D->R, R->U.

    >>> ccw(-1, 0)
    (0, -1)
    >>> ccw(0, -1)
    (1, 0)
    >>> ccw(1, 0)
    (0, 1)
    >>> ccw(0, 1)
    (-1, 0)
    """
    return (x, y) if x == 0 else (-x, y)


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


def dijkstras(grid, start, target):
    """
    1. Create an array that holds the distance of each vertex from the starting
       vertex. Initially, set this distance to infinity for all vertices except
       the starting vertex which should be set to 0.
    2. Create a priority queue (heap) and insert the starting vertex with its
       distance of 0.
    3. While there are still vertices left in the priority queue, select the vertex
       with the smallest recorded distance from the starting vertex and visit its
       neighboring vertices.
    4. For each neighboring vertex, check if it is visited already or not. If it
       isn’t visited yet, calculate its tentative distance by adding its weight
       to the smallest distance found so far for its parent/previous node
       (starting vertex in case of first-level vertices).
    5. If this tentative distance is smaller than previously recorded value
       (if any), update it in our ‘distances’ array.
    6. Finally, add this visited vertex with its updated distance to our priority
       queue and repeat step-3 until we have reached our destination or exhausted
       all nodes.
    """
    import heapq

    target = max(grid)
    seen = set()
    queue = [(start, 0)]
    while queue:
        cost, pos, direction, steps = heapq.heappop(queue)
        y, x = pos
        dy, dx = direction

        if pos == target:
            return cost

        if ((pos, "and stuff")) in seen:
            continue

        seen.add((pos, "and stuff"))

        neighbors = []
        for n in neighbors:
            heapq.heappush(queue, ("stuffs"))

    return -1
