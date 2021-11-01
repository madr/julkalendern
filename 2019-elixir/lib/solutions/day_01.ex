defmodule Aoc19.Solution.Day01 do
  @name "Day 1: The Tyranny of the Rocket Equation"
  @behaviour Solution
  # when required fuel is below 9 no furher fuel is required (fuel_requirement(n) < 0)
  @fuel_threshold 9

  @impl Solution
  def get_name, do: @name

  @impl Solution
  @doc """
  Parse raw input into a list of integers.

  ## Examples

      iex> Aoc19.Solution.Day01.parse!(\"\"\"
      ...> 10
      ...> 299
      ...> 1040
      ...> \"\"\")
      [10,299,1040]

  """
  def parse!(raw) do
    raw
    |> String.split()
    |> Enum.map(&String.to_integer/1)
  end

  @doc """
  Calculate required fuel for a module's mass. This formula
  is also used to calculate the fuel required for the fuel 
  itself.

  Take mass, divide by three, round down, and subtract 2.

  ## Examples

      iex> Aoc19.Solution.Day01.fuel_requirement(12)
      2

      iex> Aoc19.Solution.Day01.fuel_requirement(14)
      2

      iex> Aoc19.Solution.Day01.fuel_requirement(1969)
      654

      iex> Aoc19.Solution.Day01.fuel_requirement(100756)
      33583

  """
  def fuel_requirement(thing) do
    (thing |> div(3)) - 2
  end

  @doc """
  Calculate fuel requirements based on a module's mass,
  including the fuel required by the fuel itself.

  ## Examples

      iex> Aoc19.Solution.Day01.total_fuel_requirement(12)
      2

      iex> Aoc19.Solution.Day01.total_fuel_requirement(1969)
      966

      iex> Aoc19.Solution.Day01.total_fuel_requirement(100756)
      50346

  """
  def total_fuel_requirement(thing, requirements) when thing < @fuel_threshold do
    Enum.sum(requirements)
  end

  def total_fuel_requirement(thing, requirements) do
    fuel = fuel_requirement(thing)
    total_fuel_requirement(fuel, [fuel | requirements])
  end

  def total_fuel_requirement(mass) do
    fuel = fuel_requirement(mass)
    total_fuel_requirement(fuel, [fuel])
  end

  @impl Solution
  @doc """
  Solution for the first part of "Day 1: The Tyranny of the Rocket Equation".

  ## Examples

      iex> Aoc19.Solution.Day01.solve_first_part([12, 14, 1969, 100756])
      34241

  """
  def solve_first_part(input) do
    input |> Enum.map(&fuel_requirement/1) |> Enum.sum()
  end

  @impl Solution
  @doc """
  Solution for the second part of "Day 1: The Tyranny of the Rocket Equation".

  ## Examples

      iex> Aoc19.Solution.Day01.solve_second_part([12, 1969, 100756])
      51314

  """
  def solve_second_part(input) do
    input |> Enum.map(&total_fuel_requirement/1) |> Enum.sum()
  end
end
