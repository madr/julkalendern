import re
from collections import defaultdict

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "06.txt"

    def __str__(self):
        return "Day 6: Probably a Fire Hazard"

    def parse_input(self, data):
        return data.strip()

    def solve(self, puzzle_input):
        m = defaultdict(bool)
        for ase in puzzle_input.splitlines():
            p = re.match(r"^(.+) (\d+),(\d+)\D+(\d+),(\d+)", ase).groups()
            a, sx, sy, ex, ey = p
            for r in range(int(sy), int(ey) + 1):
                for c in range(int(sx), int(ex) + 1):
                    match a:
                        case "toggle":
                            m[(r, c)] = not m[(r, c)]
                        case "turn on":
                            m[(r, c)] = True
                        case "turn off":
                            m[(r, c)] = False
        p1 = sum(m.values())
        assert p1 == 569999
        return sum(m.values())

    def solve_again(self, puzzle_input):
        m = defaultdict(int)
        for ase in puzzle_input.splitlines():
            p = re.match(r"^(.+) (\d+),(\d+)\D+(\d+),(\d+)", ase).groups()
            a, sx, sy, ex, ey = p
            for r in range(int(sy), int(ey) + 1):
                for c in range(int(sx), int(ex) + 1):
                    match a:
                        case "toggle":
                            m[(r, c)] += 2
                        case "turn on":
                            m[(r, c)] += 1
                        case "turn off":
                            m[(r, c)] = max(m[(r, c)] - 1, 0)
        p2 = sum(m.values())
        assert p2 == 17836115
        return p2


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
