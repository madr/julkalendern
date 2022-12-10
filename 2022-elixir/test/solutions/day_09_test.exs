defmodule Day09Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day09
  import Aoc.Solution.Day09

  @input ~s(
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
  )

  @tag :skip
  test "09: Rope Bridge, part 1" do
    expected = 13

    result = @input |> parse!() |> solve()

    assert result == expected
  end

  # test "09: Rope Bridge, part 2" do
  #   expected = :something

  #   result = @input |> parse!() |> solve_again()

  #   assert result == expected
  # end
end
