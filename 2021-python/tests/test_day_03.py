import unittest

from solutions.day_03 import Solution


class Day03TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        00100
11110
        """
        assert self.solution.parse_input(data) == ["00100", "11110"]

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 198

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 230


if __name__ == "__main__":
    unittest.main()
