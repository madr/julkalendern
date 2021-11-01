import unittest

from solutions.day_02 import Solution


class Day02TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_calculates_checksum(self):
        puzzle_input = "\n".join([
            'abcdef',
            'bababc',
            'abbcde',
            'abcccd',
            'aabcdd',
            'abcdee',
            'ababab'
        ])
        assert self.solution.countn(puzzle_input.splitlines(), 2) == 4
        assert self.solution.countn(puzzle_input.splitlines(), 3) == 3
        assert self.solution.solve(puzzle_input) == 12

    def test_common_box_names(self):
        puzzle_input = "\n".join([
            'abcde',
            'fghij',
            'klmno',
            'pqrst',
            'fguij',
            'axcye',
            'wvxyz'
        ])
        assert self.solution.solve_again(puzzle_input) == 'fgij'


if __name__ == '__main__':
    unittest.main()
