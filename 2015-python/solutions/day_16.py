import re
from collections import defaultdict

from solutions import BaseSolution

S = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


class Solution(BaseSolution):
    input_file = "16.txt"

    def __str__(self):
        return "Day 16: fixme"

    def parse_input(self, data):
        return data.strip()

    def solve(self, puzzle_input):
        s = defaultdict(int)
        for i, l in enumerate(puzzle_input.splitlines(), 1):
            for kv in re.findall(r"\w+: \d+", l):
                k, v = kv.split(": ")
                v = int(v)
                s[i] += 1 if k in S and S[k] == v else 0
        return max(s.items(), key=lambda x: x[1])[0]

    def solve_again(self, puzzle_input):
        s = defaultdict(int)
        for i, l in enumerate(puzzle_input.splitlines(), 1):
            for kv in re.findall(r"\w+: \d+", l):
                k, v = kv.split(": ")
                v = int(v)
                match k:
                    case "cats" | "trees":
                        s[i] += 1 if k in S and S[k] < v else 0
                    case "pomeranians" | "goldfish":
                        s[i] += 1 if k in S and S[k] > v else 0
                    case _:
                        s[i] += 1 if k in S and S[k] == v else 0
        return max(s.items(), key=lambda x: x[1])[0]


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
