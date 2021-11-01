import unittest

from solutions.day_08 import Solution


class Day08TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_metadata_entries_sum(self):
        assert self.solution.solve('2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2') == 138

    def test_root_node_value(self):
        assert self.solution.solve_again('2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2') == 66


if __name__ == '__main__':
    unittest.main()
