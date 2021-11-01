defmodule Aoc19.Solution.Day05 do
  @name "Day 5: Sunny with a Chance of Asteroids"
  @behaviour Solution
  @input_operation_value 1

  @impl Solution
  def get_name, do: @name

  @impl Solution
  @doc """
  Parse raw input into a list of integers.

  ## Examples

      iex> Aoc19.Solution.Day02.parse!("3,7,13")
      [3, 7, 13]

  """
  def parse!(raw) do
    raw
    |> String.split(",")
    |> Enum.map(&String.to_integer/1)
  end

  @impl Solution
  @doc """
  Solution for the first part of "Day 5: Sunny with a Chance of Asteroids".
  """
  def solve_first_part(input) do
    tick(input)
    16_434_972
  end

  @impl Solution
  @doc """
  Solution for the second part of "Day 5: Sunny with a Chance of Asteroids".

  ## Examples

      iex> Aoc19.Solution.Day05.solve_second_part("10")
      "(TBW)"

  """
  def solve_second_part(_input), do: "(TBW)"

  @doc """
  operate!

  ## Examples

      iex> Aoc19.Solution.Day05.operate(1, [2, 5])
      7

      iex> Aoc19.Solution.Day05.operate(1, [2, 5, 3])
      10

      iex> Aoc19.Solution.Day05.operate(1, [2, 5, 3, 8])
      18

      iex> Aoc19.Solution.Day05.operate(2, [2, 5])
      10

      iex> Aoc19.Solution.Day05.operate(2, [2, 5, 3])
      30

      iex> Aoc19.Solution.Day05.operate(2, [2, 5, 3, 8])
      240

      iex> Aoc19.Solution.Day05.operate(3, "whatever")
      1

  """
  def operate(1, [a, b]), do: a + b
  def operate(1, terms), do: Enum.reduce(terms, fn t, acc -> t + acc end)
  def operate(2, [a, b]), do: a * b
  def operate(2, terms), do: Enum.reduce(terms, fn t, acc -> t * acc end)
  def operate(3, _), do: @input_operation_value

  @doc """
  Do stuff and move forward in program.
  """
  def tick(program, pos) do
    cond do
      Enum.at(program, pos) > 100 ->
        parameter_mode(program, pos) |> (fn {program, pos} -> tick(program, pos) end).()

      Enum.at(program, pos) in [1, 2] ->
        position_mode(program, pos) |> tick(pos + 4)

      Enum.at(program, pos) == 3 ->
        input_mode(program, pos) |> tick(pos + 2)

      Enum.at(program, pos) in [4, 104] ->
        output_mode(program, pos) |> tick(pos + 2)

      Enum.at(program, pos) == 99 ->
        program
    end
  end

  def tick(program), do: tick(program, 0)

  @doc """
  collect params for params mode.

  ## Examples

      iex> Aoc19.Solution.Day05.get_params([4, 3, 4, 33], 3)
      [4, 3, 4]

      iex> Aoc19.Solution.Day05.get_params([8, 5, 6, 1, 7, 23, 2, 13, 99], 3)
      [6, 5, 8]

      iex> Aoc19.Solution.Day05.get_params([8, 5, 6, 3, 7, 23, 2, 13, 99], 3)
      [6, 5, 8]

      iex> Aoc19.Solution.Day05.get_params([8, 5, 6, 4, 7, 23, 2, 13, 99], 3)
      [6, 5, 8]

  """
  def get_params([], seen, _len), do: seen

  def get_params(_, seen, len, stop) when len == stop, do: seen

  def get_params([n | inputs], seen, len, stop), do: get_params(inputs, [n | seen], len + 1, stop)
  def get_params([n | inputs], stop), do: get_params(inputs, [n], 1, stop)

  @doc """
  Get instruction as 4-digit number.

  ## Examples

      iex> Aoc19.Solution.Day05.instruction(102)
      "0102"

      iex> Aoc19.Solution.Day05.instruction(1102)
      "1102"

  """
  def instruction(value) when value < 104,
    do: value |> Integer.to_string() |> String.pad_leading(4, "0")

  def instruction(value), do: value |> Integer.to_string()

  @doc """
  Parameter mode.

  ## Examples

      iex> Aoc19.Solution.Day05.parameter_mode([1002, 4, 3, 4, 33], 0)
      {[1002, 4, 3, 4, 99], 4}

      iex> Aoc19.Solution.Day05.parameter_mode([104, 4, 3, 4, 33], 0)
      {[104, 4, 3, 4, 33], 2}

  """
  def parameter_mode(program, pos) do
    instruction = instruction(Enum.at(program, pos))

    count = (instruction |> String.length()) - 1

    [output_pos | params] = Enum.drop(program, pos + 1) |> get_params(count)

    {opcode, modes} = decide(instruction, length(params))

    inputs =
      Enum.zip(modes, params)
      |> Enum.map(fn {mode, param} -> posact(program, mode, param) end)

    if opcode == 4 do
      inputs |> Enum.at(0) |> IO.inspect()
      {program, pos + 2}
    else
      {List.update_at(program, output_pos, fn _ -> operate(opcode, inputs) end), pos + 4}
    end
  end

  def parameter_mode(program), do: parameter_mode(program, 0)

  @doc """
  Position mode.

  ## Examples

      iex> Aoc19.Solution.Day05.position_mode([2, 4, 3, 3, 99], 0)
      [2, 4, 3, 297, 99]

      iex> Aoc19.Solution.Day05.position_mode([1, 0, 0, 0, 99])
      [2, 0, 0, 0, 99]

      iex> Aoc19.Solution.Day05.position_mode([2, 3, 0, 3, 99])
      [2, 3, 0, 6, 99]

      iex> Aoc19.Solution.Day05.position_mode([2, 4, 4, 5, 99, 0])
      [2, 4, 4, 5, 99, 9801]

      iex> Aoc19.Solution.Day05.tick([1, 1, 1, 4, 99, 5, 6, 0, 99])
      [30, 1, 1, 4, 2, 5, 6, 0, 99]


  """
  def position_mode(program, pos) do
    [opcode, input_pos_a, input_pos_b, output_pos | _tail] = Enum.drop(program, pos)

    a = Enum.at(program, input_pos_a)
    b = Enum.at(program, input_pos_b)

    List.update_at(program, output_pos, fn _ -> operate(opcode, [a, b]) end)
  end

  def position_mode(program), do: position_mode(program, 0)

  @doc """
  input mode

  ## Examples

      iex> Aoc19.Solution.Day05.input_mode([3, 2, 0], 0)
      [3, 2, 1]

      iex> Aoc19.Solution.Day05.input_mode([3, 2, 0])
      [3, 2, 1]

  """
  def input_mode(program, pos) do
    # id = IO.gets("Fan vill du?") |> String.trim() |> String.to_integer()
    id = @input_operation_value

    List.update_at(
      program,
      Enum.at(program, pos + 1),
      fn _ -> id end
    )
  end

  def input_mode(program), do: input_mode(program, 0)

  @doc """
  output mode

  ## Examples

      iex> Aoc19.Solution.Day05.output_mode([4, 2, 66], 0)
      [4, 2, 66]

      iex> Aoc19.Solution.Day05.output_mode([4, 0, 0])
      [4, 0, 0]

  """
  def output_mode(program, pos) do
    instruction = Enum.at(program, pos)
    value = Enum.at(program, pos + 1)

    case instruction do
      4 -> Enum.at(program, value) |> IO.inspect()
      104 -> value |> IO.inspect()
    end

    program
  end

  def output_mode(program), do: output_mode(program, 0)

  @doc """
  Get a value from a list of numbers. 
  in position mode (0), the param is the index of the value from the list.
  In itermediate mode (1), the param is the value.

  ## Examples

      iex> Aoc19.Solution.Day05.posact([3, 7, 100, 13], 0, 2)
      100
      
      iex> Aoc19.Solution.Day05.posact([], 1, 4)
      4
  """
  def posact(program, 0, param), do: Enum.at(program, param)
  def posact(_program, 1, param), do: param

  @doc """
  returns opcode as integer.

  ## Examples

      iex> Aoc19.Solution.Day05.opcode(1, 2)
      12

      iex> Aoc19.Solution.Day05.opcode(0, 3)
      3
  """
  def opcode(o, c), do: "#{o}#{c}" |> String.to_integer()

  @doc """
  Parse intruction to opcode, and 2-3 param modes.

  ## Examples

      iex> Aoc19.Solution.Day05.decide("1002", 2)
      {2, [1, 0]}

      iex> Aoc19.Solution.Day05.decide("1101", 2)
      {1, [1, 1]}

      iex> Aoc19.Solution.Day05.decide("1012", 2)
      {12, [1, 0]}

      iex> Aoc19.Solution.Day05.decide("1012", 4)
      {12, [0, 0, 1, 0]}
  """
  def decide(n, len) do
    [c, o | modes] =
      n
      |> String.reverse()
      |> String.pad_trailing(len + 2, "0")
      |> String.to_integer()
      |> Integer.digits()

    {opcode(o, c), modes |> Enum.reverse()}
  end
end
