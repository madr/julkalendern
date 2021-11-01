from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '17.txt'

    def __str__(self):
        return 'Day 17: Spinlock'

    def solve(self, puzzle_input):
        n = int(puzzle_input)
        l = [0]
        pos = 0
        for i in range(1, 2018):
            pos = (pos + n) % i + 1
            l.insert(pos, i)
        return l[pos + 1 % 2017]

    def solve_again(self, puzzle_input):
        pos = 0
        n = int(puzzle_input)
        last_seen = 0
        for i in range(1, 5 * 10 ** 7 + 1):
            pos = (pos + n) % i + 1
            if pos == 1:
                last_seen = i
        return last_seen


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
