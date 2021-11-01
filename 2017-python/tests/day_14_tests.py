import unittest

from solutions.day_14 import Solution


class Day14TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_used_squares(self):
        assert self.solution.solve('flqrgnkx') == 8108

    def test_regions(self):
        assert self.solution.solve_again('flqrgnkx') == 1242


if __name__ == '__main__':
    unittest.main()
