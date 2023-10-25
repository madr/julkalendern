from itertools import chain
from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "10.txt"

    def __str__(self):
        return "Day 10: Elves Look, Elves Say"

    def parse_input(self, data):
        return data.strip()

    def solve(self, puzzle_input, iterations=40):
        return len(self._sequence(puzzle_input, iterations))

    def solve_again(self, puzzle_input, iterations=50):
        return len(self._sequence(puzzle_input, iterations))

    def _sequence(self, sequence, iterations=40):
        for _ in range(iterations):
            chunks = []
            v = sequence[0]
            counter = 0
            for c in sequence:
                if c == v:
                    counter += 1
                else:
                    chunks.append([str(counter), v])
                    v = c
                    counter = 1
            chunks.append([str(counter), v])
            sequence = "".join(chain(*chunks))
        return sequence


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
