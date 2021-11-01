import itertools

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '11.in'

    def __str__(self):
        return 'Day 11: Chronal Charge'

    def solve(self, puzzle_input):
        serial = int(puzzle_input)
        matrix = self._populate_matrix(serial)
        x, y, _plsum = self._get_size(matrix, 3)
        return x, y

    def solve_again(self, puzzle_input):
        serial = int(puzzle_input)
        matrix = self._populate_matrix(serial)
        results = set()
        for i in range(300):
            x, y, plsum = self._get_size(matrix, i)
            results.add((x, y, plsum, i))
        x, y, _plsum, i = sorted(results, key=lambda s: s[2], reverse=True)[0]
        return x, y, i

    def get_power_level(self, x, y, serial):
        rid = x + 10
        pl = rid * y
        pl += serial
        pl *= rid
        pl = (pl // 100) % 10
        pl -= 5
        return pl

    def _get_size(self, matrix, square_size=3):
        squares = set()
        for top, left in itertools.product(range(300-square_size), range(300-square_size)):
            plsum = sum(matrix[(x + left, y + top)]
                        for y, x in itertools.product(range(square_size), range(square_size)))
            squares.add((left, top, plsum))
        return sorted(squares, key=lambda s: s[2], reverse=True)[0]

    def _populate_matrix(self, serial):
        matrix = dict()
        for top, left in itertools.product(range(300), range(300)):
            matrix[(left, top)] = self.get_power_level(left, top, serial)
        return matrix


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
