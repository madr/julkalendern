from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "02.txt"

    def __str__(self):
        return "Day 2: Drive!"

    def parse_input(self, data):
        def xy(direction, value):
            if direction == "forward":
                return (0, int(value))
            elif direction == "up":
                return (-int(value), 0)
            elif direction == "down":
                return (int(value), 0)

        return [xy(*l.split()) for l in data.strip().splitlines()]

    def solve(self, puzzle_input):
        x = sum(map(lambda xy: xy[0], puzzle_input))
        y = sum(map(lambda xy: xy[1], puzzle_input))
        return x * y

    def solve_again(self, puzzle_input):
        pos = (0, 0, 0)
        for x, y in puzzle_input:
            if y > 0:
                pos = (pos[2] * y + pos[0], pos[1] + y, pos[2])
            else:
                pos = (pos[0], pos[1], pos[2] + x)
        return pos[0] * pos[1]


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
