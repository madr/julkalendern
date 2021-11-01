defmodule Mix.Tasks.Aoc19.SolveAll do
  use Mix.Task

  @shortdoc "Solve all puzzles"
  @impl Mix.Task
  def run(_) do
    Aoc19.solve_all()
  end
end
