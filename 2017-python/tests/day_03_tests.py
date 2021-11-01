import unittest

from solutions.day_03 import Solution


class Day3TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_shortest_manhattan_distance(self):
        assert self.solution.solve('1') == 0
        assert self.solution.solve('12') == 3
        assert self.solution.solve('23') == 2
        assert self.solution.solve('1024') == 31


if __name__ == '__main__':
    unittest.main()
