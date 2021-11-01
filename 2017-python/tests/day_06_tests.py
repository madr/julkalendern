import unittest

from solutions.day_06 import Solution


class Day6TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_count_redistribution_cycles(self):
        puzzle_input = '0 2 7 0'
        banks = list(map(int, puzzle_input.split()))
        assert self.solution.redistribute(banks) == (2, 4, 1, 2)
        assert self.solution.redistribute((2, 4, 1, 2)) == (3, 1, 2, 3)
        assert self.solution.redistribute((3, 1, 2, 3)) == (0, 2, 3, 4)
        assert self.solution.redistribute((0, 2, 3, 4)) == (1, 3, 4, 1)
        assert self.solution.redistribute((1, 3, 4, 1)) == (2, 4, 1, 2)
        assert self.solution.solve(puzzle_input) == 5

    def test_count_redistribution_cycles_again(self):
        puzzle_input = '0 2 7 0'
        assert self.solution.solve_again(puzzle_input) == 4


if __name__ == '__main__':
    unittest.main()
