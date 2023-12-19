from collections import defaultdict
from solutions import BaseSolution


N = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


class Solution(BaseSolution):
    input_file = "18.txt"

    def __str__(self):
        return "Day 18: Like a GIF For Your Yard"

    def parse_input(self, data):
        return data.strip()

    def solve(self, data):
        m = defaultdict(bool)
        rows = data.split()
        h = len(rows)
        w = len(rows[0])
        for r in range(h):
            for c in range(w):
                m[(r, c)] = 1 if rows[r][c] == "#" else 0
        for _ in range(100):
            nm = defaultdict(bool)
            for r in range(h):
                for c in range(w):
                    n = sum(m[(r + nr, c + nc)] for nr, nc in N)
                    match m[(r, c)]:
                        case 1:
                            nm[(r, c)] = n in (2, 3)
                        case 0:
                            nm[(r, c)] = n == 3
            m = nm
        return sum(m.values())

    def solve_again(self, data):
        m = defaultdict(bool)
        rows = data.split()
        h = len(rows)
        w = len(rows[0])
        for r in range(h):
            for c in range(w):
                m[(r, c)] = 1 if rows[r][c] == "#" else 0
        m[(0, 0)] = True
        m[(99, 0)] = True
        m[(99, 99)] = True
        m[(0, 99)] = True
        for _ in range(100):
            nm = defaultdict(bool)
            for r in range(h):
                for c in range(w):
                    if (r, c) in [(0, 0), (99, 0), (99, 99), (0, 99)]:
                        nm[(r, c)] = True
                        continue
                    n = sum(m[(r + nr, c + nc)] for nr, nc in N)
                    match m[(r, c)]:
                        case 1:
                            nm[(r, c)] = n in (2, 3)
                        case 0:
                            nm[(r, c)] = n == 3
            m = nm
        return sum(m.values())
        return True


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
