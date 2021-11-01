defmodule Mix.Tasks.Aoc19.New do
  use Mix.Task

  @shortdoc "Bootstrap new solution"
  @impl Mix.Task
  def run([n, name]) do
    id = n |> String.pad_leading(2, "0")

    input_file = "./inputs/" <> id <> ".in"
    test_file = "./test/day_" <> id <> "_test.exs"
    solution_file = "./lib/solutions/day_" <> id <> ".ex"

    IO.puts("Creating " <> input_file)
    File.touch(input_file)

    IO.puts("Creating " <> test_file)
    File.write!(test_file, test_file_content(id))

    IO.puts("Creating " <> solution_file)
    File.write!(solution_file, solution_file_content(name, id))

    """
    \nDone! Start coding. 

    mix test                   -- run tests.
    mix aoc19:solve_all        -- run all puzzles, starting with 1
    mix aoc19:solve <integer>  -- run single puzzle, 1-25
    """
    |> IO.puts()
  end

  defp test_file_content(id) do
    """
    defmodule Day#{id}Test do
      use ExUnit.Case
      doctest Aoc19.Solution.Day#{id}
    end
    """
  end

  defp solution_file_content(name, id) do
    ~s"""
    defmodule Aoc19.Solution.Day#{id} do
      @name "#{name}"
      @behaviour Solution

      @impl Solution
      def get_name, do: @name

      @impl Solution
      def parse!(_str), do: "10"

      @impl Solution
      @doc \"\"\"
      Solution for the first part of "#{name}".

      ## Examples

          iex> Aoc19.Solution.Day#{id}.solve_first_part("10")
          "(TBW)"

      \"\"\"
      def solve_first_part(_input), do: "(TBW)"

      @impl Solution
      @doc \"\"\"
      Solution for the second part of "#{name}".

      ## Examples

          iex> Aoc19.Solution.Day#{id}.solve_second_part("10")
          "(TBW)"

      \"\"\"
      def solve_second_part(_input), do: "(TBW)"
    end
    """
  end
end
