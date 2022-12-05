defmodule Day04Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day04
  import Aoc.Solution.Day04

  @input ~s(
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
  )

  test "04: Camp Cleanup, part 1" do
    expected = 2

    result = @input |> parse!() |> solve()

    assert result == expected
  end

  test "04: Camp Cleanup, part 2" do
    expected = 4

    result = @input |> parse!() |> solve_again()

    assert result == expected
  end
end
