import re
from math import prod


def solve(data):
    needle = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    multiplications_sum = sum(
        prod(map(int, factors)) for factors in re.findall(needle, data)
    )
    enabled_multiplications_sum = sum(
        sum(prod(map(int, factors)) for factors in re.findall(needle, chunk))
        for chunk in data.split("do")
        if not chunk.startswith("n't")
    )
    return multiplications_sum, enabled_multiplications_sum


if __name__ == "__main__":
    with open("./input/03.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
