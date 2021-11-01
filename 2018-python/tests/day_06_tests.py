import unittest

from solutions.day_06 import Solution


class Day06TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_get_largest_area_size(self):
        puzzle_input = '\n'.join([
            '1, 1',
            '1, 6',
            '8, 3',
            '3, 4',
            '5, 5',
            '8, 9',
        ])
        assert self.solution.solve(puzzle_input) == 17

    def test_get_region(self):
        puzzle_input = '\n'.join([
            '1, 1',
            '1, 6',
            '8, 3',
            '3, 4',
            '5, 5',
            '8, 9',
        ])
        assert self.solution.get_region(puzzle_input, 32) == 16


if __name__ == '__main__':
    unittest.main()
