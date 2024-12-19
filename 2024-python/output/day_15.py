from output import D, matrix


def solve(data):
    O = {k: v for k, v in zip("^>v<", D)}
    grid, movements = data.split("\n\n")
    grid, H, W = matrix(grid)
    movements = "".join(movements.split())

    grid_1 = {
        (r, c): value for r, row in enumerate(grid) for c, value in enumerate(row)
    }

    grid_2 = {}
    for pos, value in grid_1.items():
        r2, c2 = pos
        match value:
            case "O":
                grid_2[(r2, c2 * 2)] = "["
                grid_2[(r2, c2 * 2 + 1)] = "]"
            case "@":
                grid_2[(r2, c2 * 2)] = "@"
                grid_2[(r2, c2 * 2 + 1)] = "."
            case _:
                grid_2[(r2, c2 * 2)] = value
                grid_2[(r2, c2 * 2 + 1)] = value

    answers = []

    for grid, W in [(grid_1, W), (grid_2, W * 2)]:
        pos = next((r, c) for r in range(H) for c in range(W) if grid[(r, c)] == "@")

        for move in movements:
            r, c = pos
            dr, dc = O[move]
            move_boxes = True
            blocked = False

            if (r + dr, c + dc) not in grid:
                continue

            match grid[(r + dr, c + dc)]:
                case ".":
                    move_boxes = False
                case "#":
                    move_boxes = False
                    continue

            if move_boxes:
                seen = set()

                Q = [(r + dr, c + dc)]

                while Q:
                    rr, cc = Q.pop(0)

                    if (rr, cc) in seen:
                        continue

                    if (rr, cc) not in grid:
                        continue

                    if grid[(rr, cc)] == "#":
                        blocked = True
                        continue

                    seen.add((rr, cc))

                    if grid[(rr, cc)] in ".":
                        continue

                    Q.append((rr + dr, cc + dc))
                    if dr != 0:
                        match grid[(rr, cc)]:
                            case "]":
                                Q.append((rr, cc - 1))
                            case "[":
                                Q.append((rr, cc + 1))

                if blocked:
                    continue

                patchset = {
                    (rr, cc): (rr + dr, cc + dc)
                    for rr, cc in seen
                    if grid[(rr, cc)] != "."
                }

                dotset = set(seen) - set(patchset.values())

                for oldpos, newpos in sorted(patchset.items())[:: -(dr + dc)]:
                    value = grid[oldpos]
                    grid[newpos] = value

                for dot in dotset:
                    grid[dot] = "."

            grid[(r, c)] = "."
            grid[(r + dr, c + dc)] = "@"
            pos = r + dr, c + dc

        answers.append(sum(k[0] * 100 + k[1] for k, v in grid.items() if v in "O["))

    p1, p2 = answers
    return p1, p2


if __name__ == "__main__":
    with open("./input/15.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
