from output import ints


def solve(data):
    lowest, highest = min(ints(data)), max(ints(data))
    data = [ints(line) for line in data.split()]
    p1 = float("inf")
    p2 = set()
    for a, b in data:
        X = a - 1
        Y = b + 1
        if X >= lowest:
            if not any(x <= X <= y for x, y in data):
                p1 = min(p1, X)
                p2.add(X)
        if Y <= highest:
            if not any(x <= Y <= y for x, y in data):
                p1 = min(p1, Y)
                p2.add(Y)
    p2 = len(p2)
    return p1, p2


if __name__ == "__main__":
    with open("./input/20.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
