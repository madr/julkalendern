import re
from itertools import permutations

from output import ints


def solve(data):
    data = [line.strip() for line in data.splitlines()]
    p1 = scramble(data, "abcdefgh")
    p2 = unscramble(data, "fbgdceah")
    return p1, p2


def scramble(data, subject):
    r_swap = r"(?:letter|position) (.)"
    for line in data:
        if line.startswith("rotate right"):
            x = ints(line)[0]
            subject = subject[-x:] + subject[:-x]
        if line.startswith("rotate left"):
            x = ints(line)[0]
            subject = subject[x:] + subject[:x]
        if line.startswith("rotate based"):
            x = re.findall(r"letter (.)", line)[0]
            i = subject.index(x)
            j = i + 1 % len(subject)
            subject = subject[-j:] + subject[:-j]
            if i >= 4:
                subject = subject[-1:] + subject[:-1]
        if line.startswith("swap letter"):
            x, y = re.findall(r_swap, line)
            subject = subject.replace(y, "#")
            subject = subject.replace(x, y)
            subject = subject.replace("#", x)
        if line.startswith("swap position"):
            x, y = ints(line)
            v1, v2 = subject[x], subject[y]
            subject = subject[:x] + v2 + subject[x + 1 :]
            subject = subject[:y] + v1 + subject[y + 1 :]
        if line.startswith("move"):
            x, y = ints(line)
            v = subject[x]
            subject = subject[:x] + subject[x + 1 :]
            subject = subject[:y] + v + subject[y:]
        if line.startswith("reverse"):
            x, y = ints(line)
            subject = subject[:x] + subject[x : y + 1][::-1] + subject[y + 1 :]
    return subject


def unscramble(data, T):
    for candidate in ["".join(c) for c in permutations(T)]:
        if scramble(data, candidate) == T:
            return candidate


if __name__ == "__main__":
    with open("./input/21.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
