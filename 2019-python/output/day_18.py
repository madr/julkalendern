from output import answer, matrix  # D, DD, ADJ, ints, mhd, mdbg, vdbg

n = 18
title = "Many-Worlds Interpretation"


@answer(1, "Answer is {}")
def part_1(outputs):
    return outputs[0]


@answer(2, "Actually, answer is {}")
def part_2(outputs):
    return outputs[1]


def solve(data):
    M, h, w = matrix(data)
    p = None
    for r in range(h):
        for c in range(w):
            if M[r][c] == "@":
                p = (r, c)
                break
        if p:
            break
    print(p)

    return None, None


if __name__ == "__main__":
    # use dummy data
    inp = """
#########
#b.A.@.a#
#########
    """.strip()

    # uncomment to instead use stdin
    # import sys; inp = sys.stdin.read().strip()

    # uncomment to use AoC provided puzzle input
    # with open("./input/18.txt", "r") as f:
    #     inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    # b = part_2(inp)

    # uncomment and replace 0 with actual output to refactor code
    # and ensure nonbreaking changes
    # assert a == 0
    # assert b == 0
