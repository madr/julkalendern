defmodule Day01Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day01
  import Aoc.Solution.Day01

  @input ~s(
    1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
  )

  test "01: Calorie Counting, part 1" do
    expected = 24000

    result = @input |> parse!() |> solve()

    assert result == expected
  end

  test "01: Calorie Counting, part 2" do
    expected = 45000

    result = @input |> parse!() |> solve_again()

    assert result == expected
  end
end
