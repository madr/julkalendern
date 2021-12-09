import unittest

from solutions.day_09 import Solution


class Day09TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        2199943210
3987894921
9856789892
8767896789
9899965678
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        2199943210
3987894921
        """
        assert self.solution.parse_input(data) == [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        ]

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 15

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 9 * 14 * 9  # 891684


if __name__ == "__main__":
    unittest.main()
