import unittest

from solutions.day_05 import Solution


class Day05TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_react_polymer(self):
        assert self.solution.solve('dabAcCaCBAcCcaDA') == 10

    def test_reduce_and_choose_most_efficient_polymer(self):
        assert self.solution.solve_again('dabAcCaCBAcCcaDA') == 4


if __name__ == '__main__':
    unittest.main()
