import unittest

from solutions.day_10 import Solution


class Day10TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        <REPLACE ME>
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        12
        """
        assert self.solution.parse_input(data) == "12"

    def test_solve_first_part(self):
        assert self.solution._sequence("1", 1) == "11"
        assert self.solution._sequence("11", 1) == "21"
        assert self.solution._sequence("21", 1) == "1211"
        assert self.solution._sequence("1211", 1) == "111221"
        assert self.solution._sequence("111221", 1) == "312211"
        assert self.solution._sequence("1", 5) == "312211"


if __name__ == "__main__":
    unittest.main()
