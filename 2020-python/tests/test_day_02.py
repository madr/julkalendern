import unittest

from solutions.day_02 import Solution


class Day02TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        1-3 a: abcde
        1-3 b: cdefg
        2-9 c: ccccccccc
        """
        )

    def test_parse_input(self):
        data = """
        1-3 a: abcde
        """
        expected = [(1, 3, "a", "abcde")]

        assert self.solution.parse_input(data) == expected

    def test_solve_first_part(self):
        expected = 2

        assert self.solution.solve(self.puzzle_input) == expected

    def test_solve_second_part(self):
        expected = 1

        assert self.solution.solve_again(self.puzzle_input) == expected


if __name__ == "__main__":
    unittest.main()
