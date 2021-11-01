import unittest

from solutions.day_14 import Solution


class Day14TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_parse_puzzle_input(self):
        data = """
        mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
        """.strip()
        expected = [
            ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", [(8, 11), (7, 101), (8, 0)])
        ]

        assert len(self.solution.parse_input(data)) == 1
        assert (
            self.solution.parse_input(data)[0][0]
            == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        )
        assert len(self.solution.parse_input(data)[0][1]) == 3
        assert (8, 11) in self.solution.parse_input(data)[0][1]
        assert (7, 101) in self.solution.parse_input(data)[0][1]
        assert (8, 0) in self.solution.parse_input(data)[0][1]

    def test_solve_first_part(self):
        data = """
        mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
        """.strip()

        puzzle_input = self.solution.parse_input(data)
        assert self.solution.solve(puzzle_input) == 165

    def test_solve_second_part(self):
        data = """
        mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
        """.strip()

        puzzle_input = self.solution.parse_input(data)
        assert self.solution.solve_again(puzzle_input) == 208


if __name__ == "__main__":
    unittest.main()
