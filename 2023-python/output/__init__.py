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


def answer(part_index, fmt_string):
    """Decorator to present a solution in a human readable format"""

    def decorator_aoc(func):
        @functools.wraps(func)
        def wrapper_aoc(*args, **kwargs):
            decorate = kwargs.get("decorate", False)
            if decorate:
                del kwargs["decorate"]
            answer = func(*args, **kwargs)
            if not decorate:
                print(answer)
            else:
                formatted = fmt_string.format(answer)
                print(f" {part_index}) {formatted}")
            return answer

        return wrapper_aoc

    return decorator_aoc


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


# https://pieriantraining.com/understanding-dijkstras-algorithm-in-python/
def dijkstra_algorithm(graph, start_node):
    def min_distance(distances, visited):
        min_val = float("inf")
        min_index = -1

        for i in range(len(distances)):
            if distances[i] < min_val and i not in visited:
                min_val = distances[i]
                min_index = i

        return min_index

    num_nodes = len(graph)

    distances = [float("inf")] * num_nodes
    visited = []

    distances[start_node] = 0

    for i in range(num_nodes):
        current_node = min_distance(distances, visited)

        visited.append(current_node)

        for j in range(num_nodes):
            if graph[current_node][j] != 0:

                new_distance = distances[current_node] + graph[current_node][j]

                if new_distance < distances[j]:
                    distances[j] = new_distance
    return distances
