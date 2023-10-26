import unittest

from solutions.day_14 import Solution


class Day14TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
    Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
        """
        )

    def test_parse_puzzle_input(self):
        data = """
    Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
        """
        assert self.solution.parse_input(data) == [(14, 10, 127)]

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input, 1000) == 1120

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input, 1000) == 689


if __name__ == "__main__":
    unittest.main()
