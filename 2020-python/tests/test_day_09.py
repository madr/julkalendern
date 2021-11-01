import unittest

from solutions.day_09 import Solution


class Day09TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
        """.strip()
        )

    def test_parse_puzzle_input(self):
        data = """
        23
        7
        13
        """.strip()
        expected = [23, 7, 13]
        assert self.solution.parse_input(data) == expected

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input, 5) == 127

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input, 5) == 62


if __name__ == "__main__":
    unittest.main()
