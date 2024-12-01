from heapq import heappop, heappush

from output import answer  # D, DD, ADJ, ints, mhd, mdbg, vdbg

n = 17
title = "Clumsy Crucible"


@answer(1, "Using std crucible, least heat loss incured: {}")
def part_1(presolved):
    return presolved[0]


@answer(2, "Using ultra crucible, least heat loss incured: {}")
def part_2(presolved):
    return presolved[1]


def solve(data):
    grid = {
        (r, c): int(col)
        for r, row in enumerate(data.split())
        for c, col in enumerate(row)
    }
    p1 = least_heat_loss(grid, 1, 3)
    p2 = least_heat_loss(grid, 4, 10)
    return p1, p2


def least_heat_loss(grid, minsteps, maxsteps):
    target = max(grid)
    seen = set()
    queue = [(0, (0, 0), (0, 1), 0)]
    while queue:
        cost, pos, direction, steps = heappop(queue)
        y, x = pos
        dy, dx = direction

        if pos == target:
            return cost

        if ((pos, direction, steps)) in seen:
            continue

        seen.add((pos, direction, steps))

        if steps >= minsteps:
            cwdy, cwdx = clockwise(*direction)
            if (cw := (y + cwdy, x + cwdx)) in grid:
                cwy, cwx = cw
                heappush(queue, (cost + grid[cw], (cwy, cwx), (cwdy, cwdx), 1))

            ccwdy, ccwdx = counterclockwise(*direction)
            if (ccw := (y + ccwdy, x + ccwdx)) in grid:
                ccwy, ccwx = ccw
                heappush(queue, (cost + grid[ccw], (ccwy, ccwx), (ccwdy, ccwdx), 1))

        if steps < maxsteps and (fwd := (y + dy, x + dx)) in grid:
            fwdy, fwdx = fwd
            heappush(queue, (cost + grid[fwd], (fwdy, fwdx), direction, steps + 1))

    return -1


def clockwise(y, x):
    """
    >>> clockwise(-1, 0)
    (0, 1)
    >>> clockwise(0, 1)
    (1, 0)
    >>> clockwise(1, 0)
    (0, -1)
    >>> clockwise(0, -1)
    (-1, 0)
    """
    return (x, y) if y == 0 else (x, -y)


def counterclockwise(y, x):
    """
    >>> counterclockwise(-1, 0)
    (0, -1)
    >>> counterclockwise(0, -1)
    (1, 0)
    >>> counterclockwise(1, 0)
    (0, 1)
    >>> counterclockwise(0, 1)
    (-1, 0)
    """
    return (x, y) if x == 0 else (-x, y)


if __name__ == "__main__":
    with open("./input/17.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)
