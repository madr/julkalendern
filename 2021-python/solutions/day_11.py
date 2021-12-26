from solutions import BaseSolution
from collections import deque


class Solution(BaseSolution):
    input_file = "11.txt"

    def __str__(self):
        return "Day 11: Dumbo Octopus"

    def parse_input(self, data):
        return [list(map(int, d)) for d in data.split()]

    def solve(self, puzzle_input, steps=100):
        flashes = self._tick(puzzle_input, steps, exit_on_bright=False)
        return flashes

    def solve_again(self, puzzle_input, steps=100):
        brightest = self._tick(puzzle_input, steps, exit_on_bright=True)
        return brightest

    def _debug(self, d):
        print("\n")
        for r in d:
            print("".join(map(str, r)))

    def _tick(self, matrix, steps, exit_on_bright=False):
        my = len(matrix)
        mx = len(matrix[0])
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        f = 0
        # self._debug(matrix)
        counter = 0
        while 1:
            if not exit_on_bright and not counter < steps:
                break
            if exit_on_bright:
                if sum(sum(c for c in r) for r in matrix) == 0:
                    return counter
            matrix = [[(c + 1) % 10 for c in r] for r in matrix]
            flash = deque()
            for y, r in enumerate(matrix):
                for x, v in enumerate(r):
                    if v == 0:
                        flash.append((y, x))
            while flash:
                f += 1
                y, x = flash.popleft()
                for ay, ax in offsets:
                    oy, ox = y + ay, x + ax
                    if oy < 0 or ox < 0 or oy >= my or ox >= mx:
                        continue
                    v = matrix[oy][ox]
                    if v == 0:
                        continue
                    matrix[oy][ox] = (v + 1) % 10
                    if v == 9:
                        flash.append((oy, ox))
            # self._debug(matrix)
            counter += 1
        return f


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
