import unittest

from solutions.day_17 import Solution


class Day17TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_something(self):
        assert self.solution.solve('3') == 638


if __name__ == '__main__':
    unittest.main()
