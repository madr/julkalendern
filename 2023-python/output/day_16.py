from itertools import chain

from output import D, answer, matrix

n = 16
title = "The Floor Will Be Lava"


@answer(1, "Energized tiles count, starting at top-left facing right: {}")
def part_1(presolved):
    return presolved[0]


@answer(2, "Max energized tiles count, starting from all edges: {}")
def part_2(presolved):
    return presolved[1]


def presolve(data):
    m, w, h = matrix(data)
    p1 = 0
    p2 = 0
    for sp in chain(
        [(h - 1, n, 0) for n in range(w)],
        [(n, 0, 1) for n in range(h)],
        [(0, n, 2) for n in range(w)],
        [(n, w - 1, 3) for n in range(h)],
    ):
        q = [sp]
        seen = set()
        while q:
            rcd = q.pop(0)
            if (rcd) in seen:
                continue
            r, c, d = rcd
            if r < 0 or r >= h or c < 0 or c >= w:
                continue
            seen.add((r, c, d))
            match m[r][c]:
                case ".":
                    o1, o2 = D[d]
                    q.append((o1 + r, o2 + c, d))
                case "|":
                    if d in [0, 2]:
                        o1, o2 = D[d]
                        q.append((o1 + r, o2 + c, d))
                    else:
                        for d in [(d - 1) % 4, (d + 1) % 4]:
                            o1, o2 = D[d]
                            q.append((o1 + r, o2 + c, d))
                case "-":
                    if d in [1, 3]:
                        o1, o2 = D[d]
                        q.append((o1 + r, o2 + c, d))
                    else:
                        for d in [(d - 1) % 4, (d + 1) % 4]:
                            o1, o2 = D[d]
                            q.append((o1 + r, o2 + c, d))
                case "\\":
                    d += 1 if d in [1, 3] else -1
                    d = d % 4
                    o1, o2 = D[d]
                    q.append((o1 + r, o2 + c, d))
                case "/":
                    d += 1 if d in [0, 2] else -1
                    d = d % 4
                    o1, o2 = D[d % 4]
                    q.append((o1 + r, o2 + c, d))
        b = len(set([(r, c) for r, c, d in seen]))
        if sp == (0, 0, 1):
            p1 = b
        p2 = max(p2, b)
    return p1, p2


if __name__ == "__main__":
    with open("./input/16.txt", "r") as f:
        inp = f.read().strip()

    inp = presolve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 7884
    assert b == 8185
