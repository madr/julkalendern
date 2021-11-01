import unittest

from solutions.day_14 import Solution


class Day14TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_something(self):
        puzzle_input = ''
        assert self.solution.solve(puzzle_input) == True


if __name__ == '__main__':
    unittest.main()
