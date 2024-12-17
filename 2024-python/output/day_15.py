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
            moved = False

            match move:
                case "^":
                    targets = [((v, c), grid[(v, c)]) for v in range(r)][::-1]
                case "<":
                    targets = [((r, v), grid[(r, v)]) for v in range(c)][::-1]
                case "v":
                    targets = [((v, c), grid[(v, c)]) for v in range(r + 1, H)]
                case ">":
                    targets = [((r, v), grid[(r, v)]) for v in range(c + 1, W)]

            if "." not in map(lambda pv: pv[1], targets):
                continue

            if grid[(r + dr, c + dc)] == ".":
                moved = True

            if grid[(r + dr, c + dc)] == "O" or (
                grid[(r + dr, c + dc)] in "[]" and dc != 0
            ):
                canmove = False
                flips = []

                for tpos, tvalue in targets:
                    flips.append((tpos, tvalue))

                    if tvalue == "#":
                        break

                    if tvalue == ".":
                        canmove = True
                        break

                if canmove:
                    rotated = [value for _, value in flips]
                    rotated = rotated[-1:] + rotated[:-1]

                    for offset, pos in enumerate(flips):
                        grid[pos[0]] = rotated[offset]

                    moved = True

            if grid[(r + dr, c + dc)] in "[]" and dc == 0 and dr != 0:
                canmove = True
                bs = set()
                bmod = O[move][0]

                Q = [(r + bmod, c)]

                while Q:
                    rr, cc = Q.pop(0)

                    if (rr, cc) in bs:
                        continue

                    bs.add((rr, cc))

                    if grid[(rr, cc)] == "#":
                        canmove = False
                        continue

                    if grid[(rr, cc)] in "@.":
                        continue

                    match grid[(rr, cc)]:
                        case "]":
                            Q.append((rr + bmod, cc))
                            Q.append((rr, cc - 1))
                        case "[":
                            Q.append((rr + bmod, cc))
                            Q.append((rr, cc + 1))

                if canmove:
                    patchset = {
                        (rr, cc): (rr + bmod, cc)
                        for rr, cc in bs
                        if grid[(rr, cc)] != "."
                    }

                    dotset = set(bs) - set(patchset.values())

                    for psf, pst in sorted(patchset.items())[::-bmod]:
                        psnv = grid[psf]
                        grid[pst] = psnv

                    for rk in dotset:
                        grid[rk] = "."

                    moved = True

            if moved:
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
