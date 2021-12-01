from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "01.txt"

    def __str__(self):
        return "Day 1: Sonar Sweep"

    def parse_input(self, data):
        return [int(n) for n in data.split()]

    def solve(self, puzzle_input):
        return sum(
            [puzzle_input[i] > puzzle_input[i - 1] for i in range(1, len(puzzle_input))]
        )

    def solve_again(self, puzzle_input):
        puzzle_input.append(max(puzzle_input) + 1)
        return sum(
            [
                (puzzle_input[i] + puzzle_input[i - 1] + puzzle_input[i - 2])
                > (puzzle_input[i - 1] + puzzle_input[i - 2] + puzzle_input[i - 3])
                for i in range(2, len(puzzle_input) - 1)
            ]
        )


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
