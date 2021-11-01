from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '04.txt'

    def __str__(self):
        return 'Day 4: High-Entropy Passphrases'

    def validate(self, passphrase, extended=False):
        words = passphrase.split()
        if extended:
            words = [''.join(sorted(w)) for w in words]
        return sorted(list(set(words))) == sorted(words)

    def solve(self, puzzle_input):
        return sum(self.validate(p) for p in puzzle_input.splitlines())

    def solve_again(self, puzzle_input):
        return sum(self.validate(p, True) for p in puzzle_input.splitlines())


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
