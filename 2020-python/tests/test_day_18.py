import unittest

from solutions.day_18 import Solution


class Day18TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        2 * 3 + (4 * 5)
        5 + (8 * 3 + 9 + 3 * 4 * 3)
        5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
        ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        a
        b
        """
        assert self.solution.parse_input(data) == ["a", "b"]

    def test_basic_math(self):
        data = [
            (26, "2 * 3 + (4 * 5)"),
            (437, "5 + (8 * 3 + 9 + 3 * 4 * 3)"),
            (12240, "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"),
            (13632, "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"),
        ]
        for expected, exp in data:
            assert self.solution.basic_math(exp) == expected

    def test_advanced_math(self):
        data = [
            (51, "1 + (2 * 3) + (4 * (5 + 6))"),
            (46, "2 * 3 + (4 * 5)"),
            (1445, "5 + (8 * 3 + 9 + 3 * 4 * 3)"),
            (669060, "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"),
            (23340, "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"),
            (36, "3 * 4 + 3 + 5"),
            (36, "3 * (4 + 3) + 5"),
            (36, "3 * (4 + 3 * 1) + 5"),
        ]
        for expected, exp in data:
            assert self.solution.advanced_math(exp) == expected

    def test_solve_first_part(self):
        expected = 26 + 437 + 12240 + 13632
        assert self.solution.solve(self.puzzle_input) == expected

    def test_solve_second_part(self):
        expected = 46 + 1445 + 23340 + 669060
        assert self.solution.solve_again(self.puzzle_input) == expected

    def test_junk(self):
        data = [
            "(2 + (7 * 5 + 7 * 4) * 8 * (2 + 9 * 5 + 7 * 7) + 5 + (8 + 9 + 5)) + 2 + (7 * 5 * 9 * 6 * 3 + (9 * 8 + 9 * 7 + 3)) + (3 + 5 + 7 + (5 + 2 + 2 + 9)) + 9 + 8"
        ]
        assert self.solution.solve_again(data) == True


if __name__ == "__main__":
    unittest.main()
