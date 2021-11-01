import itertools
import re
from collections import defaultdict

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '03.in'

    claim_pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    def __str__(self):
        return 'Day 3: No Matter How You Slice It'

    def solve(self, puzzle_input):
        claims = self.get_claims(puzzle_input)
        return sum(map(lambda c: c[1] > 1, claims.items()))

    def solve_again(self, puzzle_input):
        claims = self.get_claims(puzzle_input)
        non_repeated_id = self._find_nri(puzzle_input, claims)
        return non_repeated_id

    def parse_claim(self, data):
        return tuple(map(int, self.claim_pattern.search(data).groups()))

    def get_claims(self, puzzle_input):
        claims = defaultdict(int)
        for line in puzzle_input.splitlines():
            _, left, top, width, height = self.parse_claim(line)
            for w, h in itertools.product(range(left, left + width), range(top, top + height)):
                claims[(w, h)] += 1
        return claims

    def _find_nri(self, puzzle_input, claims):
        for line in puzzle_input.splitlines():
            repeated = False
            cid, left, top, width, height = self.parse_claim(line)
            for w, h in itertools.product(range(left, left + width), range(top, top + height)):
                if claims[(w, h)] > 1:
                    repeated = True
            if not repeated:
                return cid


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
