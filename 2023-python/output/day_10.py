from output import answer

n = 10
title = "dddd"


@answer(1, "Answer is {}")
def part_1(data):
    return data


@answer(2, "Actually, answer is {}")
def part_2(data):
    return data


# uncomment to solve parts in one go
# def presolve(data):
#     return data


if __name__ == "__main__":
    # use dummy data
    inp = """
        replace me
    """.strip()

    # uncomment to instead use stdin
    # import sys; inp = sys.stdin.read().strip()

    # uncomment to use AoC provided puzzle input
    # with open(f"./input/10.txt", "r") as f:
    #     inp = f.read()

    # uncomment to do initial data processing shared by part 1-2
    # inp = presolve(inp)

    a = part_1(inp)
    # b = part_2(inp)

    # uncomment and replace 0 with actual output to refactor code
    # and ensure nonbreaking changes
    # assert a == 0
    # assert b == 0
