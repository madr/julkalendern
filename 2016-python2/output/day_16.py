def solve(data):
    p12 = []
    for DS in [272, 35651584]:
        s = [int(c) for c in data]
        while len(s) < DS:
            b = [abs(int(c) - 1) for c in s[::-1]]
            s = s + [0] + b
        s = s[:DS]
        p = len(s)
        while p % 2 == 0:
            s = [int(a == b) for a, b in zip(s[::2], s[1::2])]
            p = len(s)
        p12.append("".join(map(str, s)))
    return p12


if __name__ == "__main__":
    with open("./input/16.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
