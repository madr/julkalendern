defmodule Aoc.Solution.Day04 do
  @name "Day 4: The Ideal Stocking Stuffer"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def parse!(raw) do
    String.trim(raw)
  end

  @impl Solution
  def solve_first_part(input) do
    find_number(input, 0, "00000")
  end

  @impl Solution
  def solve_second_part(input) do
    find_number(input, 0, "000000")
  end

  defp find_number(a, b, prefix) do
    case valid_checksum?(a, b, prefix) do
      true -> b
      false -> find_number(a, b + 1, prefix)
    end
  end

  defp valid_checksum?(a, b, prefix) do
    :crypto.hash(:md5, "#{a}#{b}")
    |> Base.encode16()
    |> String.starts_with?(prefix)
  end
end
