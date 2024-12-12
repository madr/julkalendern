from itertools import permutations

from output import ints


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
        if used == 0:
            empty = (y1, x1)
    p1 = len(viable)
    S, E = (0, W), (0, 0)
    # dagrid(grid, H + 1, W + 1)
    y, x = empty
    p2 = x + y + W + (W - 1) * 5
    return p1, p2


def dagrid(grid, H, W):
    """Used to print the grid to be solved by hand."""
    for r in range(H):
        for c in range(W):
            u, a = grid[(r, c)]
            print(f"{u}/{a}".rjust(8), end="")
        print("\n")


if __name__ == "__main__":
    with open("./input/22.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
