import unittest

from solutions.day_13 import Solution


class Day13TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        6,10
0,14

fold along y=7
fold along x=5
        """
        assert self.solution.parse_input(data) == (
            [(6, 10), (0, 14)],
            [("y", "7"), ("x", "5")],
        )

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 17

    # def test_solve_second_part(self):
    #     assert self.solution.solve_again(self.puzzle_input) == True


if __name__ == "__main__":
    unittest.main()
