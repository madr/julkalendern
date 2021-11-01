defmodule Mix.Tasks.Aoc.New do
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

    Get your puzzle input here:
    https://adventofcode.com/2015/day/#{id}/input

    mix test                 -- run tests.
    mix Aoc.solve_all        -- run all puzzles, starting with 1
    mix Aoc.solve #{id}         -- run single puzzle, 1-25
    """
    |> IO.puts()
  end

  defp test_file_content(id) do
    """
    defmodule Day#{id}Test do
      use ExUnit.Case
      doctest Aoc.Solution.Day#{id}
      import Aoc.Solution.Day#{id}

      test "parses the input" do
        expected = 10

        assert parse!("10") == expected
      end

      test "solves first part" do
        a = "something" |> parse!() |> solve_first_part()

        expect a == :something
      end

      test "solves second part" do
        a = "something" |> parse!() |> solve_second_part()

        expect a == :something
      end
    end
    """
  end

  defp solution_file_content(name, id) do
    ~s"""
    defmodule Aoc.Solution.Day#{id} do
      @name "#{name}"
      @behaviour Solution

      @impl Solution
      def get_name, do: @name

      @impl Solution
      def parse!(_raw) do
        "10"
      end

      @impl Solution
      def solve_first_part(_input) do
        "(TBW)"
      end

      @impl Solution
      def solve_second_part(_input) do
        "(TBW)"
      end
    end
    """
  end
end
