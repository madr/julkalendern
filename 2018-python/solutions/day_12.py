from collections import defaultdict

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '12.in'

    def __str__(self):
        return 'Day 12: Subterranean Sustainability'

    def solve(self, puzzle_input):
        initital_pots, rules = self._prepare(puzzle_input)
        pots, _ = self._grow(initital_pots, rules, 20)
        return sum(k for k, v in pots.items() if v == '#')

    def solve_again(self, puzzle_input):
        # No tests cover for this, so here goes an explanation.
        #
        # To get the sum of the filty billion'th generation, we look
        # for the first recurring pot pattern. self._grow() will
        # automatically break the loop if the recurring pattern (of pots)
        # is found.
        #
        # Adding The Big Fucking Number, the correct sum is calculated.
        initital_pots, rules = self._prepare(puzzle_input)
        pots, repeated_at = self._grow(initital_pots, rules, 999)
        BFN = 50 * 10 ** 9  # Big Fucking Number
        return sum(k + (BFN - repeated_at) for k, v in pots.items() if v == '#')

    def _grow(self, pots, rules, generations):
        seen = dict()
        repeated_at = 0
        for g in range(1, generations + 1):
            start_at = min(pots) - 5
            stop_at = max(pots) + 5
            span = range(start_at, stop_at)
            updated = dict()
            for i in span:
                for rule in [''.join(pots[i + j] for j in range(-2, 3))]:
                    updated[i] = rules.get(rule, '.')
            pots.clear()
            pots.update(updated)
            pattern = ''.join(pots[i] for i in span).strip('.')
            if pattern in seen:
                repeated_at = g
                break
            seen[pattern] = g
        return pots, repeated_at

    def _prepare(self, puzzle_input):
        initial, _, *rules_data = puzzle_input.splitlines()
        pots = defaultdict(lambda: '.')
        pots.update({
            i: v for i, v in enumerate(initial[len('initial state: '):])
        })
        rules = dict()
        for r in rules_data:
            k, v = r.split(' => ')
            rules[k] = v
        return pots, rules


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
