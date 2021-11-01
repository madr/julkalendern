import unittest

from solutions.day_05 import Solution


class Day05TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        BFFFBBFRRR
        FFFBBBFRRR
        BBFFBBFRLL
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        BFFFBBFRRR
        FFFBBBFRRR
        BBFFBBFRLL
        """
        expected = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
        assert self.solution.parse_input(data) == expected

    def test_find_highest_seat_id(self):
        assert (
            self.solution.highest_seat_id(["BBBFBBBLLL", "BBBFBBBLLR"]) == "BBBFBBBLLR"
        )
        assert (
            self.solution.highest_seat_id(["FBBFBBBLLL", "BBBFBBBLLR"]) == "BBBFBBBLLR"
        )
        assert (
            self.solution.highest_seat_id(["BBBFBBBLRL", "BBBFBBBLLR"]) == "BBBFBBBLRL"
        )

    def test_get_seat_id(self):
        assert self.solution.get_seat_id("BFFFBBFRRR") == 567
        assert self.solution.get_seat_id("FFFBBBFRRR") == 119
        assert self.solution.get_seat_id("BBFFBBFRLL") == 820

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 820


if __name__ == "__main__":
    unittest.main()
