defmodule Day01Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day01
  import Aoc.Solution.Day01

  test "parses the input" do
    input = """
    1721
    979
    """

    expected = [1721, 979]

    assert parse!(input) == expected
  end

  test "solves first part" do
    input = """
    1721
    979
    366
    299
    675
    1456
    """

    a = input |> parse!() |> solve_first_part()

    assert a == 514_579
  end

  @tag :skip
  test "solves second part" do
    input = """
    1721
    979
    366
    299
    675
    1456
    """

    a = input |> parse!() |> solve_second_part()

    assert a == 130_933_530
  end
end
