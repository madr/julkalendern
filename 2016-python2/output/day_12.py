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

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
