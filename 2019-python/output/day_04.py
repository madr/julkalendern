from collections import Counter
from output import answer, puzzleinput

n = 4
title = "Secure Container"


@puzzleinput(n)
def parse_input(data):
    return data.split("-")


@answer(1, "{} combinations of valid passwords")
def part_1(range_values):
    a, b = range_values

    def valid(s):
        return "".join(sorted(s)) == s and any(x == y for x, y in zip(s, s[1:]))

    return sum(valid(str(pw)) for pw in range(int(a), int(b) + 1))


@answer(2, "{} combinations of valid passwords, including important detail")
def part_2(range_values):
    a, b = range_values

    def valid(s):
        return "".join(sorted(s)) == s and 2 in Counter(s).values()

    return sum(valid(str(pw)) for pw in range(int(a), int(b) + 1))


if __name__ == "__main__":
    parsed = parse_input()
    part_1(parsed)
    part_2(parsed)
