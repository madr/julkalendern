import unittest

from solutions.day_11 import Solution


class Day11TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        L.LL.LL.LL
        LLLLLLL.LL
        L.L.L..L..
        LLLL.LL.LL
        L.LL.LL.LL
        L.LLLLL.LL
        ..L.L.....
        LLLLLLLLLL
        L.LLLLLL.L
        L.LLLLL.LL
        """.strip()
        )

    def test_parse_puzzle_input(self):
        data = """
        L.LL.LL.LL
LLLLLLL.LL
        """.strip()
        expected = [
            ["L", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
            ["L", "L", "L", "L", "L", "L", "L", ".", "L", "L"],
        ]

        assert self.solution.parse_input(data) == expected

    def test_adjacent(self):
        data = [[1, 2, 3, 4], [11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]

        assert self.solution.get_adjacent(data, 1, 1) == [
            ((-1, -1), 1),
            ((0, -1), 2),
            ((1, -1), 3),
            ((-1, 0), 11),
            ((1, 0), 13),
            ((-1, 1), 21),
            ((0, 1), 22),
            ((1, 1), 23),
        ]
        assert self.solution.get_adjacent(data, 0, 0) == [
            ((1, 0), 2),
            ((0, 1), 11),
            ((1, 1), 12),
        ]
        assert self.solution.get_adjacent(data, 3, 3) == [
            ((-1, -1), 23),
            ((0, -1), 24),
            ((-1, 0), 33),
        ]
        assert self.solution.get_adjacent(data, 3, 0) == [
            ((0, -1), 21),
            ((1, -1), 22),
            ((1, 0), 32),
        ]
        assert self.solution.get_adjacent(data, 0, 3) == [
            ((-1, 0), 3),
            ((-1, 1), 13),
            ((0, 1), 14),
        ]

    def test_occupy_if_empty(self):
        data = ["L", "L", "L", "L", "L", "L"]
        data_no = ["#", "L", "L", "L", "L", "L"]

        assert self.solution.occupy_if_empty("L", data) == "#"
        assert self.solution.occupy_if_empty("#", data) == "#"
        assert self.solution.occupy_if_empty("L", data_no) == "L"

    def test_empty_if_occupied(self):
        data = ["L", "L", "L", "L", "L", "L"]
        data_no = ["L", "L", "#", "#", "#", "#"]
        data_no2 = ["L", "#", "#", "#", "#", "#"]

        assert self.solution.empty_if_occupied("L", data) == "L"
        assert self.solution.empty_if_occupied("#", data_no) == "L"
        assert self.solution.empty_if_occupied("#", data_no2) == "L"
        assert self.solution.empty_if_occupied("#", data) == "#"

    def test_tick(self):
        data_1 = self.solution.parse_input(
            """
        L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
        """.strip()
        )
        data_2 = self.solution.parse_input(
            """
        #.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
        """.strip()
        )
        data_3 = self.solution.parse_input(
            """
        #.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
        """.strip()
        )

        assert self.solution.tick(data_1, 10, 10, tolerance=5, in_view=True) == data_2
        assert self.solution.tick(data_2, 10, 10, tolerance=5, in_view=True) == data_3

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 37

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 26


if __name__ == "__main__":
    unittest.main()
