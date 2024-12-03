from itertools import combinations
from math import lcm

from output import answer, ints  # , matrix, D, DD, ADJ, ints, mhd, mdbg, vdbg

n = 12
title = "The N-Body Problem"


@answer(1, "Answer is {}")
def part_1(outputs):
    return outputs[0]


@answer(2, "Actually, answer is {}")
def part_2(outputs):
    return outputs[1]


def solve(data):
    M = [[ints(l), [0, 0, 0]] for l in data.splitlines()]

    def G(m):
        def U(x, y):
            if x > y:
                return -1
            elif x < y:
                return 1
            return 0

        for i, j in combinations(range(len(m)), r=2):
            m1 = m[i]
            m2 = m[j]
            g1, v1 = m1
            g2, v2 = m2
            x1, y1, z1 = g1
            x2, y2, z2 = g2
            a1, b1, c1 = v1
            a2, b2, c2 = v2
            m[i] = [
                g1,
                [
                    a1 + U(x1, x2),
                    b1 + U(y1, y2),
                    c1 + U(z1, z2),
                ],
            ]
            m[j] = [
                g2,
                [
                    a2 + U(x2, x1),
                    b2 + U(y2, y1),
                    c2 + U(z2, z1),
                ],
            ]

        return m

    def V(m):
        nm = []
        for gv in m:
            g, v = gv
            x1, y1, z1 = g
            x2, y2, z2 = v
            nm.append(
                [
                    [
                        x1 + x2,
                        y1 + y2,
                        z1 + z2,
                    ],
                    v,
                ]
            )
        return nm

    P1 = M.copy()
    for _ in range(1000):
        P1 = V(G(P1))
    p1 = sum(sum(map(abs, p)) * sum(map(abs, k)) for p, k in P1)
    P2 = M.copy()
    p2 = []
    for i, igv in enumerate(zip(*[g for g, v in P2])):
        igv = [(g, 0) for g in igv]
        Q = P2.copy()
        C = 0
        while True:
            Q = V(G(Q))
            C += 1
            sg = list(zip(*[g for g, v in Q]))[i]
            sv = list(zip(*[v for g, v in Q]))[i]
            if list(zip(sg, sv)) == igv:
                p2.append(C)
                break
    p2 = lcm(*p2)
    return p1, p2


if __name__ == "__main__":
    with open("./input/12.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 12466
    assert b == 360689156787864
