import unittest

from solutions.day_07 import Solution


class Day07TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        16,1,2,0,4,2,7,1,2,14
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        16,1,2
        """
        assert self.solution.parse_input(data) == [16, 1, 2]

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 37

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 168


if __name__ == "__main__":
    unittest.main()
