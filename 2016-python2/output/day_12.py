from output import answer  # , matrix, D, DD, ADJ, ints, mhd, mdbg, vdbg

n = 12
title = "Leonardo's Monorail"


@answer(1, "Value of registry a will be {} on exit")
def part_1(presolved):
    return presolved[0]


@answer(
    2, "If register c is initialized with 1, value of registry a will be {} on exit"
)
def part_2(presolved):
    return presolved[1]


def solve(data):
    p = data.splitlines()
    pl = len(p)

    def run(r):
        i = 0
        while i < pl:
            o, *a = p[i].split()
            match o:
                case "cpy":
                    kv, t = a
                    r[t] = int(kv) if kv.isdigit() else r[kv]
                    i += 1
                case "jnz":
                    kv, d = a
                    c = int(kv) if kv.isdigit() else r[kv]
                    i += 1 if c == 0 else int(d)
                case "inc":
                    r[a[0]] += 1
                    i += 1
                case "dec":
                    r[a[0]] -= 1
                    i += 1
        return r["a"]

    p1 = run(
        {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
        }
    )
    p2 = run(
        {
            "a": 0,
            "b": 0,
            "c": 1,
            "d": 0,
        }
    )
    return p1, p2


if __name__ == "__main__":
    with open("./input/12.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 318009
    assert b == 9227663
