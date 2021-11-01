defmodule Day02Test do
  use ExUnit.Case
  doctest Day02

  setup do
    puzzle_input = [
      'abcdef',
      'bababc',
      'abbcde',
      'abcccd',
      'aabcdd',
      'abcdee',
      'ababab'
    ]
    |> Enum.join("\n")
    {:ok, puzzle_input: puzzle_input }
  end

  test "box id checksum", meta do
    puzzle_input = [
      "abcdef",
      "bababc",
      "abbcde",
      "abcccd",
      "aabcdd",
      "abcdee",
      "ababab"
    ]
    assert Day02.countn(puzzle_input, 2) == 3
    assert Day02.countn(puzzle_input, 3) == 4
    #assert Day02.solve(puzzle_input) == 12
  end

  test "finds recurring frequency", meta do
    puzzle_input = meta[:puzzle_input]
    #assert Day02.solve_again(puzzle_input) == "fgij"
  end
end
