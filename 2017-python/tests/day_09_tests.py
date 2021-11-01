import unittest

from solutions.day_09 import Solution


class Day9TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_calculates_score(self):
        assert self.solution.solve('{}') == 1
        assert self.solution.solve('{{{}}}') == 6
        assert self.solution.solve('{{},{}}') == 5
        assert self.solution.solve('{{{},{},{{}}}}') == 16
        assert self.solution.solve('{<a>,<a>,<a>,<a>}') == 1
        assert self.solution.solve('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
        assert self.solution.solve('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
        assert self.solution.solve('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3

    def test_count_garbage(self):
        assert self.solution.solve_again('<>') == 0
        assert self.solution.solve_again('<random characters>') == 17
        assert self.solution.solve_again('<<<<>') == 3
        assert self.solution.solve_again('<{!>}>') == 2
        assert self.solution.solve_again('<!!>') == 0
        assert self.solution.solve_again('<!!!>>') == 0
        assert self.solution.solve_again('<{o"i!a,<{i<a>') == 10


if __name__ == '__main__':
    unittest.main()
