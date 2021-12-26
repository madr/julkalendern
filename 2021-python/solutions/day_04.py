from itertools import chain

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "04.txt"

    def __str__(self):
        return "Day 4: Day 4: Giant Squid"

    def parse_input(self, data):
        queue, *boards = data.strip().split("\n\n")
        queue = list(map(int, queue.split(",")))
        boards = [[list(map(int, r.split())) for r in b.splitlines()] for b in boards]
        return queue, boards

    def solve(self, puzzle_input):
        queue, boards = puzzle_input
        called, winner, _i = self._play(queue, boards)
        return self._score(called, winner)

    def solve_again(self, puzzle_input):
        queue, boards = puzzle_input
        while (len(boards)) > 0:
            called, winner, i = self._play(queue, boards)
            del boards[i]
        return self._score(called, winner)

    def _score(self, called, winner):
        return called[-1] * sum(set(chain(*winner)) - set(called))

    def _play(self, queue, boards):
        def bingo(called, numbers):
            return numbers.issubset(called)

        boards = list(
            map(
                lambda r: {"rows": list(map(set, r)), "cols": list(map(set, zip(*r)))},
                boards,
            )
        )
        for i in range(5, len(queue)):
            called = queue[:i]
            for i, b in enumerate(boards):
                if any(bingo(called, r) for r in b["rows"]) or any(
                    bingo(called, c) for c in b["cols"]
                ):
                    return called, b["rows"], i


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
