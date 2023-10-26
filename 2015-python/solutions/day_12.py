import json
import re
from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "12.txt"

    def __str__(self):
        return "Day 12: JSAbacusFramework.io"

    def parse_input(self, data):
        return data.strip()

    def solve(self, puzzle_input):
        digits = re.compile(r"-?\d+")
        return sum(map(int, re.findall(digits, puzzle_input)))

    def solve_again(self, puzzle_input):
        def nodesum(node):
            if isinstance(node, int):
                return node
            if isinstance(node, str):
                return 0
            if isinstance(node, list):
                return sum(nodesum(i) for i in node)
            if isinstance(node, object):
                if "red" in node.values():
                    return 0
                return sum(nodesum(i) for i in node.values())

        nodes = json.loads(puzzle_input)
        return nodesum(nodes)


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
