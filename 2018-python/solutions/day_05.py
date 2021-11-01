from functools import reduce

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '05.in'

    def __str__(self):
        return 'Day 5: Alchemical Reduction'

    def solve(self, puzzle_input):
        return self._react_polymer(puzzle_input)

    def solve_again(self, puzzle_input):
        sorted_data = sorted(puzzle_input)
        polymer_reactions = set()
        for char in range(ord(sorted_data[0]), ord(sorted_data[-1])):
            polymer_reactions.add(self._react_polymer(puzzle_input.replace(chr(char), '').replace(chr(char + 32), '')))
        return min(polymer_reactions)

    def _react_polymer(self, data):
        def remove_pairs(done, candidate):
            if not done:
                return candidate
            last = done[-1]
            if abs(ord(last) - ord(candidate)) == 32:
                return done[:-1]
            return ''.join([done, candidate])
        return len(reduce(remove_pairs, data))


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
