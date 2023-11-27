import sys

year = 2019

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
from output import answer, puzzleinput

n = {day_no}
title = "{name}"


@puzzleinput(n)
def parse_input(data):
    return data


@answer(1, "Answer is {{}}")
def part_1(data):
    return data


@answer(2, "Actually, answer is {{}}")
def part_2(data):
    return data


if __name__ == "__main__":
    # use dummy data
    parsed = \"\"\"
        replace me
    \"\"\".strip()

    # uncomment to instead use stdin
    # import fileinput
    # parsed = "\\n".join(list(fileinput.input()))

    # uncomment to instead use content of input/{padded_no}.txt
    # parsed = parse_input()

    part_1(parsed)
    # part_2(parsed)
""".strip()
            + "\n"
        )
    print(f"- creating empty input/{day_no.zfill(2)}.txt")
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

from output import headline

stars = 0
for i in [str(n).zfill(2) for n in range(1, 26)]:
    try:
        day = __import__(
            "output.day_{}".format(i),
            globals(),
            locals(),
            ["n", "title", "part_1", "part_2", "parse_input"],
            0,
        )
        headline(day.n, day.title)
        data = day.parse_input()
        day.part_1(data, decorate=True)
        stars += 1
        day.part_2(data, decorate=True)
        stars += 1
    except IOError:
        pass
    except ImportError:
        pass
print(f"\nStars: {stars}")
print("".join("*" if n <= stars else "•" for n in range(50)))
print("")
