import unittest

from solutions.day_18 import Solution


class Day18TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_something(self):
        puzzle_input = '''
        set a 1
        add a 2
        mul a a
        mod a 5
        snd a
        set a 0
        rcv a
        jgz a -1
        set a 1
        jgz a -2
        '''.strip()
        assert self.solution.solve(puzzle_input) == 4

    def test_something_else(self):
        puzzle_input = '''
        snd 1
        snd 2
        snd p
        rcv a
        rcv b
        rcv c
        rcv d
        '''.strip()
        assert self.solution.solve_again(puzzle_input) == 3


if __name__ == '__main__':
    unittest.main()
