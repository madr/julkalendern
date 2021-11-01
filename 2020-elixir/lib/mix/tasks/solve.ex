defmodule Mix.Tasks.Aoc.Solve do
  use Mix.Task

  @shortdoc "Solve single puzzle"
  @impl Mix.Task
  def run([id]) do
    id
    |> String.to_integer()
    |> Aoc.solve()
  end
end
