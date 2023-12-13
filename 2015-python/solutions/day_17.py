from collections import defaultdict
from itertools import combinations

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "17.txt"

    def __str__(self):
        return "Day 17: No Such Thing as Too Much"

    def parse_input(self, data):
        return data.strip()

    def solve(self, puzzle_input, g=150):
        return self._solve(puzzle_input, g)[0]

    def solve_again(self, puzzle_input, g=150):
        return self._solve(puzzle_input, g)[1]

    def _solve(self, puzzle_input, g=150):
        buckets = sorted(list(map(int, puzzle_input.split())), reverse=True)
        t = 0
        r = defaultdict(int)
        for i in range(len(buckets)):
            for c in combinations(buckets, i):
                if sum(c) == g:
                    t += 1
                    r[i] += 1
        return t, min(r.items(), key=lambda kv: kv[0])[1]


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
