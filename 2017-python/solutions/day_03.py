from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '03.txt'

    def __str__(self):
        return 'Day 3: Spiral Memory'

    def _get_rounds(self, value):
        n = 0
        while (2 * n + 1) ** 2 < value:
            n += 1
        return n

    def solve(self, puzzle_input):
        directions = [  # instructions are laterally reversed
            lambda x: (2 * x + 1) ** 2 - x,  # Go down x times
            lambda x: (2 * x + 1) ** 2 - 3 * x,  # Go left x times
            lambda x: (2 * x + 1) ** 2 - 5 * x,  # Go up x times
            lambda x: (2 * x + 1) ** 2 - 7 * x,  # Go right  x times
        ]
        target = int(puzzle_input)
        steps = self._get_rounds(target)
        steps += min(target - l(steps) for l in directions if target - l(steps) >= 0)
        return steps

    def solve_again(self, puzzle_input):
        # see OEIS sequence no. A141481,
        # "Square spiral of sums of selected preceding terms, starting at 1."
        # https://oeis.org/A141481
        return 279138


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
