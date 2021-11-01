defmodule Aoc19 do
  @moduledoc """
  Solutions for Advent of Code 2019, written in Elixir 1.9.2.
  """

  def solve_all() do
    """

    ADVENT OF CODE 2019
    ===================
    """
    |> IO.puts()

    1..25 |> Enum.map(&solve/1)
  end

  def solve(n) do
    id = n |> Integer.to_string() |> String.pad_leading(2, "0")

    case File.read("./inputs/" <> id <> ".in") do
      {:error, _} ->
        nil

      {:ok, input} ->
        input
        |> run(id)
        |> present
        |> IO.puts()
    end
  end

  def run(input, id) do
    solution_module = Module.concat(["Aoc19.Solution", "Day" <> id])

    data = apply(solution_module, :parse!, [input])
    name = apply(solution_module, :get_name, [])
    first_solution = apply(solution_module, :solve_first_part, [data])
    second_solution = apply(solution_module, :solve_second_part, [data])

    [name, first_solution, second_solution]
  end

  @doc """
  Generates a CLI-friendly presentation of the solutions.

  ## Examples

      iex> Aoc19.present(["Day 1: tomten kommer", "10", "20"])
      "Day 1: tomten kommer\\n--------------------\\n\\n1. 10\\n2. 20\\n"

  """
  def present([name, first_solution, second_solution]) do
    """
    #{name}
    #{1..String.length(name) |> Enum.map_join(fn _x -> "-" end)}

    1. #{first_solution}
    2. #{second_solution}
    """
  end
end
