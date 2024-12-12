from output import cw, matrix


def solve(data):
    M, H, W = matrix(data)
    y, x = [(r, c) for r in range(H) for c in range(W) if M[r][c] == "^"][0]
    delta_y, delta_x = (-1, 0)
    seen, _ = travel(M, H, W, y, x, delta_y, delta_x)
    num_visited = len(seen)
    num_obstruction_coords = 0
    for row, col in seen:
        grid = [list(row) for row in M]
        grid[row][col] = "#"
        _, loop_found = travel(grid, H, W, y, x, delta_y, delta_x)
        if loop_found:
            num_obstruction_coords += 1
    return num_visited, num_obstruction_coords


def travel(M, H, W, y, x, delta_y, delta_x):
    seen = set()
    hit = set()
    loop_found = False
    while True:
        seen.add((y, x))
        if y == 0 or y == H - 1 or x == 0 or x == W - 1:
            break
        if M[y + delta_y][x + delta_x] == "#":
            if (y + delta_y, x + delta_x, delta_y, delta_x) in hit:
                loop_found = True
                break
            hit.add((y + delta_y, x + delta_x, delta_y, delta_x))
            delta_y, delta_x = cw(delta_y, delta_x)
        else:
            y, x = y + delta_y, x + delta_x
    return seen, loop_found


if __name__ == "__main__":
    with open("./input/06.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
