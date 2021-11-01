import unittest

from solutions.day_08 import Solution


class Day08TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
        """.strip()
        )

    def test_parse_puzzle_input(self):
        data = """
        nop +0
acc +1
jmp -4
        """.strip()
        assert self.solution.parse_input(data) == [("nop", 0), ("acc", 1), ("jmp", -4)]

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 5

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 8


if __name__ == "__main__":
    unittest.main()
