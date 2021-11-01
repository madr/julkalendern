from solutions import BaseSolution
from functools import lru_cache


class Solution(BaseSolution):
    input_file = "10.txt"

    def __str__(self):
        return "Day 10: Adapter Array"

    def parse_input(self, data):
        return [*map(int, data.split())]

    def solve(self, adapters):
        stop_at = max(adapters)
        mj = 0
        i = 0
        iii = 0
        while mj < stop_at:
            if mj + 1 in adapters:
                mj += 1
                i += 1
            elif mj + 3 in adapters:
                mj += 3
                iii += 1
        iii += 1
        return i * iii

    def solve_again(self, adapters):
        the_end = max(adapters)
        r = range(1, 4)

        @lru_cache
        def investigate(joltage):
            if joltage == the_end:
                return 1
            combinations_count = 0
            for i in r:
                if joltage + i not in adapters:
                    continue
                combinations_count += investigate(joltage + i)
            return combinations_count

        return investigate(0)


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
