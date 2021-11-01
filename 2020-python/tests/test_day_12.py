import unittest

from solutions.day_12 import Solution


class Day12TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        F10
N3
F7
R90
F11
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        F10
N3
F7
        """.strip()
        expected = [
            ("F", 10),
            ("N", 3),
            ("F", 7),
        ]

        assert self.solution.parse_input(data) == expected

    def test_move(self):
        assert self.solution.move((0, 0), "E", 2) == (2, 0)
        assert self.solution.move((0, 0), "S", 2) == (0, 2)
        assert self.solution.move((0, 0), "W", 2) == (-2, 0)
        assert self.solution.move((0, 0), "N", 2) == (0, -2)

    def test_move_with_factor(self):
        assert self.solution.move((0, 0), "E", 2, (2, 3)) == (4, 6)
        assert self.solution.move((2, 2), "S", 3, (4, 3)) == (2 + 3 * 4, 2 + 3 * 3)

    def test_rotate(self):
        assert self.solution.rotate("E", "L", 90) == "N"
        assert self.solution.rotate("E", "L", 180) == "W"
        assert self.solution.rotate("E", "L", 270) == "S"
        assert self.solution.rotate("E", "R", 90) == "S"
        assert self.solution.rotate("E", "R", 180) == "W"
        assert self.solution.rotate("E", "R", 270) == "N"

    def test_reposition(self):
        assert self.solution.reposition("E", (10, -4), "R", 90) == ("S", (4, 10))
        assert self.solution.reposition("E", (10, -4), "R", 180) == ("W", (-10, 4))
        assert self.solution.reposition("E", (10, -4), "R", 270) == ("N", (-4, -10))
        assert self.solution.reposition("E", (10, -4), "L", 90) == ("N", (-4, -10))
        assert self.solution.reposition("E", (10, -4), "L", 180) == ("W", (-10, 4))
        assert self.solution.reposition("E", (10, -4), "L", 270) == ("S", (4, 10))

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 25

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 286


if __name__ == "__main__":
    unittest.main()
