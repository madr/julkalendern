from itertools import permutations
from re import findall
from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "09.txt"

    def __str__(self):
        return "Day 9: All in a Single Night"

    def parse_input(self, data):
        def fromtodest(line):
            f, t, d = findall(r"(\w+) to (\w+) = (\d+)", line)[0]
            return f, t, int(d)

        return [fromtodest(line) for line in data.strip().splitlines()]

    def solve(self, puzzle_input):
        return min(self._distances(puzzle_input))

    def solve_again(self, puzzle_input):
        return max(self._distances(puzzle_input))

    def _distances(self, puzzle_input):
        places = set(
            list(map(lambda sdd: sdd[0], puzzle_input))
            + list(map(lambda ssd: ssd[1], puzzle_input))
        )
        route_len = len(places)

        return [
            sum(
                sum(
                    map(
                        lambda ssd: ssd[2],
                        filter(
                            lambda ssd: (
                                (ssd[0] == route[i] and ssd[1] == route[i + 1])
                                or (ssd[0] == route[i + 1] and ssd[1] == route[i])
                            ),
                            puzzle_input,
                        ),
                    )
                )
                for i in range(route_len - 1)
            )
            for route in permutations(places)
        ]


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
