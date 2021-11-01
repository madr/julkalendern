import re

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "18.txt"

    pattern = r"\(([^\(\)]+)\)"

    def __str__(self):
        return "Day 18: Operation Order"

    def parse_input(self, data):
        return [r.strip() for r in data.strip().splitlines()]

    def chunks(self, seq):
        for i in range(0, len(seq), 2):
            yield seq[i : i + 2]

    def math(self, exp, advanced=False):
        has_nests = True
        while has_nests:
            nests = re.findall(self.pattern, exp)
            if not nests:
                has_nests = False
            for nest in nests:
                exp = exp.replace(f"({nest})", str(self.math(nest, advanced)))
        if advanced:
            has_additions = True
            while has_additions:
                additions = re.findall(r"(\d+) \+ (\d+)", exp)
                if not additions:
                    has_additions = False
                else:
                    a, b = additions[0]
                    exp = exp.replace(f"{a} + {b}", str(int(a) + int(b)), 1)
        seq = exp.split()
        result = int(seq[0])
        if len(seq) == 1:
            return result
        instructions = list(self.chunks(seq[1:]))
        for op, value in instructions:
            if op == "*":
                result *= int(value)
            if op == "+":
                result += int(value)
        return result

    def basic_math(self, exp):
        return self.math(exp, advanced=False)

    def advanced_math(self, exp):
        return self.math(exp, advanced=True)

    def solve(self, puzzle_input):
        return sum(self.basic_math(mathex) for mathex in puzzle_input)

    def solve_again(self, puzzle_input):
        return sum(self.advanced_math(mathex) for mathex in puzzle_input)


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
