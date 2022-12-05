defmodule Day05Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day05
  import Aoc.Solution.Day05

  @input ~s(
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
)

  test "05: Supply Stacks, part 1" do
    expected = "CMZ"

    result = @input |> parse!() |> solve()

    assert result == expected
  end

  test "05: Supply Stacks, part 2" do
    expected = "MCD"

    result = @input |> parse!() |> solve_again()

    assert result == expected
  end
end
