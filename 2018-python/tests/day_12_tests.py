import unittest

from solutions.day_12 import Solution


class Day12TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_20_iterations(self):
        puzzle_input = '''initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #'''
        assert self.solution.solve(puzzle_input) == 325


if __name__ == '__main__':
    unittest.main()
