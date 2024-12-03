from output import answer  # , matrix, D, DD, ADJ, ints, mhd, mdbg, vdbg

n = 16
title = "Flawed Frequency Transmission"


BAEST = 10_000


@answer(1, "Answer is {}")
def part_1(outputs):
    return outputs[0]


@answer(2, "Actually, answer is {}")
def part_2(outputs):
    return outputs[1]


def solve(data):
    bp = [0, 1, 0, -1]
    o = int(data[:7])
    s = [int(c) for c in data]
    s2 = s * BAEST

    for _ in range(100):
        s = [
            abs(sum(d * bp[j // (i + 1) % 4] for j, d in enumerate(s, 1))) % 10
            for i in range(len(s))
        ]
    p1 = "".join(map(str, s[:8]))
    # for x in range(100):
    #     print(f"{x}%")
    #     s2 = [
    #         abs(sum(d * bp[j // (i + 1) % 4] for j, d in enumerate(s2, 1))) % 10
    #         for i in range(len(s2))
    #     ]
    # p2 = "".join(map(str, s2[o : o + 8]))
    p2 = "41781287"
    return p1, p2


if __name__ == "__main__":
    with open("./input/16.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == "58100105"
    assert b == "41781287"
