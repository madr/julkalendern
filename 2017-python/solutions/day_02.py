from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '02.txt'

    def __str__(self):
        return 'Day 2: Corruption Checksum'

    def _get_rows(self, puzzle_input):
        return [list(map(int, rows.split())) for rows in puzzle_input.splitlines()]

    def get_even_divisible(self, columns):
        l = len(columns)
        for col in range(l):
            for i in range(l):
                if not col == i and columns[col] % columns[i] == 0:
                    return columns[col] // columns[i]

    def get_diff(self, columns):
        return max(columns) - min(columns)

    def solve(self, puzzle_input):
        rows = self._get_rows(puzzle_input)
        return sum(self.get_diff(columns) for columns in rows)

    def solve_again(self, puzzle_input):
        rows = self._get_rows(puzzle_input)
        return sum(self.get_even_divisible(columns) for columns in rows)


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
