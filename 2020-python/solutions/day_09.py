from itertools import combinations

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "09.txt"

    def __str__(self):
        return "Day 9: Encoding Error"

    def parse_input(self, data):
        return [*map(int, data.split())]

    def solve(self, puzzle_input, preamble=25):
        return self.first_invalid_number(puzzle_input, preamble)

    def solve_again(self, data, preamble=25):
        fin = self.solve(data, preamble)
        pos = data.index(fin)
        previous = [*filter(lambda n: n < fin, data[:pos])]
        for r in range(2, len(previous) // 2):
            for i in range(len(previous)):
                if sum(data[i : i + r]) == fin:
                    return min(data[i : i + r]) + max(data[i : i + r])

    def first_invalid_number(self, data, preamble=25):
        for i, n in enumerate(data[preamble:]):
            if not any(x + y == n for x, y in combinations(data[i : preamble + i], 2)):
                return n


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
