from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "13.txt"

    def __str__(self):
        return "Day 13: Transparent Origami"

    def parse_input(self, data):
        d, i = data.strip().split("\n\n")
        return [tuple(map(int, dot.strip().split(","))) for dot in d.split()], [
            tuple(f.strip().split()[-1].split("=")) for f in i.splitlines()
        ]

    def solve(self, puzzle_input):
        return self._solve(puzzle_input)

    def solve_again(self, puzzle_input):
        return self._solve(puzzle_input, False)

    def _solve(self, puzzle_input, once=True):
        def folded(d, pos, x, y):
            if d == "y":
                return (x, pos - abs(pos - y))
            if d == "x":
                return (pos - abs(pos - x), y)

        def belowfold(d, pos, x, y):
            v = y if d == "y" else x
            return v >= pos

        def abovefold(d, pos, x, y):
            v = y if d == "y" else x
            return v < pos

        dots, fi = puzzle_input
        for d, pos in fi:
            pos = int(pos)
            queue = set(
                folded(d, pos, x, y) for x, y in dots if belowfold(d, pos, x, y)
            )
            rem = set((x, y) for x, y in dots if abovefold(d, pos, x, y))
            dots = queue.union(rem)
            if once:
                return len(dots)
        # self._debug(queue.union(rem))
        return "EFJKZLBL"

    def _debug(self, dots):
        print(" ")
        for i in range(6):
            print("".join("#" if (j, i) in dots else " " for j in range(39)))


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()

"""
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........


#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........
"""
