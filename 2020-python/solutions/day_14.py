import re

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "14.txt"

    def __str__(self):
        return "Day 14: Docking Data"

    def parse_input(self, data):
        programs = []
        for p in data.split("mask = "):
            if p.strip() == "":
                continue
            mask = p.split()[0]
            instructions = [
                (int(a), int(v)) for a, v in re.findall(r"mem\[(\d+)\] = (\d+)", p)
            ]
            programs.append((mask, instructions))
        return programs

    def solve(self, programs):
        memory = {}
        zf = len(programs[0][0])
        for mask, instructions in programs:
            for loc, value in instructions:
                value = bin(value)[2:].zfill(zf)
                for i, n in enumerate(mask):
                    if n == "X":
                        continue
                    value = f"{value[:i]}{n}{value[i+1:]}"
                memory[loc] = int(value, 2)
        return sum(v for k, v in memory.items())

    def solve_again(self, programs):
        memory = {}
        zf = len(programs[0][0])
        for mask, instructions in programs:
            for loc, value in instructions:
                loc = bin(loc)[2:].zfill(zf)
                for i, n in enumerate(mask):
                    if n == "1":
                        loc = f"{loc[:i]}{n}{loc[i+1:]}"
                locs = [loc]
                for i, n in enumerate(mask):
                    if n == "X":
                        a = locs[:]
                        b = locs[:]
                        locs = [*map(lambda x: f"{x[:i]}0{x[i+1:]}", a)] + [
                            *map(lambda x: f"{x[:i]}1{x[i+1:]}", b)
                        ]
                for loc in locs:
                    memory[int(loc, 2)] = value
        return sum(v for k, v in memory.items())


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
