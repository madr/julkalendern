import itertools

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "01.txt"

    def __str__(self):
        return "Day 1: Report Repair"

    def parse_input(self, data):
        return [*map(int, data.split())]

    def solve(self, values):
        for x, y in itertools.combinations(values, 2):
            if x + y == 2020:
                return x * y

    def solve_again(self, values):
        for x, y, z in itertools.combinations(values, 3):
            if x + y + z == 2020:
                return x * y * z


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
