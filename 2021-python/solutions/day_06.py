from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "06.txt"

    def __str__(self):
        return "Day 6: Lanternfish"

    def parse_input(self, data):
        return list(map(int, data.strip().split(",")))

    def solve(self, puzzle_input):
        return self._produce(puzzle_input, 80)

    def solve_again(self, puzzle_input):
        return self._produce(puzzle_input, 256)

    def _produce(self, puzzle_input, tf):
        f = [*puzzle_input]
        for _ in range(tf):
            n = [8 for __ in range(sum(x <= 0 and x % 7 == 0 for x in f))]
            f = list(map(lambda x: x - 1, f))
            f.extend(n)
        return len(f)


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
