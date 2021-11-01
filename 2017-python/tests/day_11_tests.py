import unittest

from solutions.day_11 import Solution


class Day11TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_distance(self):
        assert self.solution.solve('ne,ne,ne') == 3
        assert self.solution.solve('ne,ne,sw,sw') == 0
        assert self.solution.solve('ne,ne,s,s') == 2
        assert self.solution.solve('se,sw,se,sw,sw') == 3

    def test_furthest_away(self):
        assert self.solution.solve_again('ne,ne,sw,sw') == 2
        assert self.solution.solve_again('se,sw,se,sw,sw') == 3


if __name__ == '__main__':
    unittest.main()
