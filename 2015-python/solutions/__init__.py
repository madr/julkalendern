class BaseSolution:
    input_file = None
    trim_input = True

    def read_input(self, filename):
        filepath = "./inputs/{}".format(filename)
        with open(filepath, "r") as f:
            data = f.read()
            if self.trim_input:
                return data.strip()
            return data

    def show_results(self):
        data = self.read_input(self.input_file)
        puzzle_input = self.parse_input(data)
        print(
            "\n\n{}\n{}\n\nPart 1: {}\nPart 2: {}".format(
                str(self),
                "-" * len(str(self)),
                self.solve(puzzle_input),
                self.solve_again(puzzle_input),
            )
        )

    def solve(self, puzzle_input):
        raise NotImplemented

    def solve_again(self, puzzle_input):
        raise NotImplemented

    def parse_input(self, data):
        raise NotImplemented
