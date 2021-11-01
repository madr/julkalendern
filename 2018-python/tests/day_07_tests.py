import unittest

from solutions.day_07 import Solution


class Day07TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = '\n'.join([
            'Step C must be finished before step A can begin.',
            'Step C must be finished before step F can begin.',
            'Step A must be finished before step B can begin.',
            'Step A must be finished before step D can begin.',
            'Step B must be finished before step E can begin.',
            'Step D must be finished before step E can begin.',
            'Step F must be finished before step E can begin.'
        ])

    def test_order_of_steps(self):
        assert self.solution.solve(self.puzzle_input) == 'CABDFE'

    def test_seconds_for_workers(self):
        assert self.solution.solve_with_workers(self.puzzle_input, 2, 60) == 15


if __name__ == '__main__':
    unittest.main()
