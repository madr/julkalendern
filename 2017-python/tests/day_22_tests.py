import unittest

from solutions.day_22 import Solution


class Day22TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_infected(self):
        puzzle_input = """
        ..#
        #..
        ...
        """
        assert self.solution.solve(puzzle_input, 7) == 5
        assert self.solution.solve(puzzle_input, 70) == 41
        assert self.solution.solve(puzzle_input, 10000) == 5587

    def test_evolved_infected(self):
        puzzle_input = """
        ..#
        #..
        ...
        """
        assert self.solution.solve_again(puzzle_input, 100) == 26
        assert self.solution.solve_again(puzzle_input, 10000000) == 2511944

if __name__ == '__main__':
    unittest.main()
