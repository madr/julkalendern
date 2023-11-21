from output import answer, puzzleinput

n = 1
title = "The Tyranny of the Rocket Equation"


@puzzleinput(n)
def parse_input(data):
    return list(map(int, data.split()))


@answer(1, "Total fuel requirements are {}")
def part_1(lines):
    return sum(n // 3 - 2 for n in lines)


@answer(2, "Total fuel requirements are {} including fuel costs")
def part_2(lines):
    s = 0
    for fuel in lines:
        rem = fuel
        while rem > 0:
            cost = rem // 3 - 2
            s += max(0, cost)
            rem = max(0, cost)
    return s


if __name__ == "__main__":
    parsed = parse_input()
    part_1(parsed)
    part_2(parsed)
