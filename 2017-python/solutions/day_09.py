import re

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '09.txt'

    def __str__(self):
        return 'Day 9: Stream Processing'

    def solve(self, puzzle_input):
        level = 0
        groups = []
        stream = re.sub(r'!.', '', puzzle_input)
        stream = re.sub(r'<[^>]*>', '', stream)
        for c in stream:
            if c == '{':
                level += 1
            if c == '}':
                groups.append(level)
                level -= 1
        return sum(groups)

    def solve_again(self, puzzle_input):
        stream = re.sub(r'!.', '', puzzle_input)
        garbage = re.findall(r'<([^>]*)>', stream)
        return sum([len(g) for g in garbage])


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
