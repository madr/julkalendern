from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '06.txt'

    def __str__(self):
        return 'Day 6: Memory Reallocation'

    def redistribute(self, banks):
        banks = list(banks)
        hi = banks.index(max(banks))
        l = len(banks)
        v = banks[hi] - banks[hi] % (l - 1)
        if v == 0:
            v = banks[hi]
        banks[hi] -= v
        pos = (hi + 1) % l
        while v > 0:
            if pos != hi:
                banks[pos] += 1
                v -= 1
            pos = (pos + 1) % l
        return tuple(banks)

    def _allocate(self, puzzle_input):
        banks = list(map(int, puzzle_input.split()))
        seen = [tuple(banks)]
        not_seen = True
        while not_seen:
            banks = self.redistribute(banks)
            if banks in seen:
                not_seen = False
            seen.append(banks)
        return seen

    def solve(self, puzzle_input):
        return len(self._allocate(puzzle_input)) - 1

    def solve_again(self, puzzle_input):
        seen = self._allocate(puzzle_input)
        seen_last = ' '.join(str(n) for n in seen[-1])
        return len(self._allocate(seen_last)) - 1


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
