from solutions import BaseSolution


class Cart:
    curves = ['\\', '/']
    intersection = '+'
    direction_keys = {
        'LEFT': '<',
        'DOWN': 'v',
        'RIGHT': '>',
        'UP': '^',
    }

    def __repr__(self):
        return '[{}] {} at ({},{})'.format(int(self.crashed), self.direction, self.y, self.x)

    def __init__(self, y, x, direction):
        self.rotations = 0
        self.direction = direction
        self.y = y
        self.x = x
        self.crashed = False

    @property
    def pos(self):
        return self.y, self.x

    def move(self, t, l):
        self.y += t
        self.x += l

    def rotate(self, p):
        if p in self.curves:
            if p == '/':
                if self.direction == self.direction_keys['UP']:
                    self.direction = self.direction_keys['RIGHT']
                elif self.direction == self.direction_keys['RIGHT']:
                    self.direction = self.direction_keys['UP']
                elif self.direction == self.direction_keys['DOWN']:
                    self.direction = self.direction_keys['LEFT']
                elif self.direction == self.direction_keys['LEFT']:
                    self.direction = self.direction_keys['DOWN']
            elif p == '\\':
                if self.direction == self.direction_keys['UP']:
                    self.direction = self.direction_keys['LEFT']
                elif self.direction == self.direction_keys['LEFT']:
                    self.direction = self.direction_keys['UP']
                elif self.direction == self.direction_keys['DOWN']:
                    self.direction = self.direction_keys['RIGHT']
                elif self.direction == self.direction_keys['RIGHT']:
                    self.direction = self.direction_keys['DOWN']
        if p == self.intersection:
            if self.rotations % 3 == 0:
                if self.direction == self.direction_keys['UP']:
                    self.direction = self.direction_keys['LEFT']
                elif self.direction == self.direction_keys['LEFT']:
                    self.direction = self.direction_keys['DOWN']
                elif self.direction == self.direction_keys['DOWN']:
                    self.direction = self.direction_keys['RIGHT']
                elif self.direction == self.direction_keys['RIGHT']:
                    self.direction = self.direction_keys['UP']
            if self.rotations % 3 == 2:
                if self.direction == self.direction_keys['UP']:
                    self.direction = self.direction_keys['RIGHT']
                elif self.direction == self.direction_keys['RIGHT']:
                    self.direction = self.direction_keys['DOWN']
                elif self.direction == self.direction_keys['DOWN']:
                    self.direction = self.direction_keys['LEFT']
                elif self.direction == self.direction_keys['LEFT']:
                    self.direction = self.direction_keys['UP']
            self.rotations += 1


class Solution(BaseSolution):
    input_file = '13.in'
    trim_input = False
    verbose = False  # True will visualize each tick

    def __str__(self):
        return 'Day 13: Mine Cart Madness'

    directions = {
        'v': (0, 1),
        '^': (0, -1),
        '>': (1, 0),
        '<': (-1, 0),
    }

    def solve(self, puzzle_input):
        lines, carts = self._get_carts(puzzle_input)
        crashes = []
        while len(crashes) == 0:
            self._print(lines, carts)
            carts, crashes = self.tick(lines, carts)
        y, x = crashes.pop()
        return '{},{}'.format(x, y)

    def solve_again(self, puzzle_input):
        lines, carts = self._get_carts(puzzle_input)
        while len(carts) > 1:
            self._print(lines, carts)
            carts, _ = self.tick(lines, carts)
        remaining = carts.pop()
        y, x = remaining.pos
        return '{},{}'.format(x, y)

    def tick(self, lines, carts):
        # Another rant about the examples of this years Advent of code. The
        # example for day 13 did not include a clear example of how to handle
        # these 2 scenarios:
        #
        #                           |
        #     -><-                  v
        #                           ^
        #                           |
        #
        # The example only provided the scenario of these:
        #
        #                           |
        #                           v
        #     ->-<-                 |
        #                           ^
        #                           |
        #
        # This means that using the example as a test case will make the test
        # pass, but give the wrong solution when the real puzzle input is applied.
        #
        # It is unnecessary to mention that the puzzle input is REALLY HARD to
        # debug manually, since it is way more complex.
        #
        # I figured it out from the subreddit, where several people cryptically
        # mentioned that the order matters of the carts, and by visualizing each
        # tick, seeing that my code did not handle all scenarios.
        #
        # The final solution was to drown my code in unit tests, which of course
        # is good anyway.
        #
        # What irritates me is that this year's Advent of Code have had many
        # "slamkrypare" by providing examples that are not enough, and instead
        # some cryptic wording in the description must be read over and over to
        # solve the puzzle.
        for cid, cart in enumerate(carts):
            if cart.crashed:
                continue
            l, t = self.directions[cart.direction]
            cart.move(t, l)
            y, x = cart.pos
            for cid2, other_cart in enumerate(carts):
                if cid != cid2 and other_cart.y == y and other_cart.x == x and not other_cart.crashed:
                    cart.crashed = True
                    other_cart.crashed = True
            cart.rotate(lines[y][x])
        crashes = list(set([c.pos for c in carts if c.crashed]))
        updated = [c for c in carts if not c.crashed]
        return sorted(updated, key=lambda o: o.pos), crashes

    def _print(self, lines, carts):
        if self.verbose:
            canvas = list()
            ls = lines.copy()
            for cart in carts:
                c = cart.direction
                y, x = cart.pos
                if ls[y][x] in self.directions.keys():
                    c = 'X'
                ls[y] = ls[y][:x] + c + ls[y][x + 1:]
            for l in ls:
                canvas.append(''.join(l))
            canvas = '\n'.join(canvas)
            print(canvas)

    def _get_carts(self, puzzle_input):
        pattern = self.directions.keys()
        carts = list()
        lines = puzzle_input.splitlines()
        for y, line in enumerate(lines):
            for x, cart in enumerate(line):
                if cart in pattern:
                    carts.append(Cart(y, x, cart))
        lines = puzzle_input.replace('>', '-').replace('<', '-').replace('v', '|').replace('^', '|').splitlines()
        return lines, sorted(carts, key=lambda c: c.pos)


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
