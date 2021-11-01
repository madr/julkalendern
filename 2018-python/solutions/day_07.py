import itertools

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '07.in'
    def __str__(self):
        return 'Day 07: The Sum of Its Parts'

    def solve(self, puzzle_input):
        steps = [tuple(filter(lambda x: len(x) == 1, l.split())) for l in puzzle_input.splitlines()]
        relations = self._get_relations(steps)
        completed_steps = self._get_completed_steps(relations)
        return completed_steps

    def solve_again(self, puzzle_input):
        return self.solve_with_workers(puzzle_input)

    def solve_with_workers(self, puzzle_input, workers=5, completion_reducer=0):
        steps = [tuple(filter(lambda x: len(x) == 1, l.split())) for l in puzzle_input.splitlines()]
        relations = self._get_relations(steps)
        return self.get_seconds(relations, workers, completion_reducer)

    def _get_completed_steps(self, relations):
        stop_at = len(relations.keys())
        completed_steps = ''
        while len(completed_steps) < stop_at:
            available = sorted([child for child, parents in relations.items()
                               if (all(prnt in completed_steps for prnt in parents) or len(parents) == 0) and child not in completed_steps])
            completed = available[0]
            completed_steps += completed
        return completed_steps

    def _get_relations(self, steps):
        deps = dict([(p, set()) for p in itertools.chain(dict(steps).keys(), dict(steps).values())])
        for parent, child in steps:
            deps[child].add(parent)
        return deps

    def get_seconds(self, relations, workers_count=5, completion_reduce=0):
        workers = [dict() for _ in range(workers_count)]
        stop_at = len(relations)
        seconds = 0
        completed = 0
        completed_steps = ''
        in_progress = set()
        diff = ord('A')
        while completed < stop_at:
            available_steps = sorted([child for child, parents in relations.items()
                                      if (all(prnt in completed_steps for prnt in parents) or len(parents) == 0) and
                                      child not in completed_steps])
            available_steps = [s for s in available_steps if s not in in_progress and s not in completed_steps]
            available_workers = [i for i, w in enumerate(workers) if not w]
            while available_steps and available_workers:
                avs = available_steps.pop(0)
                avw = available_workers.pop(0)
                in_progress.add(avs)
                workers[avw][avs] = 0
            busy_workers = [i for i, w in enumerate(workers) if w]
            for ip, bw in itertools.product(in_progress, busy_workers):
                if ip in workers[bw]:
                    # Apply completion_reduce (60) here since A takes 61 seconds to complete,
                    # B 62 times to complete, etc in THE REAL WORLD, but in the example it was "simplified".
                    #
                    # > To simplify things for the example, however, suppose you only have help from one Elf (a total
                    # > of two workers) and that each step takes **60 fewer seconds** (so that step A takes 1 second and
                    # > step Z takes 26 seconds).
                    #
                    # Die in a fire, would you kindly.
                    if workers[bw][ip] == 60 - completion_reduce + ord(ip) - diff:
                        completed_steps += ip
                        in_progress.remove(ip)
                        del workers[bw][ip]
                        completed += 1
                    else:
                        workers[bw][ip] += 1
            seconds += 1
        return seconds


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
