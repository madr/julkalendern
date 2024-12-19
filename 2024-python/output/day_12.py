from collections import deque

from output import D, Di, cw, matrix


def solve(data):
    grid, H, W = matrix(data)
    fence_cost = 0
    fence_cost_w_discount = 0
    seen = set()
    for r in range(H):
        for c in range(W):
            if (r, c) in seen:
                continue
            id = grid[r][c]
            regions = set()
            perimeters = 0
            q = deque([(r, c)])
            while q:
                rc = q.popleft()
                if rc in seen:
                    continue
                seen.add(rc)
                regions.add(rc)
                y, x = rc
                for delta_y, delta_x in D:
                    yn, xn = y + delta_y, x + delta_x
                    if (0 <= yn < H and 0 <= xn < W) and grid[yn][xn] == id:
                        q.append((yn, xn))
                    else:
                        perimeters += 1
            if len(regions) <= 2:
                corners = 4
            else:
                corners = count_corners(regions)
            fence_cost += len(regions) * perimeters
            fence_cost_w_discount += len(regions) * corners
    return fence_cost, fence_cost_w_discount


def count_corners(region):
    corners = 0
    for y, x in region:
        for delta_y, delta_x in D:
            # convex corners: one horisontal and one vertical
            # neighbor are not members of region
            delta_ycw, delta_xcw = cw(delta_y, delta_x)
            if (y + delta_y, x + delta_x) not in region and (
                y + delta_ycw,
                x + delta_xcw,
            ) not in region:
                corners += 1
        for delta_y, delta_x in Di:
            # concave corners: the diagonal neighbor are not
            # member of region, but the connected horisontal
            # and vertical neighbors are
            if (
                (y + delta_y, x + delta_x) not in region
                and (y + delta_y, x) in region
                and (y, x + delta_x) in region
            ):
                corners += 1
    return corners


if __name__ == "__main__":
    with open("./input/12.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
