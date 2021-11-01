import unittest

from solutions.day_13 import Solution


class Day13TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        939
7,13,x,x,59,x,31,19
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        939
7,13,x,x,59,x,31,19
        """.strip()
        assert self.solution.parse_input(data) == (
            939,
            ["7", "13", "x", "x", "59", "x", "31", "19"],
        )

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 295

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input, 1068681) == 1068781
        assert self.solution.solve_again((939, [67, 7, 59, 61]), 700000) == 754018
        assert self.solution.solve_again((939, [17, "x", 13, 19]), 3000) == 3417
        assert (
            self.solution.solve_again((939, [67, 7, "x", 59, 61]), 1260470) == 1261476
        )
        assert (
            self.solution.solve_again((939, [1789, 37, 47, 1889]), 1202160480)
            == 1202161486
        )


if __name__ == "__main__":
    unittest.main()
