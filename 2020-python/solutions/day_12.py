from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "12.txt"
    directions = ("E", "S", "W", "N")

    def __str__(self):
        return "Day 12: Rain Risk"

    def parse_input(self, data):
        return [(l[0], int(l[1:])) for l in data.split()]

    def solve(self, puzzle_input):
        pos = (0, 0)
        d = "E"

        for op, change in puzzle_input:
            if op in "RL":
                d = self.rotate(d, op, change)
            elif op in "ESWN":
                pos = self.move(pos, op, change)
            elif op in "F":
                pos = self.move(pos, d, change)

        return sum(pos)

    def solve_again(self, puzzle_input):
        ship = (0, 0)
        waypoint = (10, -1)
        d = "E"

        for op, change in puzzle_input:
            if op in "RL":
                d, waypoint = self.reposition(d, waypoint, op, change)
            elif op in "ESWN":
                waypoint = self.move(waypoint, op, change)
            elif op in "F":
                ship = self.move(ship, d, change, waypoint)

        return sum(ship)

    def move(self, pos, op, change, factors=None):
        x, y = pos
        if factors:
            fx, fy = factors
            return (x + change * fx, y + change * fy)
        if op == "W":
            return (x - change, y)
        if op == "E":
            return (x + change, y)
        if op == "N":
            return (x, y - change)
        if op == "S":
            return (x, y + change)

    def rotate(self, d, op, change):
        change = change // 90
        i = self.directions.index(d)
        if op == "L":
            return self.directions[abs((i - change) % 4)]
        else:
            return self.directions[abs((i + change) % 4)]

    def reposition(self, d, pos, op, change):
        steps = change // 90
        x, y = pos
        d = self.rotate(d, op, change)
        for _ in range(steps):
            if op == "R":
                x, y = -y, x
            if op == "L":
                x, y = y, -x
        return d, (x, y)


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
