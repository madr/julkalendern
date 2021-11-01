defmodule Aoc.Solution.Day01 do
  @name "Day 1: Day 1: Report Repair"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def parse!(raw) do
    raw |> String.split() |> Enum.map(&String.to_integer/1)
  end

  @impl Solution
  def solve_first_part(input) do
    {x, y} = input |> permutations(2) |> find_combination

    x * y
  end

  @impl Solution
  def solve_second_part(input) do
    {x, y, z} = input |> permutations(3) |> find_combination

    x * y * z
  end

  defp find_combination([[x, y] | queue]) do
    case x + y do
      2020 -> {x, y}
      _ -> find_combination(queue)
    end
  end

  defp find_combination([[x, y, z] | queue]) do
    case x + y + z do
      2020 -> {x, y, z}
      _ -> find_combination(queue)
    end
  end

  # found at: https://stackoverflow.com/questions/33756396/how-can-i-get-permutations-of-a-list
  def permutations(_chars, building, 0) do
    [building]
  end

  def permutations(values, building, num) do
    Stream.map(values, fn v -> building ++ [v] end)
    |> Enum.flat_map(fn building -> permutations(values, building, num - 1) end)
  end

  def permutations(values, num), do: permutations(values, [], num)
end
