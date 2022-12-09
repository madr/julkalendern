defmodule Day08Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day08
  import Aoc.Solution.Day08

  @input ~s(
    30373
    25512
    65332
    33549
    35390
  )

  test "08: Treetop Tree House, part 1" do
    expected = 21

    result = @input |> parse!() |> solve()

    assert result == expected
  end

  test "08: Treetop Tree House, part 2" do
    expected = 8

    result = @input |> parse!() |> solve_again()

    assert result == expected
  end
end
