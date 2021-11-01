defmodule Day04Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day04
  import Aoc.Solution.Day04

  test "parses the input" do
    i = "\n  ab  \n"
    expected = "ab"

    assert parse!(i) == expected
  end

  test "solves first part" do
    a = "abcdef" |> parse!() |> solve_first_part()
    b = "pqrstuv" |> parse!() |> solve_first_part()

    assert a == 609_043
    assert b == 1_048_970
  end
end
