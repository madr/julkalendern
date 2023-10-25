import unittest

from solutions.day_09 import Solution


class Day09TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        Lnd to Dbn = 123
        """
        assert self.solution.parse_input(data) == [("Lnd", "Dbn", 123)]

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 605

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 982


if __name__ == "__main__":
    unittest.main()
