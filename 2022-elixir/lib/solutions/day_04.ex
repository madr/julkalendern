defmodule Aoc.Solution.Day04 do
  import Aoc.Utils

  @name "Day 4: Camp Cleanup"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def present(solution), do: "#{solution} assignment pairs overlap"

  @impl Solution
  def present_again(solution), do: "Solution is #{solution}"

  @impl Solution
  def parse!(raw) do
    raw
    |> split_lines()
    |> Enum.map(fn l -> parse_values(l, ",") end)
  end

  @impl Solution
  def solve(pairs) do
    pairs
    |> ranges()
    |> overlaps()
    |> Enum.count()
  end

  @impl Solution
  def solve_again(pairs) do
    pairs
    |> ranges()
    |> strict_overlaps()
    |> Enum.count()
  end

  def ranges(rows) when length(rows) > 2 do
    Enum.map(rows, &ranges/1)
  end

  def ranges(pairs) do
    Enum.map(pairs, fn p ->
      [start, stop] = parse_values(p, "-") |> Enum.map(&String.to_integer/1)
      MapSet.new(start..stop)
    end)
  end

  def overlaps(ranges), do: Enum.filter(ranges, &overlap?/1)

  def overlap?([a, b]), do: MapSet.subset?(a, b) or MapSet.subset?(b, a)

  def strict_overlaps(ranges), do: Enum.filter(ranges, &strict_overlap?/1)

  def strict_overlap?([a, b]), do: MapSet.intersection(a, b) |> Enum.count() > 0
end
