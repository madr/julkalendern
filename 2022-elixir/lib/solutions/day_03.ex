defmodule Aoc.Solution.Day03 do
  import Aoc.Utils

  @name "Day 3: Rucksack Reorganization"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def present(solution), do: "Sum of priorities is #{solution}"

  @impl Solution
  def present_again(solution), do: "Sum of the unauthenticated priorities are #{solution}"

  @impl Solution
  def parse!(raw) do
    raw
    |> split_lines()
  end

  @impl Solution
  def solve(rucksacks) do
    rucksacks
    |> Enum.map(&compartment_pair/1)
    |> Enum.map(&calculate_compartment_priorities/1)
    |> Enum.sum()
  end

  @impl Solution
  def solve_again(rucksacks) do
    rucksacks
    |> Enum.chunk_every(3)
    |> Enum.map(&calculate_compartment_priorities/1)
    |> Enum.sum()
  end

  def compartment_pair(line) do
    half = line |> String.length() |> div(2)
    String.split_at(line, half)
  end

  def calculate_compartment_priorities(compartments) when is_tuple(compartments) do
    [a, b] =
      compartments
      |> Tuple.to_list()
      |> Enum.map(&distinct/1)

    common_priority(a, b)
  end

  def calculate_compartment_priorities(compartments) do
    [a, b, c] =
      compartments
      |> Enum.map(&distinct/1)

    common_priority(a, b, c)
  end

  def distinct(line) do
    line |> String.codepoints() |> MapSet.new()
  end

  def priority(char) when is_binary(char), do: char |> String.to_charlist() |> hd |> priority
  def priority(n) when n > 96, do: n - 96
  def priority(n), do: n - 38

  def common_priority(a, b, c) do
    MapSet.intersection(a, b)
    |> MapSet.intersection(c)
    |> MapSet.to_list()
    |> List.first()
    |> priority
  end

  def common_priority(a, b) do
    MapSet.intersection(a, b)
    |> MapSet.to_list()
    |> List.first()
    |> priority
  end
end
