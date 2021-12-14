import unittest

from solutions.day_14 import Solution


class Day14TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C

        """
        )

    def test_parse_puzzle_input(self):
        data = """
        NNCB

CH -> B
HH -> N
CB -> H
        """
        assert self.solution.parse_input(data) == (
            "NNCB",
            [("CH", "B"), ("HH", "N"), ("CB", "H")],
        )

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 1749 - 161

    # def test_solve_second_part(self):
    #     assert self.solution.solve_again(self.puzzle_input) == True


if __name__ == "__main__":
    unittest.main()
