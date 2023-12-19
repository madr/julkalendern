from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "08.txt"

    def __str__(self):
        return "Day 8: Matchsticks"

    def parse_input(self, data):
        return data.split()

    def solve(self, puzzle_input):
        def lendiff(line):
            readable = eval(line)
            return len(line) - len(readable)

        return sum(map(lendiff, puzzle_input))

    def solve_again(self, puzzle_input):
        def lendiff(line):
            encoded = line.replace("\\", "\\\\").replace('"', '\\"')
            return len(encoded) + 2 - len(line)

        return sum(map(lendiff, puzzle_input))


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
