import unittest

from solutions.day_11 import Solution


class Day11TestCase(unittest.TestCase):
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
        """.strip()
        assert self.solution.parse_input(data) == "<REPLACE ME>"

    def test_validate_passwords(self):
        assert not self.solution.is_valid("hijklmmn")
        assert not self.solution.is_valid("abbceffg")
        assert not self.solution.is_valid("abbcegjk")

    def test_solve_first_part(self):
        assert self.solution.solve("abcdefgh") == "abcdffaa"
        assert self.solution.solve("ghijklmn") == "ghjaabcc"

    # def test_solve_second_part(self):
    #     assert self.solution.solve_again(self.puzzle_input) == True


if __name__ == "__main__":
    unittest.main()
