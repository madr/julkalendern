import itertools
from collections import defaultdict, Counter

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '06.in'

    def __str__(self):
        return 'Day 6: Chronal Coordinates'

    def solve(self, puzzle_input):
        locations = [tuple(map(int, pi.split(', '))) for pi in puzzle_input.splitlines()]
        finite_locations, cols, rows = self._location_boundaries(locations)
        closest = defaultdict(int)
        for coordinate in itertools.product(cols, rows):
            distances = self._manhattan_distance(coordinate, locations)
            closest[coordinate] = '.' if distances[0][1] == distances[1][1] else distances[0][0]
        _location, count = [lc for lc in Counter(closest.values()).most_common() if lc[0] not in finite_locations][0]
        return count

    def solve_again(self, puzzle_input):
        return self.get_region(puzzle_input, 10000)

    def get_region(self, puzzle_input, max_distance):
        locations = [tuple(map(int, pi.split(', '))) for pi in puzzle_input.splitlines()]
        finite_locations, cols, rows = self._location_boundaries(locations)
        region = set()
        for coordinate in itertools.product(cols, rows):
            distances = self._manhattan_distance(coordinate, locations)
            if sum(map(lambda x: x[1], distances)) < max_distance:
                region.add(coordinate)
        return len(region)

    def _manhattan_distance(self, coordinate, locations):
        distances = [(i, abs(abs(target[0] - coordinate[0]) + abs(target[1] - coordinate[1])))
                     for i, target in enumerate(locations)]
        return sorted(distances, key=lambda x: x[1])

    def _location_boundaries(self, locations):
        min_width, min_height = map(min, zip(*locations))
        max_width, max_height = map(max, zip(*locations))
        finite_locations = [i for i, l in enumerate(locations) if l[0] not in (min_width, max_width)
                            and l[1] in (min_height, max_height)]
        return finite_locations, range(min_width, max_width), range(min_height, max_height)


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
