def solve(data):
    cols = len(data)
    prevrow = [t == "." for t in data]
    p1 = sum(prevrow) + sum(
        sum(prevrow := [issafe(prevrow, i) for i in range(cols)]) for _ in range(39)
    )
    p2 = p1 + sum(
        sum(prevrow := [issafe(prevrow, i) for i in range(cols)])
        for _ in range(400_000 - 40)
    )
    return p1, p2


def issafe(row, i):
    match i:
        case 0:
            return row[1]
        case n if n == len(row) - 1:
            return row[-2]
        case _:
            lt, rt = row[i - 1], row[i + 1]
            return not lt != rt


if __name__ == "__main__":
    with open("./input/18.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
