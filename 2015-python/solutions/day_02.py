from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "02.txt"

    def __str__(self):
        return "Day 2: I Was Told There Would Be No Math"

    def solve(self, pi):
        o = self._solve(pi)
        return o[0]

    def solve_again(self, pi):
        o = self._solve(pi)
        return o[1]

    def _solve(self, pi):
        p1 = 0
        p2 = 0
        for p in pi.splitlines():
            l, w, h = sorted([int(s) for s in p.split("x")])
            p1 += 2 * (l * w + w * h + h * l) + min([l * w, w * h, h * l])
            p2 += 2 * l + 2 * w + l * w * h
        return p1, p2

    def parse_input(self, data):
        return data.strip()


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
