import collections

from solutions import BaseSolution


class Rule:
    size = 0

    def __init__(self, line):
        pattern, output = line.split(' => ')
        self.pattern = pattern.replace('/', '')
        self.output = output.replace('/', '')
        self.size = int(len(self.pattern) ** 0.5)

        self.patterns = [
            self.pattern,
            self._f(self.pattern),
            self._r(self.pattern),
            self._f(self._r(self.pattern)),
            self._r(self._f(self.pattern)),
            self._r(self._r(self.pattern)),
        ]

    def __repr__(self):
        return '[{}] {} -> {}'.format(self.size, self.pattern, self.output)

    def _r(self, b):
        return ''.join(map(lambda g: ''.join(g), zip(*[b[s:s + self.size] for s in range(0, len(b), self.size)][::-1])))

    def _f(self, b):
        return b[-self.size:] + b[self.size:len(b) - self.size] + b[0:self.size]

    def matches(self, canvas):
        return canvas in self.patterns

    def enhance(self, canvas):
        return self.output


class Solution(BaseSolution):
    input_file = '21.txt'

    def __str__(self):
        return 'Day 21: Fractal Art'

    def _get_block(self, canvas, size, n=0):
        s = ''
        cl = int(len(canvas) ** 0.5)
        x = n % (cl // size)
        y = n // (cl // size)
        for r in range(size):
            start = cl * ((y * size) + r) + (x * size)
            end = start + size
            s += canvas[start:end]
        return s

    def _join_blocks(self, blocks):
        bl = len(blocks)
        c = int(bl ** 0.5)
        rl = int(len(blocks[0]) ** 0.5)
        canvas = ''
        for i in range(0, bl, c):
            for j in range(rl):
                canvas += ''.join([block[j * rl:(j + 1) * rl] for block in blocks[i:i + c]])
        return canvas

    def solve(self, puzzle_input, iterations=5):
        canvas = '.#...####'
        rules = [Rule(l.strip()) for l in puzzle_input.splitlines()]
        for _ in range(iterations):
            size = 2 if len(canvas) % 2 == 0 else 3
            blocks = len(canvas) // (size ** 2)
            cb = []
            for b in range(blocks):
                bc = self._get_block(canvas, size, b)
                rule = [r for r in rules if r.matches(bc) and r.size == size]
                if len(rule) > 0:
                    r = rule[0]
                cb.append(r.enhance(bc))
            canvas = self._join_blocks(cb)
        return collections.Counter(canvas)['#']

    def solve_again(self, puzzle_input):
        return self.solve(puzzle_input, 18)


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
