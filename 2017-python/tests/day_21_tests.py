import unittest

from solutions.day_21 import Solution


class Day21TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_something(self):
        puzzle_input = '''
        ../.# => ##./#../...
        .#./..#/### => #..#/..../..../#..#
        '''.strip()
        assert self.solution.solve(puzzle_input, 2) == 12


if __name__ == '__main__':
    unittest.main()
