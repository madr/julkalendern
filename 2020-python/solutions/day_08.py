from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "08.txt"

    def __str__(self):
        return "Day 8: Handheld Halting"

    def parse_input(self, data):
        def parse(l):
            op, change = l.split()
            return (op, int(change))

        return [parse(line) for line in data.splitlines()]

    def solve(self, puzzle_input):
        _, acc = self.run(puzzle_input)
        return acc

    def solve_again(self, puzzle_input):
        stop_at = len(puzzle_input)
        tried = 0
        i = 0
        offset = 0
        while tried <= stop_at and i < stop_at:
            instructions, offset = self.alter(puzzle_input, offset)
            exit_code, acc = self.run(instructions)
            if exit_code == "ok":
                return acc
            i += 1

    def run(self, instructions):
        seen = set()
        caretpos = 0
        acc = 0
        stop_at = len(instructions)
        while len(seen) < stop_at:
            if caretpos == stop_at:
                return "ok", acc
            if caretpos % stop_at in seen:
                return "exit", acc
            seen.add(caretpos)
            acc, caretpos = self.execute(instructions, caretpos % stop_at, acc)

    def execute(self, instructions, caretpos, acc):
        op, change = instructions[caretpos]
        if op == "nop":
            return acc, caretpos + 1
        if op == "jmp":
            return acc, caretpos + change
        if op == "acc":
            return acc + change, caretpos + 1

    def alter(self, instructions, offset):
        il = len(instructions)
        invalid_changes = [0, il, -il]
        dont = "DO_NOT_ALTER"

        def sanitize(instruction):
            op, change = instruction
            if op == "nop" and change in invalid_changes:
                return (dont, change)
            return (op, change)

        change_range = [op for op, _change in map(sanitize, instructions[offset:])]
        try:
            first_jmp = change_range.index("jmp")
        except ValueError:
            first_jmp = il - offset - 1
        try:
            first_nop = change_range.index("nop")
        except ValueError:
            first_nop = il - offset - 1
        change_at = offset + min(first_nop, first_jmp)
        altered = [*instructions]
        old_op, change = altered[change_at]
        new_op = "jmp" if old_op == "nop" else "nop"
        altered[change_at] = (new_op, change)
        return altered, change_at + 1


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
