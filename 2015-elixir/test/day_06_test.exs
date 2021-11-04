defmodule Day06Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day06
  import Aoc.Solution.Day06

  test "parses the input" do
    input = """
    turn off 674,321 through 793,388
    toggle 749,672 through 973,965
    turn on 943,30 through 990,907
    """ |> String.trim()

    expected = [
      {"off", 674..793, 321..388},
      {"toggle", 749..973, 672..965},
      {"on", 943..990, 30..907},
    ]

    assert parse!(input) == expected
  end

  test "solves first part" do
    input = """
    turn on 0,0 through 999,999
    toggle 0,0 through 999,0
    turn off 499,499 through 500,500
    """ |> String.trim()

    a = input |> parse!() |> solve_first_part()

    assert a == 998996
  end

  test "solves second part" do
    input = """
    turn on 0,0 through 999,999
    toggle 0,0 through 999,0
    turn off 499,499 through 500,500
    """ |> String.trim()

    a = input |> parse!() |> solve_second_part()

    assert a == 1000000 + 2000 - 4
  end
end
