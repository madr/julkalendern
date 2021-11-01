from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '01.txt'

    def __str__(self):
        return 'Day 1: Inverse Captcha'

    def solve(self, puzzle_input, distance=1):
        pi_length = len(puzzle_input)
        return sum(int(puzzle_input[pos]) for pos in range(pi_length) if
                   puzzle_input[pos] == puzzle_input[(pos + distance) % pi_length])

    def solve_again(self, puzzle_input):
        distance = len(puzzle_input) // 2
        return self.solve(puzzle_input, distance)


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
