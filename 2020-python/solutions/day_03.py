from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "03.txt"

    def __str__(self):
        return "Day 3: Toboggan Trajectory"

    def parse_input(self, data):
        return [line.strip() for line in data.strip().splitlines()]

    def solve(self, puzzle_input):
        return self.count_trees(3, 1, puzzle_input)

    def solve_again(self, puzzle_input):
        slopes = [(1, 1), (5, 1), (7, 1), (1, 2)]
        tree_encounters = self.solve(puzzle_input)  # slope 3, 1
        for x, y in slopes:
            tree_encounters *= self.count_trees(x, y, puzzle_input)
        return tree_encounters

    def count_trees(self, xdir, ydir, mapdata):
        patternlen = len(mapdata[0])
        tree_encounters = 0
        ystops = [y for y in range(len(mapdata)) if y % ydir == 0]
        for i, y in enumerate(ystops):
            x = i * xdir % patternlen
            if mapdata[y][x] == "#":
                tree_encounters += 1
        return tree_encounters


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
