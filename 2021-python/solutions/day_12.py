from solutions import BaseSolution
from collections import defaultdict, deque, Counter


class Solution(BaseSolution):
    input_file = "12.txt"

    def __str__(self):
        return "Day 12: Passage Pathing"

    def parse_input(self, data):
        return [l.split("-") for l in data.split()]

    def solve(self, puzzle_input):
        return self._solve(puzzle_input, lambda seen: True)

    def solve_again(self, puzzle_input):
        return self._solve(
            puzzle_input,
            lambda seen: any(
                [
                    k.islower() and k != "start" and v > 1
                    for k, v in Counter(seen).items()
                ]
            ),
        )

    def _solve(self, puzzle_input, isdup):
        ft = defaultdict(lambda: [])
        for f, t in puzzle_input:
            ft[f].append(t)
        for f, t in puzzle_input:
            ft[t].append(f)
        queue = deque([("start", list(), False)])
        s2e = 0
        while queue:
            pos, seen, dup = queue.pop()
            seen.append(pos)
            dup = isdup(seen)
            for t in ft[pos]:
                if t == "end":
                    s2e += 1
                    continue
                elif t == "start":
                    continue
                elif dup and t.islower() and t in seen:
                    continue
                queue.append((t, seen + [], dup))
        return s2e


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
