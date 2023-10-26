import unittest

from solutions.day_15 import Solution


class Day15TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
        """
        assert self.solution.parse_input(data) == [(-1, -2, 6, 3, 8)]

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 62842880

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 57600000


if __name__ == "__main__":
    unittest.main()
