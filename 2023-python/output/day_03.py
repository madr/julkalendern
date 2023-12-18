from collections import deque
from output import answer

n = 3
title = "Gear Ratios"


@answer(1, "Sum of all part numbers is {} in the engine schematic")
def part_1(presolved):
    s, _ = presolved
    return s


@answer(2, "Gear ratio sums is {} in the engine schematic")
def part_2(presolved):
    _, gr = presolved
    return gr


def presolve(data):
    data = data.split()
    adj = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
    w = len(data[0])
    h = len(data)
    s = list()
    gr = list()
    for y in range(w):
        for x in range(h):
            if data[y][x] != "." and not data[y][x].isdigit():
                seen = set()
                t = list()
                for oy, ox in adj:
                    if (y + oy, x + ox) in seen:
                        continue
                    if data[y + oy][x + ox].isdigit():
                        n = deque([data[y + oy][x + ox]])
                        i = x + ox - 1
                        while i in range(w) and data[y + oy][i].isdigit():
                            n.append(data[y + oy][i])
                            seen.add((y + oy, i))
                            i -= 1
                        i = x + ox + 1
                        while i in range(w) and data[y + oy][i].isdigit():
                            n.appendleft(data[y + oy][i])
                            seen.add((y + oy, i))
                            i += 1
                        t.append(sum(10**m * int(d) for m, d in enumerate(n)))
                # part 1
                s.append(sum(t))
                # part 2
                if data[y][x] == "*" and len(t) == 2:
                    a, b = t
                    gr.append(a * b)

    return sum(s), sum(gr)


if __name__ == "__main__":
    with open("./input/03.txt", "r") as f:
        inp = f.read().strip()

    parsed = presolve(inp)

    a = part_1(parsed)
    b = part_2(parsed)

    assert a == 553825
    assert b == 93994191
