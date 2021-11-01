import unittest

from solutions.day_03 import Solution


class Day03TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_overlapping_squares(self):
        puzzle_input = '\n'.join([
            '#1 @ 1,3: 4x4',
            '#2 @ 3,1: 4x4',
            '#3 @ 5,5: 2x2',
        ])
        assert self.solution.parse_claim('#123 @ 3,2: 5x4') == (123, 3, 2, 5, 4)
        assert self.solution.solve(puzzle_input) == 4

    def test_find_non_repeated_id(self):
        puzzle_input = '\n'.join([
            '#1 @ 1,3: 4x4',
            '#2 @ 3,1: 4x4',
            '#3 @ 5,5: 2x2',
        ])
        assert self.solution.solve_again(puzzle_input) == 3


if __name__ == '__main__':
    unittest.main()
