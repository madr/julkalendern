defmodule Aoc19.Solution.Day06 do
  @name "Day 6: Universal Orbit Map"
  @behaviour Solution
  @you "YOU"
  @santa "SAN"

  @impl Solution
  def get_name, do: @name

  @impl Solution
  @doc """
  Parse raw input into a list of strings.

  ## Examples

      iex> Aoc19.Solution.Day06.parse!(\"\"\"
      ...> X)5
      ...> Y)13
      ...> ZW)1
      ...> \"\"\")
      [["X", "5"], ["Y", "13"], ["ZW", "1"]]

  """
  def parse!(raw) do
    raw
    |> String.split()
    |> Enum.map(fn s -> String.split(s, ")") end)
  end

  @impl Solution
  @doc """
  Solution for the first part of "Day 6: Universal Orbit Map".

  ## Examples

      iex> \"\"\"
      ...> COM)B
      ...> B)C
      ...> C)D
      ...> D)E
      ...> E)F
      ...> B)G
      ...> G)H
      ...> D)I
      ...> E)J
      ...> J)K
      ...> K)L
      ...> \"\"\" |> Aoc19.Solution.Day06.parse!() |> Aoc19.Solution.Day06.solve_first_part()
      42

  """
  def solve_first_part(input) do
    input
    |> orbit_tree
    |> Map.values()
    |> Enum.map(fn l -> length(l) end)
    |> Enum.sum()
  end

  @impl Solution
  @doc """
  Solution for the second part of "Day 6: Universal Orbit Map".

  ## Examples

      iex> \"\"\"
      ...> COM)B
      ...> B)C
      ...> C)D
      ...> D)E
      ...> E)F
      ...> B)G
      ...> G)H
      ...> D)I
      ...> E)J
      ...> J)K
      ...> K)L
      ...> K)YOU
      ...> I)SAN
      ...> \"\"\" |> Aoc19.Solution.Day06.parse!() |> Aoc19.Solution.Day06.solve_second_part()
      4
  """
  def solve_second_part(input) do
    santa = parent_branch(input, @santa)
    you = parent_branch(input, @you)

    common = MapSet.intersection(MapSet.new(santa), MapSet.new(you)) |> Enum.to_list()

    nearest(common, you) + nearest(common, santa)
  end

  def orbit_tree(input) do
    orbits =
      input |> Enum.reduce(%{}, fn [parent, child], acc -> children(acc, parent, child) end)

    orbits
    |> Map.keys()
    |> Enum.reduce(orbits, fn k, acc -> Map.get(acc, k, []) |> grandchildren(acc, k) end)
  end

  @doc """
  Add grandchildren to branch if parent is present.

  ## Examples

      iex> Aoc19.Solution.Day06.children(%{a: [3, 2]}, :a, 5)
      %{a: [5, 3, 2]}

  """
  def children(acc, parent, child) do
    if Map.has_key?(acc, parent) do
      Map.put(acc, parent, [child | Map.get(acc, parent, child)])
    else
      Map.put(acc, parent, [child])
    end
  end

  @doc """
  Add all grandchildren to the orbit tree.

  ## Examples

      iex> Aoc19.Solution.Day06.grandchildren([5, 6], %{a: [3, 2], b: [5]}, 2)
      %{a: [3, 2, 5, 6], b: [5]}

  """
  def grandchildren(children, orbits, parent) do
    values =
      orbits
      |> Map.values()
      |> Enum.map(fn grandchildren -> append_grandchildren(grandchildren, parent, children) end)

    keys = Map.keys(orbits)

    Enum.zip(keys, values)
    |> Map.new()
  end

  @doc """
  add grandchildren to existing branch in orbit tree.

  ## Examples

      iex> Aoc19.Solution.Day06.append_grandchildren([0, 1, 2], 1, [3, 4])
      [0, 1, 2, 3, 4]

  """
  def append_grandchildren(children, parent, grandchildren) do
    if Enum.member?(children, parent) do
      [children | grandchildren] |> List.flatten()
    else
      children
    end
  end

  @doc """
  Add all grandchildren to the orbit tree.

  ## Examples

      iex> Aoc19.Solution.Day06.parent_branch([
      ...> ["13", "3"],
      ...> ["1", "7"],
      ...> ["7", "13"]
      ...> ], "13")
      ["1", "7"]

      iex> Aoc19.Solution.Day06.parent_branch([
      ...> ["13", "3"],
      ...> ["1", "7"],
      ...> ["7", "13"]
      ...> ], "7")
      ["1"]

      iex> Aoc19.Solution.Day06.parent_branch([
      ...> ["13", "3"],
      ...> ["1", "7"],
      ...> ["7", "13"]
      ...> ], "3")
      ["1", "7", "13"]

  """
  def parent_branch(orbits, subject, seen) do
    case Enum.filter(orbits, fn [_parent, child] -> child == subject end) do
      [] -> seen |> List.delete_at(-1)
      [[parent, _child]] -> parent_branch(orbits, parent, [parent | seen])
    end
  end

  def parent_branch(orbits, subject) do
    parent_branch(orbits, subject, [subject])
  end

  @doc """
  Find nearest parent in branch from a set of positions.

  ## Examples

      iex> Aoc19.Solution.Day06.nearest(["1", "2"], ["0", "1", "2", "3", "4"])
      2

  """
  def nearest(positions, branch) do
    len = length(branch)

    positions
    |> Enum.map(fn p -> len - Enum.find_index(branch, fn x -> x == p end) - 1 end)
    |> Enum.min()
  end
end
