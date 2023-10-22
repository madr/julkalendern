import unittest

from solutions.day_08 import Solution


class Day08TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            r"""
""
"abc"
"aaa\"aaa"
"\x27"
            """
        )

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 12

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 19


if __name__ == "__main__":
    unittest.main()
