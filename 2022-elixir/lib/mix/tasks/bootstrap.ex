defmodule Mix.Tasks.Aoc.New do
  use Mix.Task

  @shortdoc "Bootstrap new solution"
  @impl Mix.Task

  @year 2022

  def run([n, name]) do
    id = n |> String.pad_leading(2, "0")

    input_dir = "./inputs"
    solutions_dir = "./lib/solutions"
    tests_dir = "./test/solutions"

    input_file = input_dir <> "/" <> id <> ".in"
    test_file = tests_dir <> "/day_" <> id <> "_test.exs"
    solution_file = solutions_dir <> "/day_" <> id <> ".ex"

    for dir_path <- [input_dir, tests_dir, solutions_dir],
        do: unless(File.exists?(dir_path), do: File.mkdir(dir_path))

    IO.puts("Creating " <> input_file)
    File.touch(input_file)

    IO.puts("Creating " <> test_file)
    File.write!(test_file, test_file_content(id, name))

    IO.puts("Creating " <> solution_file)
    File.write!(solution_file, solution_file_content(name, id, n))

    """
    \nDone! Start coding.

    Get your puzzle input here:
    https://adventofcode.com/#{@year}/day/#{n}/input

    mix test                 -- run tests.
    mix aoc.solve_all        -- run all puzzles, starting with 1
    mix aoc.solve #{id}         -- run single puzzle, 1-25
    """
    |> IO.puts()
  end

  defp test_file_content(id, name) do
    """
    defmodule Day#{id}Test do
      use ExUnit.Case
      doctest Aoc.Solution.Day#{id}
      import Aoc.Solution.Day#{id}

      @input ~s(
        REPLACE ME
      )

      test "#{id}: #{name}, part 1" do
        expected = :something

        result = @input |> parse!() |> solve()

        assert result == expected
      end

      # test "#{id}: #{name}, part 2" do
      #   expected = :something

      #   result = @input |> parse!() |> solve_again()

      #   assert result == expected
      # end
    end
    """
  end

  defp solution_file_content(name, id, n) do
    ~s"""
    defmodule Aoc.Solution.Day#{id} do
      import Aoc.Utils

      @name "Day #{n}: #{name}"
      @behaviour Solution

      @impl Solution
      def get_name, do: @name

      @impl Solution
      def present(solution), do: "Solution is \#{solution}"

      @impl Solution
      def present_again(solution), do: "Solution is \#{solution}"

      @impl Solution
      def parse!(raw) do
        raw
      end

      @impl Solution
      def solve(_input) do
        "(TBW)"
      end

      @impl Solution
      def solve_again(_input) do
        "(TBW)"
      end
    end
    """
  end
end
