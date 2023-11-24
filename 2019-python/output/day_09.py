from output import answer, puzzleinput
from output.intcode_computer import execute, parse

n = 9
title = "Sensor Boost"


@puzzleinput(n)
def parse_input(data):
    return parse(data)


@answer(1, "[intcode 0.3.1] BOOST keycode: {}")
def part_1(program):
    _c, _s, _n, outputs = execute(program, stdin=[1])
    return outputs.pop(0)


@answer(2, "[intcode 0.3.1] Distress signal coordinates: {}")
def part_2(program):
    _c, _s, _n, outputs = execute(program, stdin=[2])
    return outputs.pop(0)


if __name__ == "__main__":
    assert execute(
        [
            109,
            1,
            204,
            -1,
            1001,
            100,
            1,
            100,
            1008,
            100,
            16,
            101,
            1006,
            101,
            0,
            99,
        ]
    )[3] == [
        109,
        1,
        204,
        -1,
        1001,
        100,
        1,
        100,
        1008,
        100,
        16,
        101,
        1006,
        101,
        0,
        99,
    ]
    assert len(str(execute([1102, 34915192, 34915192, 7, 4, 7, 99, 0])[3][0])) == 16
    assert 1125899906842624 in execute([104, 1125899906842624, 99])[3]
    assert execute([109, -1, 4, 1, 99])[3][0] == -1
    assert execute([109, -1, 104, 1, 99])[3][0] == 1
    assert execute([109, -1, 204, 1, 99])[3][0] == 109
    assert execute([109, 1, 9, 2, 204, -6, 99])[3][0] == 204
    assert execute([109, 1, 109, 9, 204, -6, 99])[3][0] == 204
    assert execute([109, 1, 209, -1, 204, -106, 99])[3][0] == 204
    assert execute([109, 1, 3, 3, 204, 2, 99], stdin=[666])[3][0] == 666
    assert execute([109, 1, 203, 2, 204, 2, 99], stdin=[666])[3][0] == 666
    assert execute([109, 6, 21001, 9, 25, 1, 104, 0, 99, 49])[3][0] == 74

    parsed = parse_input()
    assert execute(parsed, stdin=[1])[3][0] == 2351176124

    part_1(parsed)
    part_2(parsed)
