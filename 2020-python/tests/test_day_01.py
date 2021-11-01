import unittest

from solutions.day_01 import Solution


class Day01TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        1721
        979
        366
        299
        675
        1456
        """
        )

    def test_find_matching_pair(self):
        assert self.solution.solve(self.puzzle_input) == 514579

    def test_find_matching_triplet(self):
        assert self.solution.solve_again(self.puzzle_input) == 241861950


if __name__ == "__main__":
    unittest.main()
