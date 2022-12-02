defmodule Day02Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day02
  import Aoc.Solution.Day02

  @input ~s(
    A Y
    B X
    C Z
  )

  test "02: Rock Paper Scissors, part 1" do
    expected = 15

    result = @input |> parse!() |> solve()

    assert result == expected
  end

  test "02: Rock Paper Scissors, part 2" do
    expected = 12

    result = @input |> parse!() |> solve_again()

    assert result == expected
  end
end
