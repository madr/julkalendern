from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "09.txt"

    def __str__(self):
        return "Day 9: Smoke Basin"

    def parse_input(self, data):
        return [[int(c) for c in r] for r in data.split()]

    def solve(self, puzzle_input):
        lp = 0
        lpi = len(puzzle_input)
        for v, row in enumerate(puzzle_input):
            lr = len(row)
            for i in range(lr):
                x = row[i]
                s1 = row[i - 1] if i > 0 else 11
                s2 = row[i + 1] if i < lr - 1 else 11
                s3 = puzzle_input[v - 1][i] if v > 0 else 11
                s4 = puzzle_input[v + 1][i] if v < lpi - 1 else 11
                if all(x < s for s in [s1, s2, s3, s4]):
                    lp += 1 + x
        return lp

    def solve_again(self, puzzle_input):
        return True


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
