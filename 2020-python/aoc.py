import sys

year = 2020

try:
    _, day_no, name = sys.argv
except ValueError:
    day_no = None
    name = None

print(
    f"\nAdvent of Code {year}"
    "\n###################"
    "\n\nby Anders Ytterström (@madr_se)"
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

    def parse_input(self, data):
        return data

    def solve(self, puzzle_input):
        return True

    def solve_again(self, puzzle_input):
        return True


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
""".strip().format(
                day=day_no, day_no=day_no.zfill(2), name=name
            )
            + "\n"
        )
    print(f"- creating tests/test_day_{day_no.zfill(2)}.py")
    with open("tests/test_day_{}.py".format(day_no.zfill(2)), "w") as t:
        t.write(
            """
import unittest

from solutions.day_{day_no} import Solution


class Day{day_no}TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            \"\"\"
        <REPLACE ME>
        \"\"\"
        )

    def test_parse_puzzle_input(self):
        data = \"\"\"
        <REPLACE ME>
        \"\"\"
        assert self.solution.parse_input(data) == "<REPLACE ME>"

    # def test_solve_first_part(self):
    #     assert self.solution.solve(self.puzzle_input) == True

    # def test_solve_second_part(self):
    #     assert self.solution.solve_again(self.puzzle_input) == True


if __name__ == "__main__":
    unittest.main()
""".strip().format(
                day_no=day_no.zfill(2)
            )
            + "\n"
        )
    print(f"- creating empty inputs/{day_no.zfill(2)}.txt")
    with open("inputs/{}.txt".format(day_no.zfill(2)), "w") as i:
        i.write("")

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
