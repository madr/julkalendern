import itertools

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '01.in'

    def __str__(self):
        return 'Day 1: Chronal Calibration'

    def solve(self, puzzle_input, freq=0):
        return sum(map(int, puzzle_input.splitlines()))

    def solve_again(self, puzzle_input, freq=0):
        freq_changes = map(int, puzzle_input.splitlines())
        known = {0}
        for n in itertools.cycle(freq_changes):
            freq += n
            if freq in known:
                break
            known.add(freq)
        return freq


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
