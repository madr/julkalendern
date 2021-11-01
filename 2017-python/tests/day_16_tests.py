import unittest

from solutions.day_16 import Solution


class Day16TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_something(self):
        puzzle_input = '''s1,x3/4,pe/b'''.strip()
        assert self.solution.solve(puzzle_input, 5) == 'baedc'


if __name__ == '__main__':
    unittest.main()
