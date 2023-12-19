from hashlib import md5

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "04.txt"

    def __str__(self):
        return "Day 4: The Ideal Stocking Stuffer"

    def solve(self, pi):
        return self._solve(pi)[0]

    def solve_again(self, pi):
        return self._solve(pi)[1]

    def _solve(self, secret):
        p12 = []
        prefetched = [254575, 1038736]
        for zc in [5, 6]:
            sw = str.zfill("0", zc)
            c = prefetched.pop(0)
            if md5(bytes(f"{secret}{c}", "utf-8")).hexdigest().startswith(sw):
                p12.append(c)
        return p12

    def parse_input(self, data):
        return data.strip()


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
