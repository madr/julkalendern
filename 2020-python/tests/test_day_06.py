import unittest

from solutions.day_06 import Solution


class Day06TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        abc

a
b
c

ab
ac

a
a
a
a

b
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        abc

        a
        b
        c

        ab
        ac
        """
        expected = [["abc"], ["a", "b", "c"], ["ab", "ac"]]
        assert self.solution.parse_input(data) == expected

    def test_count_any_yes_answers(self):
        assert self.solution.count_any_yes_answers(["abc"]) == 3
        assert self.solution.count_any_yes_answers(["a", "b", "c"]) == 3
        assert self.solution.count_any_yes_answers(["ab", "ac"]) == 3
        assert self.solution.count_any_yes_answers(["a", "a", "a", "a"]) == 1
        assert self.solution.count_any_yes_answers(["b"]) == 1

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 11

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 6


if __name__ == "__main__":
    unittest.main()
