defmodule Day01Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day01
  import Aoc.Solution.Day01

  test "parses the input" do
    expected = ["(", "(", ")", ")"]

    result = parse!("(())")

    assert result == expected
  end

  test "solves first part" do
    a = "(())" |> parse!() |> solve_first_part()
    b = "()()" |> parse!() |> solve_first_part()
    c = "(((" |> parse!() |> solve_first_part()
    d = "(()(()(" |> parse!() |> solve_first_part()
    e = "))(((((" |> parse!() |> solve_first_part()
    f = "())" |> parse!() |> solve_first_part()
    g = "))(" |> parse!() |> solve_first_part()
    h = ")))" |> parse!() |> solve_first_part()
    i = ")())())" |> parse!() |> solve_first_part()

    assert a == 0
    assert b == 0
    assert c == 3
    assert d == 3
    assert e == 3
    assert f == -1
    assert g == -1
    assert h == -3
    assert i == -3
  end

  test "solves second part" do
    a = ")" |> parse!() |> solve_second_part()
    b = "()())" |> parse!() |> solve_second_part()
    c = "()())()" |> parse!() |> solve_second_part()

    assert a == 1
    assert b == 5
    assert c == 5
  end

  test "solves second part with examples of no-last chars" do
    a = "()())()" |> parse!() |> solve_second_part()

    assert a == 5
  end
end
