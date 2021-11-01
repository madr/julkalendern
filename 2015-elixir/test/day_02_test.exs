defmodule Day02Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day02
  import Aoc.Solution.Day02

  test "parses the input" do
    input = """
    2x3x4
    1x1x10
    """

    assert parse!(input) == [
             [2, 3, 4],
             [1, 1, 10]
           ]
  end

  test "solves first part" do
    a = "2x3x4" |> parse!() |> solve_first_part()
    b = "1x1x10" |> parse!() |> solve_first_part()

    assert a == 58
    assert b == 43
  end

  test "solves first part using multiple packages" do
    a = "2x3x4\n1x1x10" |> parse!() |> solve_first_part()

    assert a == 58 + 43
  end

  test "solves second part" do
    a = "2x3x4" |> parse!() |> solve_second_part()
    b = "1x1x10" |> parse!() |> solve_second_part()

    assert a == 34
    assert b == 14
  end

  test "solves second part using multiple packages" do
    a = "2x3x4\n1x1x10" |> parse!() |> solve_second_part()

    assert a == 34 + 14
  end
end
