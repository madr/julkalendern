from collections import deque


def solve(data):
    elfes = int(data)
    p1 = left_adjacent_rule(elfes)
    p1b = mathematical_superiority(elfes)
    p2 = opposite_side_rule(elfes)
    assert p1 == p1b
    return p1, p2


def mathematical_superiority(num_elfes):
    # Josephus' problem, quick method:
    # https://www.youtube.com/watch?v=uCsD3ZGzMgE
    b = format(num_elfes, "b")
    return int(b[1:] + b[0], 2)


def left_adjacent_rule(num_elfes):
    # https://en.wikipedia.org/wiki/Josephus_problem
    q = deque(list(range(1, num_elfes + 1)))
    while len(q) > 1:
        q.rotate(-1)
        q.popleft()
    return q.pop()


def opposite_side_rule(num_elfes):
    elfes = list(range(1, num_elfes + 1))
    separator = num_elfes // 2
    L, R = deque(elfes[:separator]), deque(elfes[separator:])

    while L and R:
        R.popleft()
        l2r = L.popleft()
        R.append(l2r)
        if len(R) - len(L) != 1:
            r2l = R.popleft()
            L.append(r2l)

    return R.pop()


if __name__ == "__main__":
    with open("./input/19.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
