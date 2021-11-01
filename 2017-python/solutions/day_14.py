from solutions import BaseSolution
from solutions.day_10 import Solution as KnotHash


class Solution(BaseSolution):
    input_file = '14.txt'

    def __str__(self):
        return 'Day 14: Disk Defragmentation'

    def _get_grid(self, pi):
        grid = ''
        ks = KnotHash()
        for n in range(128):
            s = '-'.join([pi, str(n)])
            knothash = ks.solve_again(s)
            grid += '{:0128b}'.format(int(knothash, 16))
        return grid

    def _find_regions(self, squares):
        seen = set()
        regions = 0

        def get_adjacent_square(i):
            if i in seen or i not in squares:
                return
            seen.add(i)
            if i % 128 > 0:
                get_adjacent_square(i - 1)
            if i > 127:
                get_adjacent_square(i - 128)
            if i % 128 < 127:
                get_adjacent_square(i + 1)
            if i < 128 ** 2 - 128:
                get_adjacent_square(i + 128)

        for i in range(128 ** 2):
            if i in seen or i not in squares:
                continue
            regions += 1
            get_adjacent_square(i)
        return regions

    def solve(self, puzzle_input):
        grid = self._get_grid(puzzle_input)
        return sum(map(int, grid))

    def solve_again(self, puzzle_input):
        grid = self._get_grid(puzzle_input)
        squares = [i for i, s in enumerate(list(grid)) if s == '1']
        return self._find_regions(squares)


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
