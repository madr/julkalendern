from collections import defaultdict
from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "20.txt"

    def __str__(self):
        return "Day 20: Infinite Elves and Infinite Houses"

    def solve(self, pi):
        S = 36_000_000
        # hn = 831601
        # x1 = defaultdict(int)
        # for i in range(1, hn):
        #     for n in range(0, hn, i):
        #         if n == 0:
        #             continue
        #         x1[n] += i * 10
        # for k, v in x1.items():
        #     if v >= S:
        #         print(k, v)
        hn = 885000
        hc = 50
        x2 = defaultdict(int)
        for i in range(1, hn):
            for n in range(0, hc * i + 1, i):
                if n == 0:
                    continue
                x2[n] += i * 11
        # p1 = max(x1.items(), key=lambda y: y[1])[0]
        p2 = min(filter(lambda x: x[1] >= S, x2.items()), key=lambda y: y[0])[0]
        return 0, p2

    def solve_again(self, pi):
        return pi

    def parse_input(self, data):
        return data.strip()


if __name__ == "__main__":
    solution = Solution()
    # solution.show_results()

    dummy = """
    replace me
    """.strip()

    print(solution.solve(dummy))
    # solution.solve_again(dummy)
