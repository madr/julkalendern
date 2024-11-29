import re


def solve(data):
    M = [
        tuple(map(int, re.search(r"(\d+) pos.+ion (\d+)", r).groups()))
        for r in data.splitlines()
    ]
    p1 = wait_and_press(M)
    p2 = wait_and_press(M + [(11, 0)])
    return p1, p2


def wait_and_press(M):
    t = 0
    while True:
        if all((ti + lp[1]) % lp[0] == 0 for ti, lp in enumerate(M, start=t + 1)):
            break
        t += 1
    return t


if __name__ == "__main__":
    with open("./input/15.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
