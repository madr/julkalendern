import re

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "25.txt"

    def __str__(self):
        return "Day 25: Let It Snow"

    def solve(self, pi):
        r, c = [int(s) - 1 for s in re.findall(r"\d+", pi)]
        v = 20151125
        seen = set()
        e = rc2p(r, c)
        t = 0
        while v not in seen:
            seen.add(v)
            v = v * 252533 % 33554393
            t += 1
        for _ in range(e % t - 1):
            v = v * 252533 % 33554393
        assert v == 9132360
        return v

    def solve_again(self, pi):
        return "God jul!"

    def parse_input(self, data):
        return data.strip()


def p2rc(p):
    """
    Get row and column for a storage position

    >>> p2rc(1)
    (0, 0)
    >>> p2rc(2)
    (1, 0)
    >>> p2rc(3)
    (0, 1)
    >>> p2rc(4)
    (2, 0)
    >>> p2rc(5)
    (1, 1)
    >>> p2rc(6)
    (0, 2)
    >>> p2rc(7)
    (3, 0)
    >>> p2rc(8)
    (2, 1)
    >>> p2rc(9)
    (1, 2)
    >>> p2rc(10)
    (0, 3)
    >>> p2rc(11)
    (4, 0)
    >>> p2rc(12)
    (3, 1)
    >>> p2rc(13)
    (2, 2)
    >>> p2rc(14)
    (1, 3)
    >>> p2rc(15)
    (0, 4)
    >>> p2rc(16)
    (5, 0)
    >>> p2rc(17)
    (4, 1)
    >>> p2rc(18)
    (3, 2)
    >>> p2rc(19)
    (2, 3)
    >>> p2rc(20)
    (1, 4)
    >>> p2rc(21)
    (0, 5)
    """
    v = 0
    i = 0
    while v < p:
        i += 1
        v = sum(range(i + 1))

    r, c = 0, i - 1
    for _ in range(v - p):
        r += 1
        c -= 1
    return (r, c)


def rc2p(r, c):
    """
    Get storage position for coordinate row R, column C

    >>> rc2p(0, 0)
    1
    >>> rc2p(1, 0)
    2
    >>> rc2p(0, 1)
    3
    >>> rc2p(2, 0)
    4
    >>> rc2p(1, 1)
    5
    >>> rc2p(0, 2)
    6
    >>> rc2p(3, 0)
    7
    >>> rc2p(2, 1)
    8
    >>> rc2p(1, 2)
    9
    >>> rc2p(0, 3)
    10
    >>> rc2p(4, 0)
    11
    >>> rc2p(3, 1)
    12
    >>> rc2p(2, 2)
    13
    >>> rc2p(1, 3)
    14
    >>> rc2p(0, 4)
    15
    >>> rc2p(5, 0)
    16
    >>> rc2p(4, 1)
    17
    >>> rc2p(3, 2)
    18
    >>> rc2p(2, 3)
    19
    >>> rc2p(1, 4)
    20
    >>> rc2p(0, 5)
    21
    """
    return sum(range(r + c + 1)) + c + 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    solution = Solution()
    solution.show_results()
