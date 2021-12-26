from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "08.txt"

    def __str__(self):
        return "Day 8: Seven Segment Search"

    def parse_input(self, data):
        def parse(l):
            i, o = l.split(" | ")
            return i.split(), o.split()

        return [parse(l) for l in data.strip().splitlines()]

    def solve(self, puzzle_input):
        return sum(sum(len(d) in (2, 3, 4, 7) for d in l[1]) for l in puzzle_input)

    def solve_again(self, puzzle_input):
        digits = [
            "abcefg",
            "cf",
            "acdeg",
            "acdfg",
            "bcdf",
            "abdfg",
            "abdefg",
            "acf",
            "abcdefg",
            "abcdfg",
        ]
        outs = []

        def outsum(n):
            out = ["".join(sorted(n[s] for s in d)) for d in digits]
            outs.append(
                int(
                    "".join(
                        map(
                            str,
                            [out.index(i) for i in ["".join(sorted(oo)) for oo in o]],
                        )
                    )
                )
            )

        for i, o in puzzle_input:
            n = {}
            v1, v7, v4, v8 = sorted(
                list(filter(lambda o: len(o) in (2, 3, 4, 7), i)), key=lambda x: len(x)
            )
            c, f = v1
            n["a"] = a = (set(v7) - set(v1)).pop()
            v235 = list(filter(lambda d: len(d) == 5, i))
            for v in v235:
                diff = set(v) - set(v4 + a)
                if len(diff) == 1:
                    n["g"] = g = diff.pop()
                    break
            n["c"] = c
            n["f"] = f
            n["e"] = e = (set(v8) - set(v4 + a + g)).pop()
            for v in v235:
                diff = set(v) - set(n.values())
                if len(diff) == 1:
                    n["d"] = d = diff.pop()
                    break
            n["b"] = b = (set(v4) - set([d, c, f])).pop()

            try:
                outsum(n)
            except ValueError:
                n["c"] = f
                n["f"] = c
                outsum(n)

        return sum(outs)


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()

"""
 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc


  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

"""
