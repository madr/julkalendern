from collections import defaultdict

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "03.txt"

    def __str__(self):
        return "Day 3: Perfectly Spherical Houses in a Vacuum"

    def solve(self, pi):
        return self._solve(pi)[0]

    def solve_again(self, pi):
        return self._solve(pi)[1]

    def _solve(self, pi):
        def f(q):
            p = (0, 0)
            vs = defaultdict(int)
            vs[p] += 1
            for d in q:
                r, c = p
                match d:
                    case "^":
                        p = (r - 1, c)
                    case ">":
                        p = (r, c + 1)
                    case "v":
                        p = (r + 1, c)
                    case "<":
                        p = (r, c - 1)
                vs[p] += 1
            return set(vs.keys())

        p1 = len(f(pi))
        p2 = len(f(pi[0::2]) | f(pi[1::2]))
        return p1, p2

    def parse_input(self, data):
        return data.strip()


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
