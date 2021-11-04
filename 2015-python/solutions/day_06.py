from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "06.txt"

    def __str__(self):
        return "Day 6: Probably a Fire Hazard"

    def parse_input(self, data):
        return data

    def solve(self, puzzle_input):
        return True

    def solve_again(self, puzzle_input):
        return True


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
