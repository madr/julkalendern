from collections import defaultdict, deque
from itertools import permutations

from output import matrix


def solve(data):
    grid, H, W = matrix(data)
    antennas = defaultdict(list)
    for row, col in [
        (row, col)
        for row, row_values in enumerate(grid)
        for col, _vc in enumerate(row_values)
    ]:
        if (id := grid[row][col]) != ".":
            antennas[id].append((row, col))
    adjacent_locs = set()
    all_antinodes = set()
    for k, v in antennas.items():
        for a, b in permutations(v, r=2):
            all_antinodes.add(a)
            a1, a2 = a
            b1, b2 = b
            delta_y, delta_x = a1 - b1, a2 - b2
            y, x = a1 + delta_y, a2 + delta_x
            if 0 <= y < H and 0 <= x < W:
                adjacent_locs.add((y, x))
                queue = deque([(y, x, delta_y, delta_x)])
                while queue:
                    y, x, delta_y, delta_x = queue.popleft()
                    if 0 <= y < H and 0 <= x < W:
                        all_antinodes.add((y, x))
                        queue.append((y + delta_y, x + delta_x, delta_y, delta_x))
    return len(adjacent_locs), len(all_antinodes)


if __name__ == "__main__":
    with open("./input/08.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
