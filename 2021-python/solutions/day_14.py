from solutions import BaseSolution
from collections import Counter, defaultdict


class Solution(BaseSolution):
    input_file = "14.txt"

    def __str__(self):
        return "Day 14: Extended Polymerization"

    def parse_input(self, data):
        p, tv = data.strip().split("\n\n")
        return p, [tuple(r.strip().split(" -> ")) for r in tv.splitlines()]

    def solve(self, puzzle_input):
        return self._solve(puzzle_input, 10)

    def solve_again(self, puzzle_input):
        return self._solve(puzzle_input, 40)

    def _solve(self, puzzle_input, steps=10):
        polymer, pir = puzzle_input
        pir = dict(pir)
        pairs = defaultdict(int)
        chars = defaultdict(int, Counter(polymer))
        for l, r in zip(polymer[:-1], polymer[1:]):
            pairs[(l, r)] += 1
        for _ in range(steps):
            nxt = defaultdict(int)
            for lr, count in pairs.items():
                l, r = lr
                m = pir["".join(lr)]
                nxt[(l, m)] += count
                nxt[(m, r)] += count
                chars[m] += count
            pairs = nxt
        cv = chars.values()
        return max(cv) - min(cv)


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
