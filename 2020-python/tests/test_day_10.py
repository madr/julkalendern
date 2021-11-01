import unittest

from solutions.day_10 import Solution


class Day10TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.data_1 = self.puzzle_input = self.solution.parse_input(
            """
        16
        10
        15
        5
        1
        11
        7
        19
        6
        12
        4
        """.strip()
        )
        self.data_2 = self.puzzle_input = self.solution.parse_input(
            """
        28
        33
        18
        42
        31
        14
        46
        20
        48
        47
        24
        23
        49
        45
        19
        38
        39
        11
        1
        32
        25
        35
        8
        17
        7
        9
        4
        2
        34
        10
        3
        """.strip()
        )

    def test_parse_puzzle_input(self):
        data = """
        16
        1
        15
        """.strip()
        assert self.solution.parse_input(data) == [16, 1, 15]

    def test_solve_first_part(self):
        assert self.solution.solve(self.data_1) == 7 * 5
        assert self.solution.solve(self.data_2) == 22 * 10

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.data_1) == 8


if __name__ == "__main__":
    unittest.main()
