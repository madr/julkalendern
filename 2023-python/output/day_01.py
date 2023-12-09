import re
from output import answer

n = 1
title = "Trebuchet?!"


@answer(1, "Calibration values sum: {}, excluding spelled out digits")
def part_1(data):
    def value(s):
        s = [int(c) for c in s if c.isdigit()]
        return s[0] * 10 + s[-1]

    return sum(value(line) for line in data.split())


@answer(2, "Calibration values sum: {}, including spelled out digits")
def part_2(data):
    mp = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    def value(l):
        s = [
            int(c) if c.isdigit() else mp[c]
            for c in re.findall(
                r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", l
            )
        ]
        return s[0] * 10 + s[-1]

    return sum(value(line) for line in data.split())


if __name__ == "__main__":
    with open(f"./input/01.txt", "r") as f:
        inp = f.read().strip()

    a = part_1(inp)
    b = part_2(inp)

    assert a == 54634
    assert b == 53855
