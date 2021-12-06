import unittest

from solutions.day_06 import Solution


class Day06TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        3,4,3,1,2
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        3,4,3,1,2
        """
        assert self.solution.parse_input(data) == [3, 4, 3, 1, 2]

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 5934

    # def test_solve_second_part(self):
    #    assert self.solution.solve_again(self.puzzle_input) == 26984457539


if __name__ == "__main__":
    unittest.main()
