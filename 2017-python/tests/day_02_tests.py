import unittest

from solutions.day_02 import Solution


class Day2TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_calculates_row_difference(self):
        assert self.solution.get_diff([5, 1, 9, 5]) == 8
        assert self.solution.get_diff([7, 5, 3]) == 4
        assert self.solution.get_diff([2, 4, 6, 8]) == 6

    def test_calculates_checksum(self):
        puzzle_input = '\n'.join(['5 1 9 5', '7 5 3', '2 4 6 8'])
        assert self.solution.solve(puzzle_input) == 18

    def test_calculates_row_even_divisible(self):
        puzzle_input = '\n'.join(['5 9 2 8', '9 4 7 3', '3 8 6 5'])
        assert self.solution.get_even_divisible([5, 9, 2, 8]) == 4
        assert self.solution.get_even_divisible([9, 4, 7, 3]) == 3
        assert self.solution.get_even_divisible([3, 8, 6, 5]) == 2

    def test_calculates_row_result_sum(self):
        puzzle_input = '\n'.join(['5 9 2 8', '9 4 7 3', '3 8 6 5'])
        assert self.solution.solve_again(puzzle_input) == 9


if __name__ == '__main__':
    unittest.main()
