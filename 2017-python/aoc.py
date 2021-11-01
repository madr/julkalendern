import sys

try:
    _, day_no, name = sys.argv
except ValueError:
    day_no = None
    name = None

if day_no and name:
    with open('solutions/day_{}.py'.format(day_no.zfill(2)), 'w') as s:
        s.write('''
from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '{day_no}.txt'

    def __str__(self):
        return 'Day {day}: {name}'

    def solve(self, puzzle_input):
        pass

    def solve_again(self, puzzle_input):
        pass


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
'''.strip().format(day=day_no, day_no=day_no.zfill(2), name=name) + '\n')
        with open('tests/day_{}_tests.py'.format(day_no.zfill(2)), 'w') as t:
            t.write('''
import unittest

from solutions.day_{day_no} import Solution


class Day{day_no}TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_something(self):
        assert self.solution.solve('puzzle_input') == True


if __name__ == '__main__':
    unittest.main()
    '''.strip().format(day_no=day_no.zfill(2)) + '\n')
    with open('inputs/{}.txt'.format(day_no.zfill(2)), 'w') as i:
        i.write('')
    exit(0)

print('\nAdvent of Code 2017'
      '\n###################'
      '\n\nby Anders Ytterström (@madr)')

for i in [str(n).zfill(2) for n in range(1, 26)]:
    try:
        solution = __import__('solutions.day_{}'.format(i), globals(), locals(), ['Solution'], 0).Solution()
        solution.show_results()
    except IOError:
        pass
    except ImportError:
        pass
