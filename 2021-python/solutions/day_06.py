from solutions import BaseSolution
from collections import Counter, deque


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
        f = Counter(puzzle_input)
        s = deque([0] * 9)
        for i in range(9):
            s[i] = f[i]
        for _d in range(tf):
            e = s.popleft()
            s[6] += e
            s.append(e)
        return sum(s)


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
