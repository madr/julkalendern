import unittest

from solutions.day_06 import Solution


class Day06TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        <REPLACE ME>
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        <REPLACE ME>
        """
        assert self.solution.parse_input(data) == "<REPLACE ME>"

    # def test_solve_first_part(self):
    #     assert self.solution.solve(self.puzzle_input) == True

    # def test_solve_second_part(self):
    #     assert self.solution.solve_again(self.puzzle_input) == True


if __name__ == "__main__":
    unittest.main()
