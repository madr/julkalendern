import itertools
from collections import Counter

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '02.in'

    def __str__(self):
        return 'Day 2: Inventory Management System'

    def _count(self, line, num):
        return any(map(lambda n: n == num, dict(Counter(line).most_common()).values()))

    def countn(self, data, n):
        return sum(map(lambda s: self._count(s, n), data))

    def solve(self, puzzle_input):
        data = puzzle_input.splitlines()
        return self.countn(data, 2) * self.countn(data, 3)

    def solve_again(self, puzzle_input):
        lines = puzzle_input.splitlines()
        for l, r in itertools.combinations(lines, 2):
            diff = list(filter(lambda x: x[0] != x[1], zip(l, r)))
            if len(diff) == 1:
                return ''.join([c for i, c in enumerate(l) if l[i] == r[i]])


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
