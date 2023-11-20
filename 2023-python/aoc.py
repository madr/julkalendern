from output import headline
import os
import sys

year = 2023

try:
    _, day_no, *name = sys.argv
except ValueError:
    day_no = None
    name = None

print(
    f"\nAdvent of Code {year}" "\n###################" "\n\nby Anders Englöf Ytterström"
)

if day_no and name:
    name = " ".join(name)
    padded_no = day_no.zfill(2)
    print(f"\n- creating output/day_{padded_no}.py")
    with open("output/day_{}.py".format(padded_no), "w") as s:
        s.write(
            f"""
from output import answer

n = {day_no}
title = "{name}"


@answer(1, "Answer is {{}}")
def part_1(data):
    return data


@answer(2, "Actually, answer is {{}}")
def part_2(data):
    return data


# uncomment to solve parts in one go
# def presolve(data):
#     return data


if __name__ == "__main__":
    # use dummy data
    inp = \"\"\"
        replace me
    \"\"\".strip()

    # uncomment to instead use stdin
    # import sys; inp = sys.stdin.read().strip()

    # uncomment to use AoC provided puzzle input
    # with open(f"./input/{padded_no}.txt", "r") as f:
    #     inp = f.read()

    # uncomment to do initial data processing shared by part 1-2
    # inp = presolve(inp)

    a = part_1(inp)
    # b = part_2(inp)

    # uncomment and replace 0 with actual output to refactor code
    # and ensure nonbreaking changes
    # assert a == 0
    # assert b == 0
""".strip()
            + "\n"
        )
    print(f"- creating empty input/{day_no.zfill(2)}.txt")
    if not os.path.exists("input"):
        os.makedirs("input")
    with open("input/{}.txt".format(day_no.zfill(2)), "w") as i:
        i.write("")

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
            filepath = f"./input/{str(n).zfill(2)}.txt"
            with open(filepath, "r") as f:
                data = f.read()
            headline(day.n, day.title)
            try:
                data = day.presolve(data)
            except:
                pass
            day.part_1(data, decorate=True)
            stars += 1
            day.part_2(data, decorate=True)
            stars += 1
        except IOError:
            pass
        except ImportError:
            pass
if not day_no:
    print(f"\nStars: {stars}")
    print("".join("*" if n < stars else "•" for n in range(50)))
print("")
