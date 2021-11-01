from collections import deque

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "15.txt"

    def __str__(self):
        return "Day 15: Rambunctious Recitation"

    def parse_input(self, data):
        return [*map(int, data.split(","))]

    def solve(self, puzzle_input):
        return self.speak(puzzle_input, 2020)

    def solve_again(self, puzzle_input):
        return self.speak(puzzle_input, 30000000)

    def speak(self, data, n):
        heard = {}
        starting_numbers = len(data)
        for i, k in enumerate(data):
            heard[k] = i + 1
        last_spoken = 0
        for t in range(starting_numbers + 2, n + 1):
            if last_spoken in heard:
                heard_at = heard[last_spoken]
                heard[last_spoken] = t - 1
                last_spoken = t - 1 - heard_at
            else:
                heard[last_spoken] = t - 1
                last_spoken = 0
        return last_spoken


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
