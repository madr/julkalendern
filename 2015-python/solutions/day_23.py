from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "23.txt"

    def __str__(self):
        return "Day 23: Opening the Turing Lock"

    def _solve(self, pi):
        p12 = []
        for a in [0, 1]:
            m = {
                "a": a,
                "b": 0,
            }
            p = [l.split() for l in pi.splitlines()]
            i = 0
            while i < len(p):
                v, rv, *a = p[i]
                rv = rv.split(",")[0]
                match v:
                    case "hlf":
                        m[rv] //= 2
                        i += 1
                    case "tpl":
                        m[rv] *= 3
                        i += 1
                    case "inc":
                        m[rv] += 1
                        i += 1
                    case "jmp":
                        i += int(rv)
                    case "jie":
                        i += int(a[0]) if int(m[rv]) % 2 == 0 else 1
                    case "jio":
                        i += int(a[0]) if int(m[rv]) == 1 else 1
            p12.append(m["b"])
        return p12

    def solve(self, pi):
        o = self._solve(pi)
        return o[0]

    def solve_again(self, pi):
        o = self._solve(pi)
        return o[1]

    def parse_input(self, data):
        return data.strip()


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
