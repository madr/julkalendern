import re


def solve(data):
    row_count = len(data.split())
    col_count = len(data.split()[0])
    grid = [c for r in data.split() for c in r]
    grid_rotated = [c for r in zip(*data.split()[::-1]) for c in r]
    needle = r"(?=(XMAS|SAMX))"

    xmas_occourences = len(re.findall(needle, data))
    xmas_occourences += len(
        re.findall(
            needle,
            "\n".join(["".join(r) for r in list(zip(*data.split()))]),
        )
    )

    for cells, o in [
        (grid, col_count),
        (grid[::-1], col_count),
        (grid_rotated, row_count),
        (grid_rotated[::-1], row_count),
    ]:
        xmas_occourences += sum(
            all(
                [
                    i % o < (o - 3),
                    cells[i] == "X",
                    cells[i + o + 1] == "M",
                    cells[i + 2 * (o + 1)] == "A",
                    cells[i + 3 * (o + 1)] == "S",
                ]
            )
            for i in range(len(cells) - 3 * (o + 1))
        )

    x_mas_occourences = sum(
        [
            1 <= (i % col_count) < col_count - 1
            and grid[i] == "A"
            and any(
                [
                    all(
                        [
                            grid[i - col_count - 1] == "M",
                            grid[i - col_count + 1] == "M",
                            grid[i + col_count - 1] == "S",
                            grid[i + col_count + 1] == "S",
                        ]
                    ),
                    all(
                        [
                            grid[i - col_count - 1] == "S",
                            grid[i - col_count + 1] == "S",
                            grid[i + col_count - 1] == "M",
                            grid[i + col_count + 1] == "M",
                        ]
                    ),
                    all(
                        [
                            grid[i - col_count - 1] == "M",
                            grid[i - col_count + 1] == "S",
                            grid[i + col_count - 1] == "M",
                            grid[i + col_count + 1] == "S",
                        ]
                    ),
                    all(
                        [
                            grid[i - col_count - 1] == "S",
                            grid[i - col_count + 1] == "M",
                            grid[i + col_count - 1] == "S",
                            grid[i + col_count + 1] == "M",
                        ]
                    ),
                ]
            )
            for i in range(col_count + 1, len(grid) - col_count - 1)
        ]
    )

    return xmas_occourences, x_mas_occourences


if __name__ == "__main__":
    with open("./input/04.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
