import unittest

from solutions.day_05 import Solution


class Day5TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_calculate_exit_distance(self):
        puzzle_input = '\n'.join(['0', '3', '0', '1', '-3',])
        assert self.solution.solve(puzzle_input) == 5

    def test_calculate_stranger_exit_distance(self):
        puzzle_input = '\n'.join(['0', '3', '0', '1', '-3',])
        assert self.solution.solve_again(puzzle_input) == 10


if __name__ == '__main__':
    unittest.main()
