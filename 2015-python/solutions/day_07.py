from collections import defaultdict

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "07.txt"

    def __str__(self):
        return "Day 7: Some Assembly Required"

    def solve(self, pi):
        return self._solve(pi)

    def solve_again(self, pi):
        a = self.solve(pi)
        return self._solve(pi.replace("19138", str(a)))

    def parse_input(self, data):
        return data.strip()

    def _solve(self, pi):
        p = pi.splitlines()
        w = defaultdict(int)

        while p:
            np = []
            for l in p:
                x, to = l.split(" -> ")
                if x.isdigit():
                    w[to] += int(x)
                elif len(x.split()) == 1:
                    if x not in w:
                        np.append(l)
                    else:
                        w[to] += w[x]
                elif x.startswith("NOT "):
                    a = x.split()[-1]
                    if a.isdigit() or a in w:
                        a = int(a) if a.isdigit() else w[a]
                        w[to] += ~a
                    else:
                        np.append(l)
                else:
                    a, v, b = x.split()
                    if (a.isdigit() or a in w) and (b.isdigit() or b in w):
                        a = int(a) if a.isdigit() else w[a]
                        b = int(b) if b.isdigit() else w[b]
                        match v:
                            case "RSHIFT":
                                w[to] += a >> b
                            case "LSHIFT":
                                w[to] += a << b
                            case "AND":
                                w[to] += a & b
                            case "OR":
                                w[to] += a | b
                    else:
                        np.append(l)
            p = np
        return w["a"]


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
