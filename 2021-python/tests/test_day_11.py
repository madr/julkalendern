import unittest

from solutions.day_11 import Solution


class Day11TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        1234
        5678
        """
        assert self.solution.parse_input(data) == [[1, 2, 3, 4], [5, 6, 7, 8]]

    def test_solve_first_part(self):
        data = """
        11111
19991
19191
19991
11111
        """
        assert self.solution.solve(self.solution.parse_input(data), 2) == 9
        assert self.solution.solve(self.puzzle_input) == 1656

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 195


if __name__ == "__main__":
    unittest.main()
