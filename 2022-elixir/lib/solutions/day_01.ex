defmodule Aoc.Solution.Day01 do
  @name "Day 1: Calorie Counting"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def present(solution), do: "Most carrying elf is carrying #{solution} cal worth of snacks"

  @impl Solution
  def present_again(solution),
    do: "3 most carrying elfes are carrying #{solution} cal worth of snacks"

  @impl Solution
  def parse!(raw) do
    raw
    |> Aoc.Utils.parse_values("\n\n")
    |> Enum.map(&Aoc.Utils.parse_values/1)
  end

  @impl Solution
  def solve(input) do
    input
    |> Enum.map(&sum_calories/1)
    |> Enum.max()
  end

  @impl Solution
  def solve_again(input) do
    [a, b, c | _] =
      input
      |> Enum.map(&sum_calories/1)
      |> Enum.sort()
      |> Enum.reverse()

    Enum.sum([a, b, c])
  end

  def sum_calories(rows) do
    rows
    |> Enum.map(&String.to_integer/1)
    |> Enum.sum()
  end
end
