import re

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "05.txt"

    def __str__(self):
        return "Day 5: Doesn't He Have Intern-Elves For This?"

    def solve(self, pi):
        return self._solve(pi)[0]

    def solve_again(self, pi):
        return self._solve(pi)[1]

    def parse_input(self, data):
        return data.strip()

    def _solve(self, pi):
        wl = pi.split()
        p1 = sum(
            not re.search(r"ab|cd|pq|xy.*", w)
            and any(w[i] == w[i + 1] for i in range(len(w) - 1))
            and len(re.findall(r"[aeiou]", w)) > 2
            for w in wl
        )
        p2 = sum(
            any(w.count(w[i : i + 2]) == 2 for i in range(len(w) - 1))
            and any(w[i] == w[i + 2] for i in range(len(w) - 2))
            for w in wl
        )
        return p1, p2


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
