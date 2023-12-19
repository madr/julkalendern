import re
from itertools import combinations
from math import prod

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "24.txt"

    def __str__(self):
        return "Day 24: Hangs in the Balance"

    def solve(self, pi):
        o = self._solve(pi)
        return o[0]

    def solve_again(self, pi):
        o = self._solve(pi)
        return o[1]

    def _solve(self, pi):
        p12 = []
        for g in [3, 4]:
            w = [int(s) for s in re.findall(r"\d+", pi)]
            gs = sum(w) // g
            c = []
            for r in range(len(w)):
                for n in combinations(w, r=r):
                    if sum(n) == gs:
                        c.append(n)
                if c:
                    break
            p12.append(min(map(prod, c)))
        return p12

    def parse_input(self, data):
        return data.strip()


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
