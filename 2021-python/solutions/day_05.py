import re
from itertools import chain
from collections import defaultdict
from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "05.txt"

    def __str__(self):
        return "Day 5: Hydrothermal Venture"

    def parse_input(self, data):
        return list(
            map(
                lambda s: tuple(map(int, re.findall(r"\d+", s))),
                data.strip().splitlines(),
            )
        )

    def solve(self, puzzle_input):
        hv = list(filter(lambda l: l[0] == l[2] or l[1] == l[3], puzzle_input))
        return self._overlaps(hv)

    def solve_again(self, puzzle_input):
        hvd = list(
            filter(
                lambda l: l[0] == l[2] or l[1] == l[3] or self._diagonal(*l),
                puzzle_input,
            )
        )
        return self._overlaps(hvd)

    def _overlaps(self, lines):
        seen = defaultdict(lambda: 0)
        for x1, y1, x2, y2 in lines:
            yn = -1 if y1 > y2 else 1
            xn = -1 if x1 > x2 else 1
            if self._diagonal(x1, y1, x2, y2):
                pl = abs(y1 - y2)
                for n in range(pl + 1):
                    seen[(y1 + n * yn, x1 + n * xn)] += 1
            else:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        seen[(y, x)] += 1
        return sum(map(lambda v: v > 1, seen.values()))

    def _diagonal(self, x1, y1, x2, y2):
        return abs(x1 - x2) == abs(y1 - y2)


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
