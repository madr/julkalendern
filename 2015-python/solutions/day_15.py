from itertools import permutations
from math import prod
from re import compile, findall
from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "15.txt"

    def __str__(self):
        return "Day 15: Science for Hungry People"

    def parse_input(self, data):
        digits = compile(r"-?\d+")
        return [
            tuple(map(int, findall(digits, line))) for line in data.strip().splitlines()
        ]

    def solve(self, puzzle_input):
        scores = []
        factors = list(zip(*puzzle_input))[:-1]
        distributions = filter(
            lambda x: sum(x) == 100, permutations(range(1, 100), len(factors[0]))
        )
        for distribution in distributions:
            total = [sum(map(prod, zip(f, distribution))) for f in factors]
            if all(map(lambda x: x > 0, total)):
                scores.append(prod(total))
        return max(scores)

    def solve_again(self, puzzle_input):
        scores = []
        factors = list(zip(*puzzle_input))
        props = factors[:-1]
        calories = factors[-1]
        distributions = filter(
            lambda x: sum(x) == 100, permutations(range(1, 100), len(factors[0]))
        )
        for distribution in distributions:
            calcount = sum(map(prod, zip(calories, distribution)))
            if calcount == 500:
                total = [sum(map(prod, zip(f, distribution))) for f in props]
                if all(map(lambda x: x > 0, total)):
                    scores.append(prod(total))
        return max(scores)


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
