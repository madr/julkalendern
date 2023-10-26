from collections import defaultdict
from itertools import permutations, pairwise
from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "13.txt"

    def __str__(self):
        return "Day 13: Knights of the Dinner Table"

    def parse_input(self, data):
        lines = defaultdict(int)

        def parseline(line):
            a, _w, gain_or_lose, value, _h, _u, _b, _s, _n, _t, b = line.split()
            units = -int(value) if gain_or_lose == "lose" else int(value)
            return (f"{a}-{b[:-1]}", units)

        for k, v in [parseline(line) for line in data.strip().splitlines()]:
            lines[k] = v

        return lines

    def _solve(self, people, puzzle_input):
        def happiness(seats):
            neighbours = list(pairwise(seats))
            neighbours.append((seats[0], seats[-1]))
            return sum(
                [
                    sum(puzzle_input["-".join([a, b])] for a, b in neighbours),
                    sum(puzzle_input["-".join([b, a])] for a, b in neighbours[::-1]),
                ]
            )

        return max(happiness(seats) for seats in permutations(people, len(people)))

    def solve(self, puzzle_input):
        people = set([ab.split("-")[0] for ab, _v in puzzle_input.items()])
        return self._solve(people, puzzle_input)

    def solve_again(self, puzzle_input):
        people = set([ab.split("-")[0] for ab, _v in puzzle_input.items()])
        people.add("-")
        return self._solve(people, puzzle_input)


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
