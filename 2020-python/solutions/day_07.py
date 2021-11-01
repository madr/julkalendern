import re

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "07.txt"

    def __str__(self):
        return "Day 7: Handy Haversacks"

    def parse_input(self, data):
        rules = []
        for rule in data.splitlines():
            prnt, *children = re.findall(r"((\d+ )?(\S+ \S+)) bags?", rule.strip())
            parent_color = prnt[0]
            try:
                rules.append(
                    (parent_color, [(n, int(q.strip())) for _, q, n in children])
                )
            except ValueError:
                # "no other" case, return empty children list
                rules.append((parent_color, []))
        return rules

    def solve(self, bags):
        seen = set()
        self.child_of(bags, "shiny gold", seen)
        return len(seen)

    def solve_again(self, bags):
        return self.weight(dict(bags), "shiny gold")

    def child_of(self, bags, child, seen):
        parents = [bag[0] for bag in bags if child in str(bag[1])]
        seen.update(parents)
        for parent in parents:
            self.child_of(bags, parent, seen)

    def weight(self, rules, bag):
        children = rules[bag]
        child_weight = sum(q for _, q in children)
        child_weight += sum(q * self.weight(rules, name) for name, q in children)
        return child_weight


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
