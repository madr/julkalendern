import unittest

from solutions.day_12 import Solution


class Day12TestCase(unittest.TestCase):
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

    def test_solve_first_part(self):
        assert self.solution.solve("[1,2,3]") == 6
        assert self.solution.solve('{"a":2,"b":4}') == 6
        assert self.solution.solve("[[[3]]]") == 3
        assert self.solution.solve('{"a":{"b":4},"c":-1}') == 3
        assert self.solution.solve('{"a":[-1,1]}') == 0
        assert self.solution.solve('-1,{"a":1}]') == 0
        assert self.solution.solve("{}") == 0
        assert self.solution.solve("[]") == 0

    def test_solve_second_part(self):
        assert self.solution.solve_again("[1,2,3]") == 6
        assert self.solution.solve_again('[1,{"c":"red","b":2},3]') == 4
        assert self.solution.solve_again('{"d":"red","e":[1,2,3,4],"f":5}') == 0
        assert self.solution.solve_again('[1,"red",5]') == 6


if __name__ == "__main__":
    unittest.main()
