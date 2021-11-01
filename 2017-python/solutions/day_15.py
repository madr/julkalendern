from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '15.txt'

    def __str__(self):
        return 'Day 15: Dueling Generators'

    def _calc(self, x, f, m=1):
        x = (x * f) % 2147483647
        if x % m != 0:
            return self._calc(x, f, m)
        else:
            return x

    def solve(self, puzzle_input):
        af, bf = (16807, 48271)
        a, b = [int(pi.split()[-1]) for pi in puzzle_input.splitlines()]
        j = 0
        for _ in range(40 * 10**6):
            a = self._calc(a, af)
            b = self._calc(b, bf)
            if '{:b}'.format(a)[-16:] == '{:b}'.format(b)[-16:]:
                j += 1
        return j

    def solve_again(self, puzzle_input):
        af, bf = (16807, 48271)
        a, b = [int(pi.split()[-1]) for pi in puzzle_input.splitlines()]
        j = 0
        for _ in range(5 * 10 ** 6):
            a = self._calc(a, af, 4)
            b = self._calc(b, bf, 8)
            if '{:b}'.format(a)[-16:] == '{:b}'.format(b)[-16:]:
                j += 1
        return j


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
