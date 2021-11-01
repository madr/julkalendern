import unittest

from solutions.day_16 import Solution


class Day16TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
        """.strip()
        )

    def test_parse_puzzle_input(self):
        data = """
        class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
        """.strip()
        assert self.solution.parse_input(data) == (
            [
                ("class", range(1, 4), range(5, 8)),
                ("row", range(6, 12), range(33, 45)),
                ("seat", range(13, 41), range(45, 51)),
            ],
            [7, 1, 14],
            ([[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]]),
        )

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 71

    def test_solve_second_part(self):
        data = """
        class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
        """.strip()
        i = self.solution.parse_input(data)

        assert self.solution.solve_again(i) == 1  # No departures

    def test_validity(self):
        ranges = [
            ("a", range(1, 4), range(5, 8)),
            ("b", range(6, 12), range(33, 45)),
            ("c", range(13, 41), range(45, 51)),
        ]
        assert self.solution.get_invalid_values(ranges, [7, 3, 47]) == []
        assert self.solution.get_invalid_values(ranges, [40, 4, 50]) == [4]
        assert self.solution.get_invalid_values(ranges, [55, 2, 20]) == [55]
        assert self.solution.get_invalid_values(ranges, [38, 6, 12]) == [12]

    def test_positions(self):
        data = """
        class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
        """.strip()
        ranges, _, tickets = self.solution.parse_input(data)

        assert self.solution.get_positions(ranges, tickets) == ["row", "class", "seat"]


if __name__ == "__main__":
    unittest.main()
