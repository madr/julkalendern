import unittest

from solutions.day_05 import Solution


class Day05TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        11,222 -> 4444,55555
8,0 -> 0,8
        """
        assert self.solution.parse_input(data) == [(11, 222, 4444, 55555), (8, 0, 0, 8)]

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 5

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 12


if __name__ == "__main__":
    unittest.main()
