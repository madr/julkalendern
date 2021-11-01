import unittest

from solutions.day_20 import Solution


class Day20TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_shortest_distance_over_time(self):
        puzzle_input = '''
        p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
        p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
        '''.strip()
        assert self.solution.solve(puzzle_input, 4) == 0

    def test_something(self):
        puzzle_input = '''
        p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
        p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
        p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
        p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
        '''.strip()
        assert self.solution.solve_again(puzzle_input, 4) == 1


if __name__ == '__main__':
    unittest.main()
