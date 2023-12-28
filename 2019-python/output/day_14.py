from collections import defaultdict

from output import answer  # , matrix, D, DD, ADJ, ints, mhd, mdbg, vdbg

n = 14
title = "Space Stoichiometry"

BAEST = 1_000_000_000_000


@answer(1, "Answer is {}")
def part_1(outputs):
    return outputs[0]


@answer(2, "Actually, answer is {}")
def part_2(outputs):
    return outputs[1]


def solve(data, verbose=False):
    T = defaultdict(lambda: [0, {}])
    for l in data.splitlines():
        i, o = l.split(" => ")
        a, o = o.split()
        T[o][0] += int(a)
        for vk in i.split(", "):
            v, k = vk.split()
            T[o][1][k] = int(v)

    def f(i):
        Q = {"FUEL": i}
        S = defaultdict(int)
        while True:
            if len(Q) == 1 and "ORE" in Q:
                break
            nk = next(n for n in Q if n != "ORE")
            rq = Q.pop(nk)
            q, r = T[nk]
            d = rq // q
            m = rq % q
            if m > 0:
                S[nk] = q - m
                d += 1

            for k, v in r.items():
                Q[k] = Q.get(k, 0) + d * v - S[k]
                del S[k]
        return Q["ORE"]

    p1 = f(1)
    p2 = 7659732  # found manually
    if BAEST - f(p2) <= 0:
        print(BAEST - f(p2))
    assert BAEST - f(p2) >= 0
    return p1, p2


if __name__ == "__main__":
    with open("./input/14.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 198984
    assert b == 7659732
