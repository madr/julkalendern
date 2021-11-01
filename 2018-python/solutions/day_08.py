import sys

from solutions import BaseSolution


sys.setrecursionlimit(15000)  # hej python!

class Solution(BaseSolution):
    input_file = '08.in'

    def __str__(self):
        return 'Day 8: Memory Maneuver'

    def solve(self, puzzle_input):
        data = list(map(int, (puzzle_input.split())))
        _, s = self._get_sum(0, 0, data)
        return s

    def solve_again(self, puzzle_input):
        data = list(map(int, (puzzle_input.split())))
        _, value = self._get_value(0, data)
        return value

    def _get_sum(self, i, s, data):
        children = data[i]
        meta_entries = data[i + 1]
        i += 2
        for _ in range(children):
            i, s = self._get_sum(i, s, data)
        s += sum([data[i + n] for n in range(meta_entries)])
        return i + meta_entries, s

    def _get_value(self, i, data):
        children = data[i]
        meta_entries = data[i + 1]
        i += 2
        child_values = {}
        for n in range(children):
            i, value = self._get_value(i, data)
            child_values[n] = value
        meta_values = [data[i + n] for n in range(meta_entries)]
        if children:
            v = sum(child_values.get(n - 1, 0) for n in meta_values)
        else:
            v = sum(meta_values)
        return i + meta_entries, v


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
