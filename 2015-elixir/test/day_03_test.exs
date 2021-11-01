defmodule Day03Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day03
  import Aoc.Solution.Day03

  test "parses the input" do
    expected = ["<", ">"]

    assert parse!("<>") == expected
  end

  test "solves first part" do
    a = ">" |> parse!() |> solve_first_part()
    b = "^>v<" |> parse!() |> solve_first_part()
    c = "^v^v^v^v^v" |> parse!() |> solve_first_part()

    assert a == 2
    assert b == 4
    assert c == 2
  end

  test "solves second part" do
    a = "^v" |> parse!() |> solve_second_part()
    b = "^>v<" |> parse!() |> solve_second_part()
    c = "^v^v^v^v^v" |> parse!() |> solve_second_part()

    assert a == 3
    assert b == 3
    assert c == 11
  end
end
