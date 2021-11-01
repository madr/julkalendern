from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '05.txt'

    def __str__(self):
        return 'Day 5: A Maze of Twisty Trampolines, All Alike'

    def solve(self, puzzle_input, strange_jumps=False):
        pos = 0
        steps = 0
        offset_values = [int(ov) for ov in puzzle_input.splitlines()]
        r = range(len(offset_values))
        while pos in r:
            jump_by = offset_values[pos]
            offset_values[pos] += -1 if strange_jumps and jump_by > 2 else 1
            pos += jump_by
            steps += 1
        return steps

    def solve_again(self, puzzle_input):
        return self.solve(puzzle_input, True)


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
