from collections import deque

from output import ints


def solve(data):
    R, program = data.split("\n\n")
    R = {k: int(v) for k, v in zip("abc", ints(R))}
    program = ints(program)
    P = ",".join(map(str, program))

    p1 = org_version(R["a"], program)
    p2 = float("inf")

    Q = deque([1])
    while Q:
        x = Q.popleft()
        for i in range(8):
            o = org_version(x + i, program)
            if P.endswith(o):
                if o == P:
                    p2 = min(p2, x + i)
                else:
                    Q.append((x + i) * 8)

    return p1, p2


def org_version(A, program):
    R = {"a": A, "b": 0, "c": 0}

    def combo(v):
        return v if v < 4 else R[chr(93 + v)]

    i = 0
    out = []
    while i < len(program):
        cl = program[i + 1]
        match program[i]:
            case 0:
                R["a"] = R["a"] // (2 ** combo(cl))
                i += 2
            case 1:
                a, b = R["b"], cl
                R["b"] = a ^ b
                i += 2
            case 2:
                R["b"] = combo(cl) % 8
                i += 2
            case 3:
                i = (i + 2) if R["a"] == 0 else cl
            case 4:
                a, b = R["b"], R["c"]
                R["b"] = a ^ b
                i += 2
            case 5:
                out.append(combo(cl) % 8)
                i += 2
            case 6:
                R["b"] = R["a"] // (2 ** combo(cl))
                i += 2
            case 7:
                R["c"] = R["a"] // (2 ** combo(cl))
                i += 2
    return ",".join(map(str, out))


if __name__ == "__main__":
    with open("./input/17.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
