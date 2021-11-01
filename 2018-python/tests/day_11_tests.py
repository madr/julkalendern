import unittest

from solutions.day_11 import Solution


class Day11TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_power_level(self):
        assert self.solution.get_power_level(122, 79, 57) == -5
        assert self.solution.get_power_level(217, 196, 39) == 0
        assert self.solution.get_power_level(101, 153, 71) == 4

    def test_largest_square_size3x3(self):
        assert self.solution.solve('18') == (33, 45)
        assert self.solution.solve('42') == (21, 61)

    def test_largest_square_any_size(self):
        assert self.solution.solve_again('18') == (90, 269, 16)
        assert self.solution.solve_again('42') == (232, 251, 12)


if __name__ == '__main__':
    unittest.main()
