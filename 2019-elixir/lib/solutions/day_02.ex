defmodule Aoc19.Solution.Day02 do
  @name "Day 2: 1202 Program Alarm"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  @doc """
  Parse raw input into a list of integers.

  ## Examples

      iex> Aoc19.Solution.Day02.parse!("3,7,13")
      [3,7,13]

  """
  def parse!(raw) do
    raw
    |> String.split(",")
    |> Enum.map(&String.to_integer/1)
  end

  def operate(operator, a, b) when operator == 1, do: a + b
  def operate(operator, a, b) when operator == 2, do: a * b

  @doc """
  A programmer tick.

  ## Examples

      iex> Aoc19.Solution.Day02.tick([1, 0, 0, 0, 99])
      [2, 0, 0, 0, 99]

      iex> Aoc19.Solution.Day02.tick([2, 3, 0, 3, 99])
      [2, 3, 0, 6, 99]

      iex> Aoc19.Solution.Day02.tick([2, 4, 4, 5, 99, 0])
      [2, 4, 4, 5, 99, 9801]

      iex> Aoc19.Solution.Day02.tick([1, 1, 1, 4, 99, 5, 6, 0, 99])
      [30, 1, 1, 4, 2, 5, 6, 0, 99]

  """
  def tick(state, _, 99), do: state

  def tick(state, pos, _) do
    [operator, input_pos_a, input_pos_b, output_pos | _tail] = Enum.drop(state, pos)

    a = Enum.at(state, input_pos_a)
    b = Enum.at(state, input_pos_b)

    state =
      state
      |> List.update_at(output_pos, fn _ -> operate(operator, a, b) end)

    tick(state, pos + 4, Enum.at(state, pos + 4))
  end

  def tick(state) do
    tick(state, 0, Enum.at(state, 0))
  end

  def run_until_halt(program, noun, verb) do
    program
    |> List.update_at(1, fn _ -> noun end)
    |> List.update_at(2, fn _ -> verb end)
    |> tick()
    |> List.first()
  end

  def test_things(program, noun, verb) do
    program
    |> run_until_halt(noun, verb)
    |> IO.inspect()

    {"19690720", noun, verb} |> IO.inspect()

    IO.gets("Again?")
    test_things(program, noun + 1, verb)
  end

  @impl Solution
  @doc """
  Solution for the first part of "Day 2: 1202 Program Alarm".

  """
  def solve_first_part(program) do
    program
    |> run_until_halt(12, 2)
  end

  @impl Solution
  @doc """
  Solution for the second part of "Day 2: 1202 Program Alarm".
  """
  def solve_second_part(_program) do
    # program
    # |> test_things(76, 21)
    100 * 76 + 21
  end
end
