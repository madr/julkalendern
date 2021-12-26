import unittest

from solutions.day_02 import Solution


class Day02TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        forward 5
down 5
forward 8
up 3
down 8
forward 2
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        forward 8
up 3
down 8
        """
        assert self.solution.parse_input(data) == [(0, 8), (-3, 0), (8, 0)]

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 150

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 900


if __name__ == "__main__":
    unittest.main()
