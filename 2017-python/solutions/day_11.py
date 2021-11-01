from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '11.txt'
    furthest_away = 0
    # https://www.redblobgames.com/grids/hexagons/#coordinates
    DIRECTIONS = {
        'n': lambda x, y, z: (x, y + 1, z - 1),
        'ne': lambda x, y, z: (x + 1, y, z - 1),
        'se': lambda x, y, z: (x + 1, y - 1, z),
        's': lambda x, y, z: (x, y - 1, z + 1),
        'sw': lambda x, y, z: (x - 1, y, z + 1),
        'nw': lambda x, y, z: (x - 1, y + 1, z),
    }

    def __str__(self):
        return 'Day 11: Hex Ed'

    def _get_end(self, steps):
        x = 0
        y = 0
        z = 0
        self.furthest_away = 0
        for step in steps:
            x, y, z = self.DIRECTIONS[step](x, y, z)
            self.furthest_away = max(self.furthest_away, abs(x), abs(y), abs(z))
        return abs(x), abs(y), abs(z)

    def solve(self, puzzle_input):
        x, y, z = self._get_end(puzzle_input.split(','))
        return max(x, y, z)

    def solve_again(self, puzzle_input):
        _, *__ = self._get_end(puzzle_input.split(','))
        return self.furthest_away


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
