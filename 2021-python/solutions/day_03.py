from collections import Counter
from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "03.txt"

    def __str__(self):
        return "Day 3: Binary Diagnostic"

    def parse_input(self, data):
        return data.split()

    def solve(self, puzzle_input):
        e, g = self._eg(puzzle_input)
        return int("".join(g), 2) * int("".join(e), 2)

    def solve_again(self, puzzle_input):
        og = self._ogco2(puzzle_input, "1")
        co2 = self._ogco2(puzzle_input, "0")
        return int("".join(og), 2) * int("".join(co2), 2)

    def _eg(self, puzzle_input):
        e = []
        g = []
        for r in zip(*puzzle_input):
            x, y = Counter(r).most_common()
            e.append(x[0])
            g.append(y[0])
        return e, g

    def _ogco2(self, values, default, i=0):
        eg = [Counter(r).most_common() for r in zip(*values)]
        k = default if eg[i][0][1] == eg[i][1][1] else eg[i][abs(int(default) - 1)][0]
        rem = [v for v in values if v[i] == k]
        if len(rem) == 1:
            return rem
        return self._ogco2(rem, default, i + 1)


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
