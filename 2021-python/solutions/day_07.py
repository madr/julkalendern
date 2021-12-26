from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "07.txt"

    def __str__(self):
        return "Day 7: The Treachery of Whales"

    def parse_input(self, data):
        return [int(d) for d in data.strip().split(",")]

    def solve(self, puzzle_input):
        return min(
            [
                sum(abs(start - pos) for start in puzzle_input)
                for pos in range(max(puzzle_input))
            ]
        )

    def solve_again(self, puzzle_input):
        l = sum(range(max(puzzle_input))) * len(puzzle_input)
        for pos in range(max(puzzle_input)):
            l = min(
                l,
                sum(
                    abs(start - pos) + sum(range(abs(start - pos)))
                    for start in puzzle_input
                ),
            )
        return l


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
