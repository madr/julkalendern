from collections import deque

from output import ints


def solve(data):
    mul_add = calculate(data)
    mul_add_concat = calculate(data, concat=True)
    return mul_add, mul_add_concat


def calculate(data, concat=False):
    values = list()
    for nums in [ints(line) for line in data.splitlines()]:
        T, start, *nums = nums
        E = len(nums)
        q = deque([(0, start)])
        ok = False
        while q:
            i, value = q.pop()
            if i == E:
                if value == T:
                    ok = True
                continue
            if (a := value + nums[i]) <= T:
                q.append((i + 1, a))
            if (b := value * nums[i]) <= T:
                q.append((i + 1, b))
            if concat and (c := int(f"{value}{nums[i]}")) <= T:
                q.append((i + 1, c))
        if ok:
            values.append(T)
    return sum(values)


if __name__ == "__main__":
    with open("./input/07.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
