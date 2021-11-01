import time
from datetime import timedelta


class BaseSolution:
    puzzle_input = ""
    input_file = None
    trim_input = True

    def parse_input(self, filename):
        filepath = './inputs/{}'.format(filename)
        with open(filepath, 'r') as f:
            self.puzzle_input = f.read()
            if self.trim_input:
                self.puzzle_input = self.puzzle_input.strip()

    def show_results(self):
        self.parse_input(self.input_file)
        start_time = time.monotonic()
        p1 = self.solve(self.puzzle_input)
        p2 = self.solve_again(self.puzzle_input)
        end_time = time.monotonic()
        duration = timedelta(seconds=end_time - start_time)
        print('\n\n{}\n{}\n\nPart 1: {}\nPart 2: {}\n\nDuration: {}'.format(
            str(self),
            '-' * len(str(self)),
            p1,
            p2,
            duration,
        ))

    def solve(self, puzzle_input):
        raise NotImplemented

    def solve_again(self, puzzle_input):
        raise NotImplemented
