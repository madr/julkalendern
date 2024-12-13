from output import ints


def solve(data):
    offset = 10_000_000_000_000
    machines = data.split("\n\n")
    p1 = ratio(machines)
    p2 = ratio(machines, offset)
    return p1, p2


def ratio(machines, offset=0):
    cost = 0
    for mid, config in enumerate(machines):
        a_x, a_y, b_x, b_y, goal_x, goal_y = ints(config)

        goal_x, goal_y = goal_x + offset, goal_y + offset

        ratio = (goal_x * a_y - goal_y * a_x) / (goal_y * b_x - goal_x * b_y)
        a_presses = round(goal_x / (b_x * ratio + a_x))
        b_presses = round(a_presses * ratio)

        a_presses, b_presses = int(a_presses), int(b_presses)
        if (a_x + a_y) * a_presses + (b_x + b_y) * b_presses == goal_x + goal_y:
            cost += 3 * a_presses + b_presses
    return cost


if __name__ == "__main__":
    with open("./input/13.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
