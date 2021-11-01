import re

import collections

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '20.txt'

    def __str__(self):
        return 'Day 20: Particle Swarm'

    def _get_particle(self, line):
        return [list(map(int, coordinate.split(','))) for coordinate in re.findall(r'.=<([^>]+)>', line)]

    def solve(self, puzzle_input, ticks=10 ** 4):
        particles = [self._get_particle(line) for line in puzzle_input.splitlines()]
        distances = [[] for _ in range(len(particles))]
        for _ in range(ticks):
            for i, particle in enumerate(particles):
                p, v, a = particle
                v[0] += a[0]
                v[1] += a[1]
                v[2] += a[2]
                p[0] += v[0]
                p[1] += v[1]
                p[2] += v[2]
                distances[i].append(sum(map(abs, p)))
        d = sorted(map(lambda d: (d[0], sum(d[1]) / len(d[1])), enumerate(distances)), key=lambda x: x[1])
        return d[0][0]

    def solve_again(self, puzzle_input, ticks=10 ** 3):
        particles = [self._get_particle(line) for line in puzzle_input.splitlines()]
        for _ in range(ticks):
            positions = collections.defaultdict(list)
            for particle in particles:
                p, v, a = particle
                v[0] += a[0]
                v[1] += a[1]
                v[2] += a[2]
                p[0] += v[0]
                p[1] += v[1]
                p[2] += v[2]
                k = '-'.join(map(str, p))
                positions[k].append(particle)
            for duplicates in positions.values():
                if len(duplicates) > 1:
                    for d in duplicates:
                        particles.remove(d)
        return len(particles)


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
