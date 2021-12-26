import unittest

from solutions.day_01 import Solution


class Day01TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        199
200
208
210
200
207
240
269
260
263
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        12
        23
        45
        """
        assert self.solution.parse_input(data) == [12, 23, 45]

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 7

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 5


if __name__ == "__main__":
    unittest.main()
