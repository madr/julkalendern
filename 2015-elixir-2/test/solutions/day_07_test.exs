defmodule Day07Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day07
  import Aoc.Solution.Day07

  @input ~s(
    123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
  )

  test "07: Some Assembly Required, part 1" do
    expected = %{
      "d" => 72,
      "e" => 507,
      "f" => 492,
      "g" => 114,
      "h" => 65412,
      "i" => 65079,
      "x" => 123,
      "y" => 456
    }

    result = @input |> parse!() |> solve("d")

    assert result == Map.get(expected, "d")
  end
end
