from solutions import BaseSolution


class Program:
    def __init__(self, data=None):
        if data:
            name, weight, disc = self._parse(data)
            self.name = name
            self.weight = weight
            self.disc = disc

    def __repr__(self):
        return str(self.name)

    def _parse(self, data):
        disc = []
        try:
            name, weight = data.split()
        except ValueError:
            name, weight, _, *disc = data.split()
        weight = int(weight[1:len(weight) - 1])
        disc = tuple(p.replace(',', '') for p in disc)
        return name, weight, disc

    def has_disc(self):
        return len(self.disc) > 0

    def unseen_discs(self, seen_discs):
        return [t for t in self.disc if t not in seen_discs]


class Solution(BaseSolution):
    input_file = '07.txt'

    def __str__(self):
        return 'Day 7: Recursive Circus'

    def _get_programs(self, puzzle_input):
        return [Program(data) for data in puzzle_input.splitlines()]

    def _get_discs(self, disc, programs):
        subdisc = [{'own_weight': p.weight, 'obj': p} for p in programs if p.name in disc]
        for t in subdisc:
            t['weight'] = t['own_weight']
            if t['obj'].has_disc():
                t['disc'] = self._get_discs(t['obj'].disc, programs)
                t['weight'] += sum([st['weight'] for st in t['disc']])
            del (t['obj'])
        return subdisc

    def _find_unbalanced_disc(self, disc):
        disc = sorted(disc, key=lambda t: t['weight'])
        if not disc[0]['weight'] < disc[1]['weight']:
            disc = sorted(disc, key=lambda t: t['weight'], reverse=True)
        return disc[0], disc[1]['weight'] - disc[0]['weight']

    def solve(self, puzzle_input):
        programs = self._get_programs(puzzle_input)
        programs_with_discs = []
        seen = []
        for p in programs:
            if p.has_disc():
                programs_with_discs.append(p)
            else:
                seen.append(p.name)
        for p in programs_with_discs:
            unseen = p.unseen_discs(seen)
            if len(unseen) > 0:
                seen += unseen
        bottom_program = list(filter(lambda p: p.name not in seen, programs_with_discs))[0]
        return bottom_program

    def solve_again(self, puzzle_input):
        programs = self._get_programs(puzzle_input)
        bottom_program = self.solve(puzzle_input)
        disc_tree = {
            'own_weight': bottom_program.weight,
            'disc': self._get_discs(bottom_program.disc, programs)
        }
        diff = -1
        unbalanced = True
        while unbalanced:
            disc, new_diff = self._find_unbalanced_disc(disc_tree['disc'])
            if new_diff == 0:
                unbalanced = False
            else:
                disc_tree = disc
                diff = new_diff
        return disc_tree['own_weight'] + diff


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
