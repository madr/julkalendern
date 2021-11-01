from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '10.txt'
    list = []
    l = 0
    skip_size = 0
    pos = 0

    def __str__(self):
        return 'Day 10: Knot Hash'

    def reset(self, l=256):
        self.list = list(range(l))
        self.l = l
        self.skip_size = 0
        self.pos = 0

    def reverse(self, sublist_length):
        sublist = []
        for i in range(sublist_length):
            sublist.append(self.list[(self.pos + i) % self.l])
        for i, n in enumerate(reversed(sublist)):
            self.list[(self.pos + i) % self.l] = n
        self.pos = (self.pos + sublist_length + self.skip_size) % self.l
        self.skip_size += 1

    def solve(self, puzzle_input, r=256):
        self.reset(r)
        for sublist_length in map(int, puzzle_input.split(',')):
            self.reverse(sublist_length)
        return self.list[0] * self.list[1]

    def solve_again(self, puzzle_input, r=256):
        puzzle_input = [ord(c) for c in puzzle_input] + [17, 31, 73, 47, 23]
        self.reset(r)
        for _ in range(64):
            for sublist_length in puzzle_input:
                self.reverse(sublist_length)
        dense_hash = [eval('^'.join(list(map(str, self.list[seq:seq+16])))) for seq in range(0, r, 16)]
        return ''.join(['{:x}'.format(int(i)).zfill(2) for i in dense_hash])


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
