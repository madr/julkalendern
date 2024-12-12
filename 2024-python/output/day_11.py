from collections import defaultdict

from output import ints


def solve(data):
    state = defaultdict(int)
    for e in ints(data):
        state[e] += 1
    for lap in range(75):
        if lap == 25:
            stones_count_25 = sum(state.values())
        queue = list(map(lambda x: x, state.items()))
        for e, delta in queue:
            if e == 0:
                state[1] += delta
                state[0] -= delta
            elif len(str(e)) % 2 == 0:
                i = len(str(e)) // 2
                l, r = int(str(e)[:i]), int(str(e)[i:])
                state[l] += delta
                state[r] += delta
                state[e] -= delta
            else:
                state[e * 2024] += delta
                state[e] -= delta
    stones_count_75 = sum(state.values())
    return stones_count_25, stones_count_75


if __name__ == "__main__":
    with open("./input/11.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
