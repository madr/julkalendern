import itertools

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '13.txt'
    layers = []
    scanners = []

    def __str__(self):
        return 'Day 13: Packet Scanners'

    def _move_scanners(self):
        for p, l in enumerate(self.layers):
            if l != 0:
                self.scanners[p][0] += self.scanners[p][1]
                if self.scanners[p][0] == l - 1 or self.scanners[p][0] == 0:
                    self.scanners[p][1] = -self.scanners[p][1]

    def _init_scanners(self):
        self.scanners = [[0, 1] for l in self.layers]

    def _setup(self, puzzle_input):
        pi = [tuple(map(int, line.strip().split(': '))) for line in puzzle_input.splitlines()]
        self.layers = [0 for _ in range(pi[-1][0] + 1)]
        self._init_scanners()
        for k, v in pi:
            self.layers[k] = v

    def _get_severity(self):
        severity = 0
        for pos in range(len(self.layers)):
            if self.scanners[pos][0] == 0 and self.layers[pos] > 0:
                severity += self.layers[pos] * pos
            self._move_scanners()
        return severity

    def _will_be_caught(self):
        caught = False
        for pos, l in enumerate(self.layers):
            if l > 0 and self.scanners[pos][0] == 0:
                caught = True
            self._move_scanners()
        return caught

    def solve(self, puzzle_input):
        self._setup(puzzle_input)
        severity = self._get_severity()
        return severity

    def _scan(self, height, time):
        offset = time % ((height - 1) * 2)
        return 2 * (height - 1) - offset if offset > height - 1 else offset

    def solve_again(self, puzzle_input):
        # todo: rewrite!
        lines = [line.split(': ') for line in puzzle_input.splitlines()]
        heights = {int(pos): int(height) for pos, height in lines}
        wait = next(
            wait for wait in itertools.count() if not any(self._scan(heights[pos], wait + pos) == 0 for pos in heights))
        return wait


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
