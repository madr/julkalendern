import re
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import chain, combinations, compress, permutations

from output import ADJ, DD, D, ccw, cw, ints, matrix, mdbg, mhd, vdbg


def solve(data):
    o = {k:v for k, v in zip("^>v<", D)}
    grid, movements = data.split("\n\n")
    grid, H, W = matrix(grid)
    movements = "".join(movements.split())
    grid1 = {(r, c):col for r, row in enumerate(grid) for c, col in enumerate(row)}
    grid2 = {}
    for k, v in grid1.items():
        r2, c2 = k
        match v:
            case "O":
                grid2[(r2, c2 * 2)] = "["
                grid2[(r2, c2 * 2 + 1)] = "]"
            case "@":
                grid2[(r2, c2 * 2)] = "@"
                grid2[(r2, c2 * 2 + 1)] = "."
            case _:
                grid2[(r2, c2 * 2)] = v
                grid2[(r2, c2 * 2 + 1)] = v
    ans = []
    for grid in [grid1, grid2]:
        pos = [(r, c) for r in range(H) for c in range(W) if grid[(r,c)] == "@"][0]
        for T, move in enumerate(movements):
            r, c = pos
            targets = closest(grid, r, c, move, W, H)
            if "." not in map(lambda pv: pv[1], targets):
                continue
            dr, dc = o[move]
            moved = False
            if grid[(r + dr, c + dc)] == ".":
                moved = True
            if grid[(r + dr, c + dc)] == "O" or (grid[(r + dr, c + dc)] in "[]" and dc != 0):
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
                    rotated = [rtv for rtp, rtv in flips]
                    rotated = rotated[-1:] + rotated[:-1]
                    for fi, rtp in enumerate(flips):
                        rtp, *_ = rtp
                        grid[rtp] = rotated[fi]
                    moved = True
            if grid[(r + dr, c + dc)] in "[]" and dc == 0 and dr != 0:
                # move cluster of boxes
                canmove = False
                flips = []
                for tpos, tvalue in targets:
                    flips.append((tpos, tvalue))
                    if tvalue == "#":
                        break
                    if tvalue == ".":
                        canmove = True
                        break
                    if tvalue == "[":
                        # look on right side
                        # targets = closest(grid, r, c, move)
                        pass
                    if tvalue == "]":
                        # look on right side
                        # targets = closest(grid, r, c, move)
                        pass
                if canmove:
                    rotated = [rtv for rtp, rtv in flips]
                    rotated = rotated[-1:] + rotated[:-1]
                    for fi, rtp in enumerate(flips):
                        rtp, *_ = rtp
                        grid[rtp] = rotated[fi]
                    moved = True
                pass
            if moved:
                grid[(r, c)] = "."
                grid[(r + dr, c + dc)] = "@"
                pos = r + dr, c + dc
            if False and T > 67:
                print(T, move)
                print(targets)
                show(grid, H, W)
                input("--- any key or gtfo ---")
        ans.append(sum(k[0] * 100 + k[1] for k, v in grid.items() if v in "O["))
    p1, p2 = ans
    return p1, p2

def show(grid, H, W):
    for r in range(H):
        for c in range(W):
            print(grid[(r,c)], end="")
        print("")
    print("")

def closest(grid, r, c, move, W, H):
    match move:
        case "^":
            targets = [((v,c), grid[(v,c)]) for v in range(r)][::-1]
        case "<":
            targets = [((r,v), grid[(r,v)]) for v in range(c)][::-1]
        case "v":
            targets = [((v,c), grid[(v,c)]) for v in range(r+1,H)]
        case ">":
            targets = [((r,v), grid[(r,v)]) for v in range(c+1,W)]
    return targets


if __name__ == "__main__":
    import os

    # use dummy data
    inp = """
    ##########
    #..O..O.O#
    #......O.#
    #.OO..O.O#
    #..O@..O.#
    #O#..O...#
    #O..O..O.#
    #.OO.O.OO#
    #....O...#
    ##########

    <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
    vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
    ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
    <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
    ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
    ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
    >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
    <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
    ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
    v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^

    """.strip()

    # uncomment to instead use stdin
    # import sys; inp = sys.stdin.read().strip()

    # uncomment to use AoC provided puzzle input
    with open("./input/15.txt", "r") as f:
        insp = f.read().strip()

    # uncomment to do initial data processing shared by part 1-2
    p1, p2 = solve(inp)

    print(p1)
    os.system(f"echo {p1} | wl-copy")
    print(p2)
    os.system(f"echo {p2} | wl-copy")

    # uncomment and replace 0 with actual output to refactor code
    # and ensure nonbreaking changes
    # assert p1 == 1426855
    # assert p2 == 0
