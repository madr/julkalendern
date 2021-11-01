from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '08.txt'
    registry = {}

    def __str__(self):
        return 'Day 8: I Heard You Like Registers'

    def _should_modify(self, x, comp, y):
        if comp in ('==', '!=', '>=', '<=', '>', '<'):
            return eval('{:d} {} {:d}'.format(x, comp, y))
        return False

    def _update_registry(self, registry, instruction):
        r, action, n, _, k, comp, v = instruction.split()
        current = registry.get(r, 0)
        if self._should_modify(registry.get(k, 0), comp, int(v)):
            registry[r] = current + int(n) if action == 'inc' else current - int(n)

    def solve(self, puzzle_input):
        registry = {}
        for instruction in puzzle_input.splitlines():
            self._update_registry(registry, instruction)
        return max(registry.values())

    def solve_again(self, puzzle_input):
        registry = {}
        max_value = 0
        for instruction in puzzle_input.splitlines():
            self._update_registry(registry, instruction)
            if len(registry) > 0:
                max_value = max([max_value, max(registry.values())])
        return max_value


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
