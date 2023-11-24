from collections import defaultdict


"""
intcode computer, AoC 2019

Changelog
=========

0.3.1
-----

Patch release (day 7 part 1-2).

- Supports relative parameter mode

0.3.0
-----

Minor release (day 7 part 1-2).

BREAKING CHANGE: execute() now returns 4 values.

- now: exit code, state at halt, instruction position at halt, and captured stdout
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
__version__ = "0.3.1"


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
    state = defaultdict(int)
    for k, v in zip(range(len(program)), program):
        state[k] = v
    if noun:
        state[1] = noun
    if verb:
        state[2] = verb
    c = 0
    rb = 0
    stdout = []
    if not isinstance(stdin, list):
        stdin = [stdin]

    def halt(code):
        return code, state, n, stdout

    def values(modes, *parameters):
        for i, v in enumerate(parameters):
            if modes[i] == "0" and v < 0:
                print("================ ERROR =================")
                print("Negative index provided to position mode")
            if modes[i] == "2" and rb + v < 0:
                print("================ ERROR =================")
                print("Negative index provided to relative mode")

        def value(i, v):
            if modes[i] == "1":
                return v
            if modes[i] == "2":
                return state[v + rb]
            return state[v]

        if len(parameters) > 1:
            return [value(i, v) for i, v in enumerate(parameters)]
        return value(0, parameters[0])

    while True:
        instruction = state[n]
        # if instruction > 200 and instruction < 1000:
        # print("")
        # spn = 2 if instruction % 100 % 3 == 0 else 4
        # print(list(state.values())[n : n + spn])
        opcode = instruction % 100
        modes = str(instruction // 100).zfill(3)[::-1]
        if opcode == 1:
            a = state[n + 1]
            b = state[n + 2]
            c = n + 3
            x, y = values(modes, a, b)
            p = state[c]
            if modes[2] == "2":
                p += rb
            if debug:
                print(f"@{str(n).zfill(4)} {opcode}_ADDITION | {x} + {y} to {p})")
            state[p] = x + y
            n += 4
        if opcode == 2:
            a = state[n + 1]
            b = state[n + 2]
            c = n + 3
            x, y = values(modes, a, b)
            p = state[c]
            if modes[2] == "2":
                p += rb
            if debug:
                print(f"@{str(n).zfill(4)} {opcode}_MULTIPLY | {x} * {y} to {p}")
            state[p] = x * y
            n += 4
        if opcode == 3:
            a = n + 1
            p = state[a]
            if modes[0] == "2":
                p += rb
            if debug:
                print(
                    f"@{str(n).zfill(4)}    {opcode}_INPUT | target={p}, queued={stdin}, interactive={interactive}"
                )
            if stdin:
                state[p] = stdin.pop(0)
            else:
                if interactive:
                    state[p] = int(input("> "))
                else:
                    if debug:
                        print(f"@{str(n).zfill(4)} [suspended, awaiting input]")
                    return halt(3)
            n += 2
        if opcode == 4:
            a = state[n + 1]
            x = values(modes, a)
            stdout.append(x)
            if verbose:
                print(x)
            if debug:
                print(f"@{str(n).zfill(4)}   {opcode}_OUTPUT | echo {x}")
            n += 2
        if opcode == 5:
            a = state[n + 1]
            b = state[n + 2]
            x, y = values(modes, a, b)
            if x != 0:
                if debug:
                    print(f"@{str(n).zfill(4)} {opcode}_JMP-IF-1 | {x} != 0, n={y}")
                n = y
            else:
                if debug:
                    print(f"@{str(n).zfill(4)} {opcode}_JMP-IF-1 | {x} != 0, ignoring")
                n += 3
        if opcode == 6:
            a = state[n + 1]
            b = state[n + 2]
            x, y = values(modes, a, b)
            if x == 0:
                n = y
            else:
                n += 3
            if debug:
                print(f"{n}:{opcode} | {n}")
        if opcode == 7:
            a = state[n + 1]
            b = state[n + 2]
            c = n + 3
            x, y = values(modes, a, b)
            p = state[c]
            if modes[2] == "2":
                p += rb
            if debug:
                print(f"@{str(n).zfill(4)} {opcode}_LESSTHAN | {x} < {y} to {p}")
            state[p] = int(x < y)
            n += 4
        if opcode == 8:
            a = state[n + 1]
            b = state[n + 2]
            c = n + 3
            x, y = values(modes, a, b)
            p = state[c]
            if modes[2] == "2":
                p += rb
            if debug:
                print(f"@{str(n).zfill(4)}   {opcode}_EQUALS | {x} == {y} to {p}")
            state[p] = int(x == y)
            n += 4
        if opcode == 9:
            a = state[n + 1]
            x = values(modes, a)
            if debug:
                print(f"@{str(n).zfill(4)}  {opcode}_RELBASE | {rb} + {x}")
            rb += x
            n += 2
        if opcode == 99:
            break
        c += 1
        if debug and c % 1000 == 0:
            print(f"{c} instructions done, current pos: {n}")
        if c == 33:
            break
    if verbose:
        title = f"intcode computer received SIGTERM"
    return halt(99)
