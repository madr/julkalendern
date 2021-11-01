defmodule Aoc19.Solution.Day03 do
  @name "Day 3: Crossed Wires"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  @doc """
  Parse raw input into a list of paths.

  ## Examples

      iex> Aoc19.Solution.Day03.parse!("U3,R7\\nD11,L13")
      [["U3", "R7"], ["D11", "L13"]]

  """
  def parse!(raw) do
    raw
    |> String.split()
    |> Enum.map(fn s -> String.split(s, ",") end)
  end

  @impl Solution
  @doc """
  Solution for the first part of "Day 3: Crossed Wires".

  ## Examples

      iex> Aoc19.Solution.Day03.solve_first_part("R8,U5,L5,D3\\nU7,R6,D4,L4" |> Aoc19.Solution.Day03.parse!)
      6

      iex> Aoc19.Solution.Day03.solve_first_part("R75,D30,R83,U83,L12,D49,R71,U7,L72\\nU62,R66,U55,R34,D71,R55,D58,R83" |> Aoc19.Solution.Day03.parse!)
      159

      iex> Aoc19.Solution.Day03.solve_first_part("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7" |> Aoc19.Solution.Day03.parse!)
      135

  """
  def solve_first_part(input) do
    [a, b] =
      input
      |> Enum.map(&get_wire/1)
      |> Enum.map(&MapSet.new/1)

    MapSet.intersection(a, b)
    |> Enum.map(&manhattan_distance/1)
    |> Enum.min()
  end

  @impl Solution
  @doc """
  Solution for the second part of "Day 3: Crossed Wires".

  ## Examples

      iex> Aoc19.Solution.Day03.solve_second_part("R8,U5,L5,D3\\nU7,R6,D4,L4" |> Aoc19.Solution.Day03.parse!)
      30

      iex> Aoc19.Solution.Day03.solve_second_part("R75,D30,R83,U83,L12,D49,R71,U7,L72\\nU62,R66,U55,R34,D71,R55,D58,R83" |> Aoc19.Solution.Day03.parse!)
      610

      iex> Aoc19.Solution.Day03.solve_second_part("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7" |> Aoc19.Solution.Day03.parse!)
      410

  """
  def solve_second_part(input) do
    wires =
      input
      |> Enum.map(&get_wire/1)

    ab = wires |> Enum.map(&Enum.count/1) |> Enum.sum()
    [a, b] = wires

    MapSet.intersection(MapSet.new(a), MapSet.new(b))
    |> Enum.map(fn pos ->
      {Enum.find_index(a, fn x -> x == pos end), Enum.find_index(b, fn x -> x == pos end)}
    end)
    |> Enum.map(fn {x, y} ->
      ab - x - y
    end)
    |> Enum.min()
  end

  @doc """
  Return a changeset (a tuple of x and y additions) for a defined direction.
  """
  def direction("U"), do: {1, 0}
  def direction("R"), do: {0, 1}
  def direction("D"), do: {-1, 0}
  def direction("L"), do: {0, -1}

  @doc """
  Get a wire's complete spread (in steps) from a list of directions.

  ## Examples

      iex> Aoc19.Solution.Day03.get_wire(["U7", "R6", "D4", "L4"])
      [{3, 2}, {3, 3}, {3, 4}, {3, 5}, {3, 6}, {4, 6}, {5, 6}, {6, 6}, {7, 6}, {7, 5}, {7, 4}, {7, 3}, {7, 2}, {7, 1}, {7, 0}, {6, 0}, {5, 0}, {4, 0}, {3, 0}, {2, 0}, {1, 0}]

      iex> Aoc19.Solution.Day03.get_wire(["R8", "U5", "L5", "D3"])
      [{2, 3}, {3, 3}, {4, 3}, {5, 3}, {5, 4}, {5, 5}, {5, 6}, {5, 7}, {5, 8}, {4, 8}, {3, 8}, {2, 8}, {1, 8}, {0, 8}, {0, 7}, {0, 6}, {0, 5}, {0, 4}, {0, 3}, {0, 2}, {0, 1}]

  """
  def get_wire(paths) do
    paths
    |> Enum.map(&steps/1)
    |> List.flatten()
    |> Enum.reduce(
      {{0, 0}, []},
      fn {x1, y1}, {{x2, y2}, seen} ->
        {{x1 + x2, y1 + y2}, [{x1 + x2, y1 + y2} | seen]}
      end
    )
    |> elem(1)
  end

  @doc """
  Get the Manhattan distance from position {0, 0}.

  ## Examples

      iex> Aoc19.Solution.Day03.manhattan_distance({-300, 100})
      400

      iex> Aoc19.Solution.Day03.manhattan_distance({-20, -20})
      40

      iex> Aoc19.Solution.Day03.manhattan_distance({111, 111})
      222

  """
  def manhattan_distance({x, y}), do: abs(x) + abs(y)

  @doc """
  Get step changesets for a path.

  ## Examples

  iex> Aoc19.Solution.Day03.steps("U4")
  [{1, 0}, {1, 0}, {1, 0}, {1, 0}]

  iex> Aoc19.Solution.Day03.steps("R2")
  [{0, 1}, {0, 1}]

  iex> Aoc19.Solution.Day03.steps("D3")
  [{-1, 0}, {-1, 0}, {-1, 0}]

  iex> Aoc19.Solution.Day03.steps("L1")
  [{0, -1}]

  """
  def steps(path) do
    {d, steps} = String.split_at(path, 1)
    modifier = direction(d)
    stop_at = String.to_integer(steps)
    1..stop_at |> Enum.map(fn _ -> modifier end)
  end
end
