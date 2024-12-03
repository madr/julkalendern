from output import answer

n = 1
title = "The Tyranny of the Rocket Equation"


@answer(1, "Total fuel requirements are {}")
def part_1(o):
    return o[0]


@answer(2, "Total fuel requirements are {} including fuel costs")
def part_2(o):
    return o[1]


def solve(data):
    lines = list(map(int, data.split()))
    p1 = sum(n // 3 - 2 for n in lines)
    p2 = 0
    for fuel in lines:
        rem = fuel
        while rem > 0:
            cost = rem // 3 - 2
            p2 += max(0, cost)
            rem = max(0, cost)
    return p1, p2


if __name__ == "__main__":
    with open("./input/01.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 3393938
    assert b == 5088037
