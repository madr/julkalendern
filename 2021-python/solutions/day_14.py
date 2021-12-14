from solutions import BaseSolution
from collections import Counter


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
        for _ in range(steps):
            p = []
            for i in range(len(polymer) - 1):
                a, b = polymer[i : i + 2]
                p.append(a)
                s = pir.get(a + b)
                if s:
                    p.append(s)
            p.append(polymer[-1])
            polymer = p
        c = [v for k, v in Counter(polymer).most_common()]
        return max(c) - min(c)


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()

"""
Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
"""
