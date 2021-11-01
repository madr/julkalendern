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
        print('\n\n{}\n{}\n\nPart 1: {}\nPart 2: {}'.format(
            str(self),
            '-' * len(str(self)),
            self.solve(self.puzzle_input),
            self.solve_again(self.puzzle_input),
        ))

    def solve(self, puzzle_input):
        raise NotImplemented

    def solve_again(self, puzzle_input):
        raise NotImplemented
