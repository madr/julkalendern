from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '12.txt'
    seen = []

    def __str__(self):
        return 'Day 12: Digital Plumber'

    def _walk(self, i, programs):
        line = next(filter(lambda l: l.startswith('{} <->'.format(i)), programs))
        piped = line.split()[2:]
        self.seen.add(i)
        for p in [int(p.replace(',', '')) for p in piped]:
            if p not in self.seen:
                self._walk(p, programs)

    def solve(self, puzzle_input):
        programs = [pi.strip() for pi in puzzle_input.splitlines()]
        self.seen = set()
        self._walk(0, programs)
        return len(self.seen)

    def solve_again(self, puzzle_input):
        programs = [pi.strip() for pi in puzzle_input.splitlines()]
        self.seen = set()
        groups = 0
        for line in programs:
            pid = int(line.split()[0])
            if pid not in self.seen:
                self._walk(pid, programs)
                groups += 1
        return groups


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
