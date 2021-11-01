import unittest

from solutions.day_13 import Solution


class Day13TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_get_through_firewall(self):
        puzzle_input = '''
        0: 3
        1: 2
        4: 4
        6: 4
        '''.strip()
        assert self.solution.solve(puzzle_input) == 24

    def test_wait(self):
        puzzle_input = '''
        0: 3
        1: 2
        4: 4
        6: 4
        '''.strip()
        assert self.solution.solve_again(puzzle_input) == 10


if __name__ == '__main__':
    unittest.main()
