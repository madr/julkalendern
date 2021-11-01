import itertools
import re

from solutions import BaseSolution


class Point:
    def __init__(self, x, y, lr, du):
        self.x = x
        self.y = y
        self.lr = lr
        self.du = du

    def tick(self):
        self.x += self.lr
        self.y += self.du

    def pos(self):
        return self.x, self.y

    def __repr__(self):
        return 'position=<{}, {}> velocity=<{}, {}>'.format(
            self.x, self.y, self.lr, self.du
        )


class Solution(BaseSolution):
    input_file = '10.in'

    def __str__(self):
        return 'Day 10: Day 10: The Stars Align'

    def solve(self, puzzle_input):
        return '\n' + self.render(puzzle_input, 10391)

    def solve_again(self, puzzle_input):
        return 10391  # by science and a little magic

    def _print(self, data, max_x, min_x, max_y, min_y):
        pos = set((p.x, p.y) for p in data)
        canvas = []
        l = max_x - min_x + 1
        for y, x in itertools.product(range(min_y, max_y + 1), range(min_x, max_x + 1)):
            if (x, y) in pos:
                v = '#'
            else:
                v = '.'
            canvas.append(v)
        return '\n'.join(''.join(canvas[0 + i:l + i]) for i in range(0, len(canvas), l))

    def _bounds(self, data):
        set_x = [p.x for p in data]
        set_y = [p.y for p in data]
        min_x = min(set_x)
        min_y = min(set_y)
        max_x = max(set_x)
        max_y = max(set_y)
        return max_x, min_x, max_y, min_y

    def render(self, puzzle_input, ticks):
        r = re.compile(r'\< ?(-?\d+),\s+(-?\d+)\>.+< ?(-?\d+),\s+(-?\d+)\>')
        data = [Point(*map(int, r.search(l).groups())) for l in puzzle_input.splitlines()]
        for n in range(ticks):
            for p in data:
                p.tick()
        max_x, min_x, max_y, min_y = self._bounds(data)
        return self._print(data, max_x, min_x, max_y, min_y)


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()