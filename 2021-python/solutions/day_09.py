from solutions import BaseSolution
from typing import List, Tuple


class Solution(BaseSolution):
    input_file = "09.txt"

    def __str__(self):
        return "Day 9: Smoke Basin"

    def parse_input(self, data):
        return [[int(c) for c in r] for r in data.split()]

    def solve(self, puzzle_input):
        lp = self._lowpoints(puzzle_input)
        return sum(lpv[1] + 1 for lpv in lp)

    def solve_again(self, puzzle_input):
        offsets = (-1, 0), (0, 1), (1, 0), (0, -1)
        my = len(puzzle_input)
        mx = len(puzzle_input[0])

        basins = []

        def basin(y, x, value, seen=set()):
            if value < 9:
                seen.add((value, (y, x)))
                for oy, ox in offsets:
                    sy = y + oy
                    sx = x + ox
                    if any((sy < 0, sx < 0, sy >= my, sx >= mx)):
                        continue
                    s = puzzle_input[sy][sx]
                    if s > value:
                        seen = basin(sy, sx, s, seen)
            return seen

        for lp, value in self._lowpoints(puzzle_input):
            y, x = lp
            basins.append(len(basin(y, x, value, set())))
        p1, p2, p3, *_ = sorted(basins, reverse=True)
        return p1 * p2 * p3

    def _lowpoints(self, puzzle_input):
        lp = []
        lpi = len(puzzle_input)
        for v, row in enumerate(puzzle_input):
            lr = len(row)
            for i in range(lr):
                x = row[i]
                s1 = row[i - 1] if i > 0 else 11
                s2 = row[i + 1] if i < lr - 1 else 11
                s3 = puzzle_input[v - 1][i] if v > 0 else 11
                s4 = puzzle_input[v + 1][i] if v < lpi - 1 else 11
                if all(x < s for s in [s1, s2, s3, s4]):
                    lp.append(((v, i), x))
        return lp


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()

"""
2199943210
3987894921
9856789892
8767896789
9899965678
"""
