from collections import deque
from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "10.txt"

    def __str__(self):
        return "Day 10: Syntax Scoring"

    def parse_input(self, data):
        return data.split()

    def solve(self, puzzle_input):
        scores = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137,
        }
        co = {"]": "[", "}": "{", ">": "<", ")": "("}
        openers = co.values()
        closers = co.keys()

        def corrupt(l):
            o = deque()
            for i, c in enumerate(l):
                if c in openers:
                    o.append(c)
                    continue
                if co[c] != o.pop():
                    return i, c
            else:
                return 0

        lines = list(filter(corrupt, puzzle_input))
        return sum(scores[c] for _, c in map(corrupt, lines))

    def solve_again(self, puzzle_input):
        scoremap = {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4,
        }
        co = {"]": "[", "}": "{", ">": "<", ")": "("}
        oc = dict([(o, c) for c, o in co.items()])
        openers = co.values()
        closers = co.keys()

        def score(chars):
            s = 0
            for i, x in enumerate(chars):
                s *= 5
                s += scoremap[x]
            return s

        def incomplete(l):
            o = deque()
            for c in l:
                if c in openers:
                    o.append(c)
                    continue
                if co[c] != o.pop():
                    return 0
            else:
                return o

        lines = list(filter(incomplete, puzzle_input))
        med = len(lines) // 2
        completes = [
            score([oc[oo] for oo in reversed(o)]) for o in map(incomplete, lines)
        ]
        return sorted(completes)[med]
        return True


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
