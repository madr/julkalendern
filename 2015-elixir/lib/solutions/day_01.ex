defmodule Aoc.Solution.Day01 do
  @name "Day 1: Not Quite Lisp"
  @behaviour Solution

  @basement -1

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def parse!(raw) do
    raw
    |> String.split("", trim: true)
  end

  @impl Solution
  def solve_first_part(input) do
    input
    |> Enum.map(fn d ->
      case d do
        "(" -> 1
        ")" -> -1
        _ -> 0
      end
    end)
    |> Enum.sum()
  end

  @impl Solution
  def solve_second_part(input) do
    [change | changes] =
      input
      |> Enum.map(fn d ->
        case d do
          "(" -> 1
          ")" -> -1
          _ -> 0
        end
      end)

    move(change, 1, 0, changes)
  end

  defp move(change, pos, current, []) do
    case current + change do
      @basement -> pos
      _ -> :basement_never_reached
    end
  end

  defp move(change, pos, current, [next | changes]) do
    case current + change do
      @basement -> pos
      _ -> move(next, pos + 1, current + change, changes)
    end
  end
end
