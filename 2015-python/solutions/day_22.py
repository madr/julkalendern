import random
import re
from math import inf

from solutions import BaseSolution

C = {
    "M": 53,
    "D": 73,
    "S": 113,
    "P": 173,
    "R": 229,
}

D = {
    "S": 6,
    "P": 6,
    "R": 5,
}

E = {
    "P": 3,
    "R": 101,
    "S": 7,
}


class Solution(BaseSolution):
    input_file = "22.txt"

    def __str__(self):
        return "Day 22: Wizard Simulator 20XX"

    def solve(self, pi):
        o = self._solve(pi)
        return o[0]

    def solve_again(self, pi):
        o = self._solve(pi)
        return o[1]

    def parse_input(self, data):
        return data.strip()

    def _solve(self, data):
        p12 = []
        boss = re.findall(r"\d+", data)
        shp, smp = 50, 500
        for hd in [False, True]:
            x = 100_000
            l = inf
            for _i in range(x):
                bhp, bd = [int(v) for v in boss]
                t, ms = 0, 0
                hp, mp = shp, smp
                e = {"S": 0, "P": 0, "R": 0}
                while hp > 0 and bhp > 0 and mp > 0:
                    if hd and t % 2 == 0:
                        hp -= 1
                        if hp == 0:
                            break
                    b = {"d": bd, "e": 0}
                    p = {"e": 0}
                    if e["P"] > 0:
                        e["P"] -= 1
                        bhp -= E["P"]
                        if bhp <= 0:
                            break
                    if e["R"] > 0:
                        e["R"] -= 1
                        mp += E["R"]
                    if e["S"] > 0:
                        e["S"] -= 1
                        p["e"] += E["S"]
                    if t % 2 == 0:
                        a = self._guess(mp, e)
                        if a in "RSP":
                            e[a] = D[a]
                        dp, db = self._turn(t, p, b, a)
                        mp -= C[a]
                        ms += C[a]
                    else:
                        dp, db = self._turn(t, p, b)
                    hp += dp
                    bhp += db
                    t += 1
                if bhp <= 0 and mp >= 0:
                    l = min(l, ms)
            p12.append(l)
        assert p12[0] == 953
        assert p12[1] == 1289
        return p12

    @staticmethod
    def _guess(mp, e):
        v = False
        while not v:
            a = random.choice("MDPRS")
            match a:
                case "S" | "P" | "R":
                    v = e[a] == 0
                case _:
                    v = True
        return a

    @staticmethod
    def _turn(t, p, b, a=None):
        """Take turns

        >>> Solution._turn(1, {}, {"d": 5})
        (-5, 0)
        >>> Solution._turn(1, {}, {"d": 5, "e": -2})
        (-5, -2)
        >>> Solution._turn(1, {"e": 7}, {"d": 5})
        (-1, 0)
        >>> Solution._turn(2, {}, {}, "M")
        (0, -4)
        >>> Solution._turn(2, {}, {}, "D")
        (2, -2)
        >>> Solution._turn(2, {}, {}, "S")
        (0, 0)
        >>> Solution._turn(2, {}, {}, "P")
        (0, 0)
        >>> Solution._turn(2, {}, {}, "R")
        (0, 0)
        """
        ped = p.get("e", 0)
        bed = b.get("e", 0)
        if t % 2 == 1:
            return min(ped - b["d"], -1), 0 + bed
        else:
            match a:
                case "D":
                    return 2, -2
                case "M":
                    return 0, -4
                case "S":
                    return 0, 0
                case "R":
                    return 0, 0
                case "P":
                    return 0, 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    solution = Solution()
    solution.show_results()
