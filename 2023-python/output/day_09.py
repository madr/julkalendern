from output import answer

n = 9
title = "Mirage Maintenance"


@answer(1, "OASIS report extrapolated values sum is {}")
def part_1(data):
    lines = [[int(d) for d in line.split()] for line in data.splitlines()]
    return _solve(lines)


@answer(2, "Using prepending, OASIS report extrapolated values sum is {}")
def part_2(data):
    lines = [[int(d) for d in line.split()[::-1]] for line in data.splitlines()]
    return _solve(lines)


def _solve(lines):
    vs = 0
    for l in lines:
        h = [l]
        while any(n != 0 for n in h[-1]):
            h.append([b - a for a, b in zip(h[-1], h[-1][1:])])
        h = h[::-1]
        for i in range(len(h)):
            h[i].append(0 if i == 0 else h[i - 1][-1] + h[i][-1])
        vs += h[-1][-1]
    return vs


if __name__ == "__main__":
    with open(f"./input/09.txt", "r") as f:
        inp = f.read().strip()

    a = part_1(inp)
    b = part_2(inp)

    assert a == 1702218515
    assert b == 925
