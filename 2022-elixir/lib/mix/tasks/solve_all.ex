defmodule Mix.Tasks.Aoc.SolveAll do
  use Mix.Task

  @shortdoc "Solve all puzzles"
  @impl Mix.Task
  def run(_) do
    Aoc.solve_all()
  end
end
