from collections import defaultdict


"""
intcode computer, AoC 2019

Changelog
=========

0.3.0
-----

Minor release (day 7 part 1-2).

BREAKING CHANGE: execute() now returns 4 values.
- now: exit code, state at halt, instruction position at halt, and captured stdout.
- before: final state, and captured stdout

Changes:

- Add support for a sequence of stdins
- Add interactive param to ask for manual (interactive) input on input opcode
- Add verbose param to show more output in interactive input mode
- Will now halt with code 3 (input) when input is required, stdin is empty and interactive input mode is not enabled

0.2.1
-----

Patch release (day 5 part 2).

- Add operation 5: set instruction pointer to value at parameter 2 position, based on value at parameter 1 position
- Add operation 6: set instruction pointer to value at parameter 2 position, based on value at parameter 1 position
- Add operation 7: compares values in parameter 1 position and parameter 2 position, stores at parameter 3 position
- Add operation 8: compares values in parameter 1 position and parameter 2 position, stores at parameter 3 position

0.2.0
-----

Minor release (day 5 part 1).

- Support immediate parameter mode
- Add stdin argument
- Make arguments optional: noun, verb
- Capture and return stdout
- Add operation 3: store stdin to parameter 1 position
- Add operation 4: output value at parameter 1 position to stdout

0.1.1
-----

Patch release (day 2 part 2).

- Remove initial modification 1=12, 2=2
- Add noun argument, stored at pos 1 (default value: 12)
- Add verb argument, stored at pos 2 (default value: 2)

0.1.0
-----

Initial version (day 2 part 1).

- Support positional parameter mode
- Add operation 1: adds parameter 1 to parameter 2, store to parameter 3 position
- Add operation 2: multiply parameter 1 with parameter 2, store to parameter 3 position
"""
v = "0.2.3"


def parse(data):
    return list(map(int, data.split(",")))


def execute(
    program,
    noun=None,
    verb=None,
    stdin=[],
    debug=False,
    interactive=False,
    verbose=False,
    n=0,
):
    if verbose:
        title = f"intcode computer, version {v}"
        print("".join("=" for _ in title))
        print(title)
        print("".join("=" for _ in title))
    state = dict(zip(range(len(program)), program))
    if noun:
        state[1] = noun
    if verb:
        state[2] = verb
    c = 0
    stdout = []
    if not isinstance(stdin, list):
        stdin = [stdin]

    while True:
        instruction = state[n]
        opcode = instruction % 100
        modes = str(instruction // 100 % 100).zfill(2)
        if opcode == 1:
            a = state[n + 1]
            b = state[n + 2]
            p = state[n + 3]
            x = a if modes[1] == "1" else state[a]
            y = b if modes[0] == "1" else state[b]
            state[p] = x + y
            n += 4
            if debug:
                print(f"{n}:{opcode} | {x} + {y} to {p}")
        if opcode == 2:
            a = state[n + 1]
            b = state[n + 2]
            p = state[n + 3]
            x = a if modes[1] == "1" else state[a]
            y = b if modes[0] == "1" else state[b]
            state[p] = x * y
            n += 4
            if debug:
                print(f"{n}:{opcode} | {x} * {y} to {p}")
        if opcode == 3:
            p = state[n + 1]
            if stdin:
                state[p] = stdin.pop(0)
            else:
                if interactive:
                    state[p] = int(input("> "))
                else:
                    return 3, state, n, stdout
            n += 2
            if debug:
                print(f"{n}:{opcode} | {i} to {p}")
        if opcode == 4:
            a = state[n + 1]
            x = a if modes[1] == "1" else state[a]
            n += 2
            stdout.append(x)
            if verbose:
                print(x)
            if debug:
                print(f"{n}:{opcode} | {stdout}")
        if opcode == 5:
            a = state[n + 1]
            b = state[n + 2]
            x = a if modes[1] == "1" else state[a]
            y = b if modes[0] == "1" else state[b]
            if x != 0:
                n = y
            else:
                n += 3
            if debug:
                print(f"{n}:{opcode} | {n}")
        if opcode == 6:
            a = state[n + 1]
            b = state[n + 2]
            x = a if modes[1] == "1" else state[a]
            y = b if modes[0] == "1" else state[b]
            if x == 0:
                n = y
            else:
                n += 3
            if debug:
                print(f"{n}:{opcode} | {n}")
        if opcode == 7:
            a = state[n + 1]
            b = state[n + 2]
            p = state[n + 3]
            x = a if modes[1] == "1" else state[a]
            y = b if modes[0] == "1" else state[b]
            state[p] = int(x < y)
            n += 4
            if debug:
                print(f"{n}:{opcode} | {x}")
        if opcode == 8:
            a = state[n + 1]
            b = state[n + 2]
            p = state[n + 3]
            x = a if modes[1] == "1" else state[a]
            y = b if modes[0] == "1" else state[b]
            state[p] = int(x == y)
            n += 4
            if debug:
                print(f"{n}:{opcode} | {x}")
        if opcode == 99:
            break
        c += 1
        if debug and c % 1000 == 0:
            print(f"{c} instructions done, current pos: {n}")
        # if c == 3:
        #     break
    if verbose:
        title = f"intcode computer received SIGTERM"
    return 99, state, n, stdout
