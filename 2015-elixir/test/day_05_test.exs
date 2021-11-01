defmodule Day05Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day05
  import Aoc.Solution.Day05

  test "parses the input" do
    input = """
    a
    b
    c
    """

    expected = ["a", "b", "c"]

    assert parse!(input) == expected
  end

  test "solves first part" do
    a = "ugknbfddgicrmopn" |> parse!() |> solve_first_part()
    b = "aaa" |> parse!() |> solve_first_part()
    c = "jchzalrnumimnmhp" |> parse!() |> solve_first_part()
    d = "haegwjzuvuyypxyu" |> parse!() |> solve_first_part()
    e = "dvszwmarrgswjxmb" |> parse!() |> solve_first_part()

    assert a == 1
    assert b == 1
    assert c == 0
    assert d == 0
    assert e == 0
  end

  test "solves second part" do
    a = "qjhvhtzxzqqjkmpb" |> parse!() |> solve_second_part()
    b = "xxyxx" |> parse!() |> solve_second_part()
    c = "uurcxstgmygtbstg" |> parse!() |> solve_second_part()
    d = "ieodomkazucvgmuy" |> parse!() |> solve_second_part()

    assert a == 1
    assert b == 1
    assert c == 0
    assert d == 0
  end
end
