from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "01.txt"

    def __str__(self):
        return "Day 1: Not Quite Lisp"

    def solve(self, pi):
        return sum([-1 if c == ")" else 1 for c in pi])

    def solve_again(self, pi):
        f = 1
        for i, v in enumerate(pi):
            f += -1 if v == ")" else 1
            if f == -1:
                return i

    def parse_input(self, data):
        return data.strip()


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
