defmodule Aoc.Solution.Day02 do
  @name "I Was Told There Would Be No Math"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def parse!(raw) do
    raw
    |> String.split()
    |> Enum.map(fn p -> p |> String.split("x") |> Enum.map(&String.to_integer/1) end)
  end

  @impl Solution
  def solve_first_part(input) do
    input
    |> Enum.map(fn p -> area(p) end)
    |> Enum.sum()
  end

  @impl Solution
  def solve_second_part(input) do
    input
    |> Enum.map(fn p -> ribbon(p) end)
    |> Enum.sum()
  end

  defp area(p) do
    [l, w, h] = p
    extra = Enum.min([l * w, w * h, h * l])
    2 * l * w + 2 * w * h + 2 * h * l + extra
  end

  defp ribbon(p) do
    [l, w, h] = p
    [x, y | _] = Enum.sort(p)
    ribbon = 2 * x + 2 * y
    bow = l * w * h
    bow + ribbon
  end
end
