defmodule Aoc.Solution.Day03 do
  @name "Perfectly Spherical Houses in a Vacuum"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def parse!(raw) do
    String.split(raw, "", trim: true)
  end

  @impl Solution
  def solve_first_part(input) do
    input |> deliver() |> MapSet.size()
  end

  @impl Solution
  def solve_second_part(input) do
    santa = Enum.take_every(input, 2) |> deliver()

    robosanta =
      input
      |> Enum.with_index()
      |> Enum.reject(fn {_k, v} -> rem(v, 2) == 0 end)
      |> Enum.map(fn {k, _v} -> k end)
      |> deliver()

    MapSet.union(santa, robosanta) |> MapSet.size()
  end

  defp move("<", {x, y}), do: {x - 1, y}

  defp move(">", {x, y}), do: {x + 1, y}

  defp move("v", {x, y}), do: {x, y + 1}

  defp move("^", {x, y}), do: {x, y - 1}

  defp deliver(input) do
    {_, seen} =
      input
      |> Enum.reduce(
        {{0, 0}, MapSet.new([{0, 0}])},
        fn d, {pos, seen} ->
          next = move(d, pos)
          {next, MapSet.put(seen, next)}
        end
      )

    seen
  end
end
