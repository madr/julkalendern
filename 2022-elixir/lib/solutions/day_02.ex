defmodule Aoc.Solution.Day02 do
  import Aoc.Utils

  @name "Day 2: Rock Paper Scissors"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def present(solution), do: "Asumed strategy guide will grant #{solution} total score"

  @impl Solution
  def present_again(solution), do: "Actual strategy guide will grant #{solution} total score"

  @impl Solution
  def parse!(raw) do
    raw |> split_lines() |> Enum.map(&parse_values/1)
  end

  @impl Solution
  def solve(rounds) do
    rounds |> Enum.map(&asumed_score/1) |> Enum.sum()
  end

  @impl Solution
  def solve_again(rounds) do
    rounds |> Enum.map(&score/1) |> Enum.sum()
  end

  def asumed_score([opponent, "X"]) do
    result =
      case opponent do
        "A" -> 3
        "B" -> 0
        "C" -> 6
      end

    result + 1
  end

  def asumed_score([opponent, "Y"]) do
    result =
      case opponent do
        "A" -> 6
        "B" -> 3
        "C" -> 0
      end

    result + 2
  end

  def asumed_score([opponent, "Z"]) do
    result =
      case opponent do
        "A" -> 0
        "B" -> 6
        "C" -> 3
      end

    result + 3
  end

  def score([opponent, "X"]) do
    result =
      case opponent do
        "A" -> 3
        "B" -> 1
        "C" -> 2
      end

    result
  end

  def score([opponent, "Y"]) do
    result =
      case opponent do
        "A" -> 1
        "B" -> 2
        "C" -> 3
      end

    result + 3
  end

  def score([opponent, "Z"]) do
    result =
      case opponent do
        "A" -> 2
        "B" -> 3
        "C" -> 1
      end

    result + 6
  end
end
