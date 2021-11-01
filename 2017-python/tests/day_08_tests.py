import unittest

from solutions.day_08 import Solution


class Day8TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_largest_registry_value(self):
        puzzle_input = '''
        b inc 5 if a > 1
        a inc 1 if b < 5
        c dec -10 if a >= 1
        c inc -20 if c == 10
        '''.strip()
        assert self.solution.solve(puzzle_input) == 1

    def test_largest_ath_registry_value(self):
        puzzle_input = '''
        b inc 5 if a > 1
        a inc 1 if b < 5
        c dec -10 if a >= 1
        c inc -20 if c == 10
        '''.strip()
        assert self.solution.solve_again(puzzle_input) == 10


if __name__ == '__main__':
    unittest.main()
