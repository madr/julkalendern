from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '16.txt'

    def __str__(self):
        return 'Day 16: Permutation Promenade'

    def _move(self, programs, m, i):
        l = len(programs)
        if m == 's':
            r = int(i)
            return programs[-r:] + programs[:l - r]
        if m == 'x':
            x, y = [int(s) for s in i.split('/')]
            z = programs[x]
            programs[x] = programs[y]
            programs[y] = z
            return programs
        if m == 'p':
            xp, yp = i.split('/')
            x = programs.index(xp)
            y = programs.index(yp)
            z = programs[x]
            programs[x] = programs[y]
            programs[y] = z
            return programs

    def _dance(self, programs, moves):
        for m in moves:
            programs = self._move(programs, m[0], m[1:])
        return programs

    def solve(self, puzzle_input, n=16):
        programs = [chr(c) for c in range(97, 97 + n)]
        moves = puzzle_input.split(',')
        return ''.join(self._dance(programs, moves))

    def solve_again(self, puzzle_input, n=16):
        moves = puzzle_input.split(',')
        initial = [chr(c) for c in range(97, 97 + n)]
        programs = list(self.solve(puzzle_input))
        dances = 1
        while not programs == initial:
            programs = self._dance(programs, moves)
            dances += 1
        for _ in range(10 ** 9 % dances):
            programs = self._dance(programs, moves)
        return ''.join(programs)


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
