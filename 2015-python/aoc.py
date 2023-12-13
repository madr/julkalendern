import sys

year = 2015

try:
    _, day_no, name = sys.argv
except ValueError:
    day_no = None
    name = None

print(
    f"\nAdvent of Code {year}" "\n###################" "\n\nby Anders Englöf Ytterström"
)

if day_no and name:
    print(f"\n- creating solutions/day_{day_no.zfill(2)}.py")
    with open("solutions/day_{}.py".format(day_no.zfill(2)), "w") as s:
        s.write(
            """
from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "{day_no}.txt"

    def __str__(self):
        return "Day {day}: {name}"

    def solve(self, pi):
        return pi

    def solve_again(self, pi):
        return pi

    def parse_input(self, data):
        return data.strip()


if __name__ == "__main__":
    solution = Solution()
    # solution.show_results()

    dummy = \"\"\"
    replace me
    \"\"\".strip()

    solution.solve(dummy)
    # solution.solve_again(dummy)
""".strip().format(day=day_no, day_no=day_no.zfill(2), name=name)
            + "\n"
        )

    print(
        f"""
Done! start coding.

Puzzle link:
https://adventofcode.com/{year}/day/{day_no}

Puzzle input (copy and paste to inputs/{day_no.zfill(2)}.txt):
https://adventofcode.com/{year}/day/{day_no}/input
    """
    )
    exit(0)

for i in [str(n).zfill(2) for n in range(1, 26)]:
    try:
        solution = __import__(
            "solutions.day_{}".format(i), globals(), locals(), ["Solution"], 0
        ).Solution()
        solution.show_results()
    except IOError:
        pass
    except ImportError:
        pass
