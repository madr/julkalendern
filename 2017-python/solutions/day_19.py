from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '19.txt'
    trim_input = False

    def __str__(self):
        return 'Day 19: A Series of Tubes'

    def _walk_maze(self, puzzle_input):
        DIRECTIONS = {
            'D': (1, 0),
            'U': (-1, 0),
            'R': (0, 1),
            'L': (0, -1),
        }
        maze = puzzle_input.splitlines()
        pos = (0, list(maze[0]).index('|'))
        d = DIRECTIONS['D']
        paths = '-|'
        steps = 0
        seen = ''

        def _nc(nu):
            np = (pos[0] + nu[0], pos[1] + nu[1])
            if np[0] < len(maze) and np[1] < len(maze[np[0]]):
                return maze[np[0]][np[1]]
            else:
                return ' '

        while True:
            pos = (pos[0] + d[0], pos[1] + d[1])
            c = _nc((0, 0))
            steps += 1
            if c == '+':
                nc = _nc(d)
                if nc == ' ':
                    for v in DIRECTIONS.values():
                        if -v[0] == d[0] and -v[1] == d[1]:
                            continue
                        nc = _nc(v)
                        if nc != ' ':
                            d = v
                            break
            elif c == ' ':
                break
            elif c not in paths:
                seen += c
        return seen, steps

    def solve(self, puzzle_input):
        seen, _ = self._walk_maze(puzzle_input)
        return seen

    def solve_again(self, puzzle_input):
        _, steps = self._walk_maze(puzzle_input)
        return steps


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
