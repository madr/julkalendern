import unittest

from solutions.day_12 import Solution


class Day12TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_connected_to_program0(self):
        puzzle_input = '''
        0 <-> 2
        1 <-> 1
        2 <-> 0, 3, 4
        3 <-> 2, 4
        4 <-> 2, 3, 6
        5 <-> 6
        6 <-> 4, 5
        '''.strip()
        assert self.solution.solve(puzzle_input) == 6

    def test_group_coun(self):
        puzzle_input = '''
        0 <-> 2
        1 <-> 1
        2 <-> 0, 3, 4
        3 <-> 2, 4
        4 <-> 2, 3, 6
        5 <-> 6
        6 <-> 4, 5
        '''.strip()
        assert self.solution.solve_again(puzzle_input) == 2


if __name__ == '__main__':
    unittest.main()
