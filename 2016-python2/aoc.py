import sys
from pathlib import Path


def headline(n):
    """Print day number and name, followed by a ruler. Used by the answer decorator"""
    print(f"\n--- Day {n} ---\n")


year = 2016

try:
    _, day_no, *name = sys.argv
except ValueError:
    day_no = None
    name = None

print(
    f"\nAdvent of Code {year}" "\n###################" "\n\nby Anders Englöf Ytterström"
)

Path("./input").mkdir(parents=True, exist_ok=True)
Path("./output").mkdir(parents=True, exist_ok=True)

if day_no and name:
    name = " ".join(name)
    padded_no = day_no.zfill(2)
    print(f"\n- creating output/day_{padded_no}.py")
    with open("output/day_{}.py".format(padded_no), "w") as s:
        s.write(
            f"""
import re
from collections import deque, Counter
from heapq import heappop, heappush
from itertools import compress, combinations, chain

from output import answer  # , matrix, D, DD, ADJ, ints, mhd, mdbg, vdbg


def solve(data):
    p1 = 1
    p2 = 2
    return p1, p2


if __name__ == "__main__":
    # use dummy data
    inp = \"\"\"
        replace me
    \"\"\".strip()

    # uncomment to instead use stdin
    # import sys; inp = sys.stdin.read().strip()

    # uncomment to use AoC provided puzzle input
    # with open("./input/{padded_no}.txt", "r") as f:
    #     inp = f.read().strip()

    # uncomment to do initial data processing shared by part 1-2
    p1, p2 = solve(inp)

    print(p1)
    # print(p2)

    # uncomment and replace 0 with actual output to refactor code
    # and ensure nonbreaking changes
    # assert p1 == 0
    # assert p2 == 0
""".strip()
            + "\n"
        )
    print(
        f"""
Done! start coding.

Puzzle link:
https://adventofcode.com/{year}/day/{day_no}

Puzzle input (copy and paste to input/{day_no.zfill(2)}.txt):
https://adventofcode.com/{year}/day/{day_no}/input
    """
    )
    exit(0)


stars = 0
for i in [str(n).zfill(2) for n in range(1, 26)]:
    if not day_no or day_no.zfill(2) == i:
        try:
            day = __import__(
                "output.day_{}".format(i),
                globals(),
                locals(),
                ["solve"],
                0,
            )
            with open(f"./input/{i}.txt", "r") as f:
                data = f.read().strip()
            headline(i)
            try:
                data = day.presolve(data)
            except AttributeError:
                pass
            try:
                p1, p2 = day.solve(data)
            except AttributeError:
                pass
            if p1:
                print(f"    1. {p1}")
                stars += 1
            if p2:
                print(f"    2. {p2}")
                stars += 1
        except IOError:
            pass
        except ImportError:
            pass
if not day_no:
    print(f"\nStars: {stars}")
    print("".join("*" if n < stars else "•" for n in range(50)))
print("")
