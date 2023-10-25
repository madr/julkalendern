import re
from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "11.txt"

    def __str__(self):
        return "Day 11: Corporate Policy"

    def is_valid(self, suggestion):
        if "i" in suggestion or "l" in suggestion or "o" in suggestion:
            return False
        if (
            len(
                set(
                    map(
                        lambda x: x[0],
                        filter(lambda x: x[0] == x[1], zip(suggestion, suggestion[1:])),
                    )
                )
            )
            < 2
        ):
            return False

        def seq(abc):
            a, b, c = abc
            return ord(b) - ord(a) == 1 and ord(c) - ord(b) == 1

        return any(map(seq, zip(suggestion, suggestion[1:], suggestion[2:])))

    def parse_input(self, data):
        return data

    def solve(self, password):
        def tick(p):
            chars = list(p)[::-1]
            i = 0
            for c in chars:
                if c == "z":
                    chars[i] = "a"
                else:
                    chars[i] = chr(ord(chars[i]) + 1)
                    break
                i += 1
            return "".join(chars[::-1])

        unallowed = re.compile(r"i|l|o")
        fastforward = re.search(unallowed, password)
        if fastforward:
            password = (
                password[: fastforward.start()]
                + chr(ord(password[fastforward.start()]) + 1)
            ).ljust(len(password), "a")

        while True:
            password = tick(password)
            if self.is_valid(password):
                return password

    def solve_again(self, puzzle_input):
        return self.solve(self.solve(puzzle_input))


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
