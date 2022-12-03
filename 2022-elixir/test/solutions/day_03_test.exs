defmodule Day03Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day03
  import Aoc.Solution.Day03

  @input ~s(
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
  )

  test "03: Rucksack Reorganization, part 1" do
    expected = 157

    result = @input |> parse!() |> solve()

    assert result == expected
  end

  test "03: Rucksack Reorganization, part 2" do
    expected = 70

    result = @input |> parse!() |> solve_again()

    assert result == expected
  end
end
