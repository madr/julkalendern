import sys
from pathlib import Path


def headline(n, title):
    """Print day number and name, followed by a ruler. Used by the answer decorator"""
    print(f"\n--- Day {n}: {title} ---\n")


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
from output import answer  # , matrix, D, DD, ADJ, ints, mhd, mdbg, vdbg

n = {day_no}
title = "{name}"


@answer(1, "Answer is {{}}")
def part_1(presolved):
    return presolved[0]


@answer(2, "Actually, answer is {{}}")
def part_2(presolved):
    return presolved[1]


def solve(data):
    return 1, 2


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
    inp = solve(inp)

    a = part_1(inp)
    # b = part_2(inp)

    # uncomment and replace 0 with actual output to refactor code
    # and ensure nonbreaking changes
    # assert a == 0
    # assert b == 0
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
                ["n", "title", "part_1", "part_2"],
                0,
            )
            with open(f"./input/{i}.txt", "r") as f:
                data = f.read().strip()
            headline(day.n, day.title)
            try:
                data = day.presolve(data)
            except AttributeError:
                pass
            try:
                data = day.solve(data)
            except AttributeError:
                pass
            if day.part_1(data, decorate=True):
                stars += 1
            if day.part_2(data, decorate=True):
                stars += 1
        except IOError:
            pass
        except ImportError:
            pass
if not day_no:
    print(f"\nStars: {stars}")
    print("".join("*" if n < stars else "•" for n in range(50)))
print("")
