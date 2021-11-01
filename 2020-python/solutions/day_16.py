import re
from collections import defaultdict

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "16.txt"

    def __str__(self):
        return "Day 16: Ticket Translation"

    def parse_input(self, data):
        def get_ranges(line):
            label = line.split(":")[0]
            r1a, r1b, r2a, r2b = re.findall(rxranges, line.strip())
            return (label, range(int(r1a), int(r1b) + 1), range(int(r2a), int(r2b) + 1))

        rxranges = r"([0-9]+)"
        ranges, golden_ticket, other_tickets = data.split("\n\n")
        ranges = [*map(get_ranges, ranges.splitlines())]
        golden_ticket = [*map(int, golden_ticket.splitlines()[1].split(","))]
        other_tickets = [
            [*map(int, ticket.split(","))] for ticket in other_tickets.splitlines()[1:]
        ]
        return (ranges, golden_ticket, other_tickets)

    def get_invalid_values(self, ranges, ticket):
        def not_in_any_range(x):
            return all(x not in r1 and x not in r2 for _, r1, r2 in ranges)

        return [*filter(not_in_any_range, ticket)]

    def solve(self, puzzle_input):
        ranges, _, tickets = puzzle_input
        error_rate = 0
        valid_tickets = []
        for ticket in tickets:
            error_rate += sum(self.get_invalid_values(ranges, ticket))
        return error_rate

    def solve_again(self, puzzle_input):
        ranges, golden_ticket, tickets = puzzle_input
        valid_tickets = []
        for ticket in tickets:
            if len(self.get_invalid_values(ranges, ticket)) == 0:
                valid_tickets.append(ticket)
        sorted_ranges = self.get_positions(ranges, valid_tickets)
        factors = [i for i, r in enumerate(sorted_ranges) if "departure" in r]
        m = 1
        for f in factors:
            m *= golden_ticket[f]
        return m

    def get_positions(self, ranges, valid_tickets):
        columns = [*zip(*valid_tickets)]
        matches = defaultdict(lambda: set())
        # Step 1: find all possible range matches for columns
        # Example: {'row': {0, 1, 2}, 'class': {1, 2}, 'seat': {2}}
        for e, column in enumerate(columns):
            for column_name, r1, r2 in ranges:
                if all(x in r1 or x in r2 for x in column):
                    matches[column_name].add(e)
        # Step 2: collect all columns with only one matching range, and subtract
        # these ranges from the columns having multiple ranges. Repeat until all
        # columns only have one matching range.
        # Example:
        #       #1: {'row': {0, 1, 2}, 'class': {1, 2}, 'seat': {2}}
        #       #2: {'row': {0, 1}, 'class': {1}, 'seat': {2}}
        #       #3: {'row': {0}, 'class': {1}, 'seat': {2}}
        while any(len(v) > 1 for _k, v in matches.items()):
            singles = set({}).union(*[v for _k, v in matches.items() if len(v) == 1])
            for m in matches:
                if len(matches[m]) > 1:
                    matches[m] = matches[m] - singles
        # step 3: Sort the matches list and return a list only containing the
        # column names.
        final = sorted([(k, v.pop()) for k, v in matches.items()], key=lambda kv: kv[1])
        return [k for k, _v in final]


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
