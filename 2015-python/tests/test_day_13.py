import unittest

from solutions.day_13 import Solution


class Day13TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
        """
        )

    def test_parse_puzzle_input(self):
        data = """
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
        """
        assert self.solution.parse_input(data) == dict(
            [
                ("Alice-Bob", 54),
                ("Alice-Carol", -79),
            ]
        )

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 330

    # def test_solve_second_part(self):
    #     assert self.solution.solve_again(self.puzzle_input) == True


if __name__ == "__main__":
    unittest.main()
