from collections import deque

from output import ints, D


def solve(data):
    grid = [tuple(ints(line)[::-1]) for line in data.splitlines()]
    sample_size = 1024
    H = 71
    W = 71
    E = H - 1, W - 1
    p1 = None
    p2 = None
    FIRST_BLOCKED = 2974
    for sample_size in [1024, FIRST_BLOCKED]:
        answer = None
        Q = deque([(0, 0, 0)])
        seen = set()
        while Q:
            y, x, w = Q.popleft()
            if (y, x) in seen:
                continue
            seen.add((y, x))
            if (y, x) == E:
                answer = w
            for dy, dx in D:
                if not (0 <= y + dy < H and 0 <= x + dx < W):
                    continue
                if (y + dy, x + dx) in grid[:sample_size]:
                    continue
                Q.append((y + dy, x + dx, w + 1))
        if not answer:
            r, c = grid[sample_size - 1]
            p2 = f"{c},{r}"
        else:
            p1 = answer
    return p1, p2


if __name__ == "__main__":
    import os

    # use dummy data
    inp = """
    5,4
    4,2
    4,5
    3,0
    2,1
    6,3
    2,4
    1,5
    0,6
    3,3
    2,6
    5,1
    1,2
    5,5
    2,5
    6,5
    1,4
    0,4
    6,4
    1,1
    6,1
    1,0
    0,5
    1,6
    2,0
    """.strip()

    # uncomment to instead use stdin
    # import sys; inp = sys.stdin.read().strip()

    # uncomment to use AoC provided puzzle input
    with open("./input/18.txt", "r") as f:
        inp = f.read().strip()

    # uncomment to do initial data processing shared by part 1-2
    p1, p2 = solve(inp)

    print(p1)
    os.system(f"echo {p1} | wl-copy")
    print(p2)
    os.system(f"echo {p2} | wl-copy")

    # uncomment and replace 0 with actual output to refactor code
    # and ensure nonbreaking changes
    # assert p1 == 0
    # assert p2 == 0
