from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '18.txt'
    sound_freq = 0
    queue = [], []
    sent = [0, 0]

    def __str__(self):
        return 'Day 18: Duet'

    def _run(self, line, registry, swag_mode=True):
        actions = 'add jgz mod mul rcv set snd'
        a, *kv = line.split()
        if len(kv) == 2:
            k, v = kv
        else:
            k = kv[0]
            v = None
        if a in actions:
            if a == 'add' and k in registry:
                registry[k] += registry[v] if v in registry else int(v)
            if a == 'jgz':  # damn you, 'jgz 1 3'
                try:
                    k = int(k)
                except ValueError:
                    k = registry[k] if k in registry else 0
                try:
                    v = int(v)
                except ValueError:
                    v = registry[v] if v in registry else 1
                return v if k > 0 else 1
            if a == 'mod' and k in registry:
                registry[k] %= registry[v] if v in registry else int(v)
            if a == 'mul' and k in registry:
                registry[k] *= registry[v] if v in registry else int(v)
            if a == 'set':
                registry[k] = registry[v] if v in registry else int(v)
            if swag_mode:  # Part 1: scientific wild-ass guess
                if a == 'rcv' and registry[k] != 0:
                    return self.STOP_SIGNAL
                if a == 'snd' and k in registry:
                    self.sound_freq = registry[k]
            else:  # part 2, actual instructions
                if a == 'rcv':
                    if len(self.queue[registry['_id']]) == 0:
                        return 0
                    registry[k] = self.queue[registry['_id']].pop(0)
                if a == 'snd':
                    self.sent[registry['_id']] += 1
                    q = (registry['_id'] + 1) % 2
                    kk = registry[k] if k in registry else int(k)
                    self.queue[q].append(kk)
        return 1

    def solve(self, puzzle_input):
        lines = puzzle_input.splitlines()
        stop = len(lines)
        self.STOP_SIGNAL = stop
        i = 0
        registry = {}
        while i < stop:
            i += self._run(lines[i], registry)
        return self.sound_freq

    def solve_again(self, puzzle_input):
        registry = {'p': 0, '_id': 0}, {'p': 1, '_id': 1}
        lines = puzzle_input.splitlines()
        i = 0
        j = 0
        p0_queue = True
        p1_queue = False
        while p1_queue or p0_queue:
            while p0_queue:
                x = self._run(lines[i], registry[0], swag_mode=False)
                if x == 0:
                    p0_queue = False
                else:
                    i += x
            p1_queue = len(self.queue[1]) > 0
            while p1_queue:
                x = self._run(lines[j], registry[1], swag_mode=False)
                if x == 0:
                    p1_queue = False
                else:
                    j += x
            p0_queue = len(self.queue[0]) > 0
        return self.sent[1]


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
