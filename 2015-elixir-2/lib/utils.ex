defmodule Aoc.Utils do
  @doc """
  Extracts values as trimmed strings using a separator.

  ## Examples

      iex> Aoc.Utils.parse_values(~s(
      ...>   abc:
      ...>   123 q1w2e3r4
      ...> ), ":")
      ["abc", "123 q1w2e3r4"]

      iex> Aoc.Utils.parse_values(~s(
      ...>   abc AND 123 AND q1w2e3r4
      ...> ), "AND")
      ["abc", "123", "q1w2e3r4"]
  """
  def parse_values(input, separator) do
    input
    |> String.trim()
    |> String.split(separator)
    |> Enum.map(&String.trim/1)
  end

  @doc """
  Extracts values from input by white space as trimmed strings.

  ## Examples

      iex> Aoc.Utils.parse_values(~s(
      ...>   abc
      ...>   123 q1w2e3r4
      ...> ))
      ["abc", "123", "q1w2e3r4"]
  """
  def parse_values(input), do: String.split(input)

  @doc """
  Split input to trimmed lines.
  Equal to parse_values(input, ["\n", "\r"])

  ## Examples

      iex> Aoc.Utils.split_lines(~s(
      ...>   a bc
      ...>   12 3
      ...>   q1w2 e3r4
      ...> ))
      ["a bc", "12 3", "q1w2 e3r4"]
  """
  def split_lines(input), do: parse_values(input, ["\n", "\r"])

  @doc """
  Split input to trimmed strings by comma as separator.
  Equal to Aoc.Utils.parse_values(input, ",")

  ## Examples

      iex> Aoc.Utils.parse_csv(~s(
      ...>   abc,123,q1w2 e3r4
      ...> ))
      ["abc", "123", "q1w2 e3r4"]
  """
  def parse_csv(input), do: parse_values(input, ",")
end
