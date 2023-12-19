import re
from random import shuffle

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "19.txt"

    def __str__(self):
        return "Day 19: Medicine for Rudolph"

    def solve(self, pi):
        ml, s = pi.split("\n\n")
        o = set()
        for l in ml.splitlines():
            k, v = l.split(" => ")
            for mo in re.finditer(k, s):
                a, b = mo.span()
                o.add(s[:a] + v + s[b:])
        return len(o)

    def solve_again(self, pi):
        m = {}
        ml, e = pi.split("\n\n")
        for l in ml.splitlines():
            k, v = l.split(" => ")
            m[v] = k
        p2 = 0
        while p2 == 0:
            s = e
            c = 0
            os = ""
            keys = list(m.keys())
            shuffle(keys)
            while os != s:
                os = s
                for k in keys:
                    while k in s:
                        c += s.count(k)
                        s = s.replace(k, m[k])
            p2 = int(s == "e") * c
        return p2

    def parse_input(self, data):
        return data.strip()


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
