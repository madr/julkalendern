import unittest

from solutions.day_10 import Solution


class Day10TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_process_and_check(self):
        self.solution.reset(5)
        self.solution.reverse(3)
        assert self.solution.list == [2, 1, 0, 3, 4]
        assert self.solution.skip_size == 1
        assert self.solution.pos == 3
        self.solution.reverse(4)
        assert self.solution.list == [4, 3, 0, 1, 2]
        assert self.solution.skip_size == 2
        assert self.solution.pos == 3
        self.solution.reverse(1)
        assert self.solution.list == [4, 3, 0, 1, 2]
        assert self.solution.skip_size == 3
        assert self.solution.pos == 1
        self.solution.reverse(5)
        assert self.solution.list == [3, 4, 2, 1, 0]
        assert self.solution.skip_size == 4
        assert self.solution.pos == 4
        assert self.solution.solve('3,4,1,5', r=5) == 12

    def test_dense_hash(self):
        assert self.solution.solve_again('') == 'a2582a3a0e66e6e86e3812dcb672a272'
        assert self.solution.solve_again('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
        assert self.solution.solve_again('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
        assert self.solution.solve_again('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'


if __name__ == '__main__':
    unittest.main()
