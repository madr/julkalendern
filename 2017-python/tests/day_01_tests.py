import unittest

from solutions.day_01 import Solution


class Day1TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sums_equal_pairs(self):
        assert self.solution.solve('1122') == 3
        assert self.solution.solve('1111') == 4
        assert self.solution.solve('1234') == 0
        assert self.solution.solve('91212129') == 9

    def test_sums_equal_pairs_halvway_around(self):
        assert self.solution.solve_again('1212') == 6
        assert self.solution.solve_again('1221') == 0
        assert self.solution.solve_again('123425') == 4
        assert self.solution.solve_again('123123') == 12
        assert self.solution.solve_again('12131415') == 4


if __name__ == '__main__':
    unittest.main()
