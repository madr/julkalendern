import unittest

from solutions.day_03 import Solution


class Day03TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
        """
        )

    def test_parse_puzzle_input(self):
        data = """
    ..##.......
    #...#...#..
    .#....#..#.
        """
        expected = ["..##.......", "#...#...#..", ".#....#..#."]

        assert self.solution.parse_input(data) == expected

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 7

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 336


if __name__ == "__main__":
    unittest.main()
