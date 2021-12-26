import unittest

from solutions.day_10 import Solution


class Day10TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        [({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        abc
        efg
        """
        assert self.solution.parse_input(data) == ["abc", "efg"]

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 26397

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 288957


if __name__ == "__main__":
    unittest.main()
