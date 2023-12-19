import re
from itertools import product
from math import inf

from solutions import BaseSolution

SHOP = [
    [
        ("Dagger", 8, 4, 0),
        ("Shortsword", 10, 5, 0),
        ("Warhammer", 25, 6, 0),
        ("Longsword", 40, 7, 0),
        ("Greataxe", 74, 8, 0),
    ],
    [
        ("No armor", 0, 0, 0),
        ("Leather", 13, 0, 1),
        ("Chainmail", 31, 0, 2),
        ("Splintmail", 53, 0, 3),
        ("Bandedmail", 75, 0, 4),
        ("Platemail", 102, 0, 5),
    ],
    [
        ("No ring", 0, 0, 0),
        ("Damage +1", 25, 1, 0),
        ("Damage +2", 50, 2, 0),
        ("Damage +3", 100, 3, 0),
        ("Defense +1", 20, 0, 1),
        ("Defense +2", 40, 0, 2),
        ("Defense +3", 80, 0, 3),
        ("Damage +1 & Damage +2", 75, 3, 0),
        ("Damage +1 & Damage +3", 125, 4, 0),
        ("Damage +1 & Defense +1", 45, 1, 1),
        ("Damage +1 & Defense +2", 65, 1, 2),
        ("Damage +1 & Defense +3", 105, 1, 3),
        ("Damage +2 & Damage +3", 150, 5, 0),
        ("Damage +2 & Defense +1", 70, 2, 1),
        ("Damage +2 & Defense +2", 90, 2, 2),
        ("Damage +2 & Defense +3", 130, 2, 3),
        ("Damage +3 & Defense +1", 120, 3, 1),
        ("Damage +3 & Defense +2", 140, 3, 2),
        ("Damage +3 & Defense +3", 180, 3, 3),
        ("Defense +1 & Defense +2", 60, 0, 3),
        ("Defense +1 & Defense +3", 100, 0, 4),
        ("Defense +2 & Defense +3", 120, 0, 5),
    ],
]


class Solution(BaseSolution):
    input_file = "21.txt"

    def __str__(self):
        return "Day 21: RPG Simulator 20XX"

    def solve(self, pi):
        o = self._solve(pi)
        return o[0]

    def solve_again(self, pi):
        o = self._solve(pi)
        return o[1]

    def parse_input(self, data):
        return data.strip()

    def _solve(self, pi):
        boss = re.findall(r"\d+", pi)
        l = inf
        m = 0
        for ph, pd, pa, c in self._gearup():
            bh, bd, ba = [int(v) for v in boss]
            while bh > 0 and ph > 0:
                bh -= max(1, pd - ba)
                if bh <= 0:
                    break
                ph -= max(1, bd - pa)
            if ph > 0:
                l = min(l, c)
            else:
                m = max(m, c)
        return l, m

    def _gearup(self):
        g = []
        for w, a, r in product(*SHOP):
            g.append(
                (
                    100,
                    sum([w[2], a[2], r[2]]),
                    sum([w[3], a[3], r[3]]),
                    sum([w[1], a[1], r[1]]),
                )
            )
        return g


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
