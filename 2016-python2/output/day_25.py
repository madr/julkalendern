def solve(data):
    p = data.splitlines()
    csl = 30
    A = "01" * (csl // 2)
    i = 1
    while True:
        if A == run(
            csl,
            p.copy(),
            {
                "a": i,
                "b": 0,
                "c": 0,
                "d": 0,
            },
        ):
            break
        i += 2
    p1 = i
    return p1, None


def run(lO, p, r):
    i = 0
    pl = len(p)
    outs = []
    while i < pl and len(outs) < lO:
        o, *a = p[i].split()
        match o:
            case "cpy":
                kv, t = a
                if t in "abcd":
                    r[t] = int(kv) if kv not in "abcd" else r[kv]
                i += 1
            case "out":
                kv, *_ = a
                outs.append(f'{int(kv) if kv not in "abcd" else r[kv]}')
                i += 1
            case "jnz":
                kv, d = a
                c = int(kv) if kv not in "abcd" else r[kv]
                d = int(d) if d not in "abcd" else r[d]
                i += 1 if c == 0 else d
            case "inc":
                r[a[0]] += 1
                i += 1
            case "dec":
                r[a[0]] -= 1
                i += 1
            case "tgl":
                kv = a[0]
                c = int(kv) if kv not in "abcd" else r[kv]
                if 0 <= i + c < pl:
                    old, *v = p[i + c].split()
                    match old:
                        case "inc":
                            nw = "dec"
                        case "dec":
                            nw = "inc"
                        case "tgl":
                            nw = "inc"
                        case "jnz":
                            nw = "cpy"
                        case _:
                            nw = "jnz"
                    p[i + c] = " ".join([nw] + v)
                i += 1
    return "".join(outs)


if __name__ == "__main__":
    with open("./input/25.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
