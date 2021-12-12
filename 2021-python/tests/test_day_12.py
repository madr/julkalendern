import unittest

from solutions.day_12 import Solution


class Day12TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        start-A
start-b
A-c
A-b
b-d
A-end
b-end
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        a-b
        q1w2-e3r4
        """
        assert self.solution.parse_input(data) == [["a", "b"], ["q1w2", "e3r4"]]

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 10

    def test_solve_second_part(self):
        assert self.solution.solve_again(self.puzzle_input) == 36


if __name__ == "__main__":
    unittest.main()

"""
start,A,b,A,b,A,c,A,end
start,A,b,A,b,A,end
start,A,b,A,b,end
start,A,b,A,c,A,b,A,end
start,A,b,A,c,A,b,end
start,A,b,A,c,A,c,A,end
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,d,b,A,c,A,end
start,A,b,d,b,A,end
start,A,b,d,b,end
start,A,b,end
start,A,c,A,b,A,b,A,end
start,A,c,A,b,A,b,end
start,A,c,A,b,A,c,A,end
start,A,c,A,b,A,end
start,A,c,A,b,d,b,A,end
start,A,c,A,b,d,b,end
start,A,c,A,b,end
start,A,c,A,c,A,b,A,end
start,A,c,A,c,A,b,end
start,A,c,A,c,A,end
start,A,c,A,end
start,A,end
start,b,A,b,A,c,A,end
start,b,A,b,A,end
start,b,A,b,end
start,b,A,c,A,b,A,end
start,b,A,c,A,b,end
start,b,A,c,A,c,A,end
start,b,A,c,A,end
start,b,A,end
start,b,d,b,A,c,A,end
start,b,d,b,A,end
start,b,d,b,end
start,b,end
"""
