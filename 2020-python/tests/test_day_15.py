import unittest

from solutions.day_15 import Solution


class Day15TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        0,3,6
        """.strip()
        )

    def test_parse_puzzle_input(self):
        data = """
        0,3,6
        """.strip()
        assert self.solution.parse_input(data) == [0, 3, 6]

    def test_solve_first_part(self):
        assert self.solution.solve([0, 3, 6]) == 436
        assert self.solution.solve([1, 3, 2]) == 1
        assert self.solution.solve([1, 2, 3]) == 27
        assert self.solution.solve([2, 3, 1]) == 78
        assert self.solution.solve([3, 2, 1]) == 438
        assert self.solution.solve([3, 1, 2]) == 1836


if __name__ == "__main__":
    unittest.main()
