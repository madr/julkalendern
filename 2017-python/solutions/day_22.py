from collections import Counter

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '22.txt'

    def __str__(self):
        return 'Day 22: Sporifica Virus'

    infected = 0

    def solve(self, puzzle_input, bursts=10000):
        return self._calculate_infected(puzzle_input, bursts)

    def solve_again(self, puzzle_input, bursts=10000000):
        return self._calculate_infected(puzzle_input, bursts, evolved=True)

    def _calculate_infected(self, puzzle_input, bursts, evolved=False):
        dirs, amap, pos = self._setup(puzzle_input)
        for _ in range(bursts):
            amap, state = self._get_state(amap, pos)
            dirs = self._change_dir(dirs, state)
            if not evolved:
                amap = self._update_state(amap, pos)
            else:
                amap = self._update_state_evolved(amap, pos)
            pos = self._move(pos, dirs[0])
        return self.infected

    def _setup(self, puzzle_input):
        self.infected = 0
        dirs = [
            (-1, 0),  # up
            (0, -1),  # right
            (1, 0),  # down
            (0, 1),  # left
        ]
        amap = []
        pil = puzzle_input.strip().splitlines()
        pos = [len(pil) // 2, len(pil[0]) // 2]
        for n, line in enumerate(pil):
            for nn, c in enumerate(line.strip()):
                amap.append([n, nn, c])
        return dirs, amap, pos

    def _change_dir(self, dirs, state):
        if state == ".":
            dirs = dirs[1:] + [dirs[0]]
        elif state == "#":
            dirs = [dirs[3]] + dirs[:3]
        elif state == 'F':
            dirs = dirs[2:] + dirs[:2]
        return dirs

    def _get_state(self, amap, pos):
        t = lambda x: x[1][0] == pos[0] and x[1][1] == pos[1]
        existing = next(filter(t, enumerate(amap)), None)
        if existing:
            i, p = existing
            return amap, p[2]
        else:
            amap.append([pos[0], pos[1], '.'])
            return amap, '.'

    def _update_state(self, amap, pos):
        t = lambda x: x[1][0] == pos[0] and x[1][1] == pos[1]
        existing = next(filter(t, enumerate(amap)))
        i, p = existing
        if p[2] == '.':
            self.infected += 1
        amap[i][2] = '.' if p[2] == '#' else '#'
        return amap

    def _move(self, pos, d):
        return [pos[0] + d[0], pos[1] + d[1]]

    def _update_state_evolved(self, amap, pos):
        t = lambda x: x[1][0] == pos[0] and x[1][1] == pos[1]
        existing = next(filter(t, enumerate(amap)))
        i, p = existing
        if p[2] == '.':
            ns = 'W'
        elif p[2] == 'W':
            self.infected += 1
            ns = "#"
        elif p[2] == '#':
            ns = "F"
        else:
            ns = "."
        amap[i][2] = ns
        return amap


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
