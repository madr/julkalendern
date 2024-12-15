from output import sints, vdbg


def solve(data, find_easter_egg=False, display_easter_egg=True):
    W = 101
    H = 103
    easter_egg_recurring = 103
    easter_egg_offset = 64
    robots = [sints(line) for line in data.splitlines()]
    state = {}
    for id, robot in enumerate(robots):
        x, y, *_ = robot
        state[id] = (x, y)
    i = 0
    easter_egg_appearance = 7892
    while i < easter_egg_appearance:
        if i == 100:
            midW = W // 2
            midH = H // 2
            safety_factor_t100 = (
                sum(0 <= x < midW and 0 <= y < midH for x, y in state.values())
                * sum(midW < x < W and 0 <= y < midH for x, y in state.values())
                * sum(0 <= x < midW and midH < y < H for x, y in state.values())
                * sum(midW < x < W and midH < y < H for x, y in state.values())
            )
        for id, props in enumerate(robots):
            _ix, _iy, vx, vy = props
            x, y = state[id]
            state[id] = ((x + vx) % W, (y + vy) % H)
        i += 1
        if find_easter_egg:
            if i % easter_egg_recurring == easter_egg_offset:
                vdbg(state.values(), H, W)
                print(i)
                input("--- any key pls ---")
    if display_easter_egg:
        easter_egg = [
            (y - 26, x - 23)
            for x, y in state.values()
            if 20 <= x <= 53 and 24 <= y <= 60
        ]
        max_y, max_x = max(easter_egg)
        vdbg(easter_egg, max_y + 1, max_x + 1)
        print("")
    return safety_factor_t100, easter_egg_appearance


if __name__ == "__main__":
    with open("./input/14.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp, display_easter_egg=False)

    print(p1)
    print(p2)
