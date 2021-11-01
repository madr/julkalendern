import unittest

from solutions.day_01 import Solution


class Day01TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_resolves_frequency(self):
        freq_1 = '\n'.join(['+1', '+1', '+1'])
        freq_2 = '\n'.join(['+1', '+1', '-2'])
        freq_3 = '\n'.join(['-1', '-2', '-3'])
        assert self.solution.solve(freq_1) == 3
        assert self.solution.solve(freq_2) == 0
        assert self.solution.solve(freq_3) == -6

    def test_resolves_recurring_frequency(self):
        freq_1 = '\n'.join(['+1', '-1'])
        freq_2 = '\n'.join(['+3', '+3', '+4', '-2', '-4'])
        freq_3 = '\n'.join(['-6', '+3', '+8', '+5', '-6'])
        freq_4 = '\n'.join(['+7', '+7', '-2', '-7', '-4'])
        assert self.solution.solve_again(freq_1) == 0
        assert self.solution.solve_again(freq_2) == 10
        assert self.solution.solve_again(freq_3) == 5
        assert self.solution.solve_again(freq_4) == 14


if __name__ == '__main__':
    unittest.main()
