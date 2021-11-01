import unittest

from solutions.day_15 import Solution


class Day15TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_40m_pairs(self):
        puzzle_input = '''
        Generator A starts with 65
        Generator B starts with 8921
        '''.strip()
        #assert self.solution.solve(puzzle_input) == 588

    def test_5k_pairs(self):
        puzzle_input = '''
        Generator A starts with 65
        Generator B starts with 8921
        '''.strip()
        assert self.solution.solve_again(puzzle_input) == 309


if __name__ == '__main__':
    unittest.main()
