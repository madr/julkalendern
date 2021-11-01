from collections import Counter

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "06.txt"

    def __str__(self):
        return "Day 6: Custom Customs"

    def parse_input(self, data):
        return [g.split() for g in data.split("\n\n")]

    def solve(self, puzzle_input):
        return sum(self.count_any_yes_answers(g) for g in puzzle_input)

    def solve_again(self, puzzle_input):
        return sum(self.count_every_yes_answers(g) for g in puzzle_input)

    def count_any_yes_answers(self, groupdata):
        return len(set("".join(groupdata)))

    def count_every_yes_answers(self, groupdata):
        groupsize = len(groupdata)
        answer_counts = Counter("".join(groupdata))
        return sum(v == groupsize for _k, v in answer_counts.items())


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
