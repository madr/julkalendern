defmodule Aoc.Solution.Day06 do
  @name "Day 6: Tuning Trouble"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def present(solution), do: "Packet marker is at #{solution}"

  @impl Solution
  def present_again(solution), do: "Message marker is at #{solution}"

  @impl Solution
  def parse!(raw) do
    raw |> String.trim() |> String.codepoints()
  end

  @impl Solution
  def solve(datastream) do
    datastream |> packet_marker()
  end

  @impl Solution
  def solve_again(datastream) do
    datastream |> message_marker()
  end

  def packet_marker(datastream) do
    distinct_sequence(datastream, 4)
  end

  def message_marker(datastream) do
    distinct_sequence(datastream, 14)
  end

  def distinct_sequence(datastream, l, start \\ 0) do
    case datastream |> Enum.slice(start, l) |> MapSet.new() |> MapSet.size() do
      ^l -> start + l
      _ -> distinct_sequence(datastream, l, start + 1)
    end
  end
end
