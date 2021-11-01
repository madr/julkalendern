defmodule Aoc19.Solution.Day04 do
  @name "Day 4: Secure Container"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  @doc """
  Get the range of numbers from the input.

  ## Examples

      iex> Aoc19.Solution.Day04.parse!("1-4")
      1..4

      iex> Aoc19.Solution.Day04.parse!("4-32")
      4..32
  """
  def parse!(str) do
    [start, stop] =
      str
      |> String.split("-")
      |> Enum.map(&String.to_integer/1)

    start..stop
  end

  @impl Solution
  @doc """
  Solution for the first part of "Day 4: Secure Container".
  """
  def solve_first_part(range),
    do: range |> Stream.filter(&matches?/1) |> Enum.count()

  @impl Solution
  @doc """
  Solution for the second part of "Day 4: Secure Container".
  """
  def solve_second_part(range),
    do:
      range
      |> Stream.filter(&matches?/1)
      |> Stream.filter(&larger_groups?/1)
      |> Enum.count()

  @doc """
  Check if password matches all initital criterias.

  ## Examples

      iex> Aoc19.Solution.Day04.matches?(8)
      true

      iex> Aoc19.Solution.Day04.matches?(12)
      true

      iex> Aoc19.Solution.Day04.matches?(1123)
      true

      iex> Aoc19.Solution.Day04.matches?(22222)
      true

      iex> Aoc19.Solution.Day04.matches?(122345)
      true

      iex> Aoc19.Solution.Day04.matches?(111123)
      true

      iex> Aoc19.Solution.Day04.matches?(223450)
      false

      iex> Aoc19.Solution.Day04.matches?(123789)
      false

  """
  def matches?(password) do
    [a, b, c, d, e, f] = number_to_password(password) |> String.codepoints()

    (a == b or b == c or c == d or d == e or e == f) and
      (a <= b and b <= c and c <= d and d <= e and e <= f)
  end

  @doc """
  Check if password digit pairs are not part of a larget group of digits.

  ## Examples

      iex> Aoc19.Solution.Day04.larger_groups?(112233)
      true

      iex> Aoc19.Solution.Day04.larger_groups?(123444)
      false

      iex> Aoc19.Solution.Day04.larger_groups?(111122)
      true

  """
  def larger_groups?(password) do
    washed = Regex.replace(~r/(\d)\1\1+/, number_to_password(password), "")

    case Regex.run(~r/(\d)\1/, washed) do
      nil -> false
      _ -> true
    end
  end

  @doc """
  Takes an integer and turns it to a password by making it a string
  and left pad it with zeros.

  ## Examples

  iex> Aoc19.Solution.Day04.number_to_password(8)
  "000008"

  iex> Aoc19.Solution.Day04.number_to_password(123)
  "000123"

  iex> Aoc19.Solution.Day04.number_to_password(123123)
  "123123"

  """
  def number_to_password(n),
    do: Integer.to_string(n) |> String.pad_leading(6, "0")
end
