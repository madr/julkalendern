defmodule Day07Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day07
  import Aoc.Solution.Day07

  test "parses the input" do
    expected = 10

    assert parse!("10") == expected
  end

  test "solves first part" do
    a = "something" |> parse!() |> solve_first_part()

    assert a == :something
  end

  test "solves second part" do
    a = "something" |> parse!() |> solve_second_part()

    assert a == :something
  end
end
