defmodule Aoc.Solution.Day10 do
  import Aoc.Utils

  @name "Day 10: Cathode-Ray Tube"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def present(solution), do: "Sum of signal strengths is #{solution}"

  @impl Solution
  def present_again(solution), do: "The 8 capital letters appearing on CRT:\n\n#{solution}"

  @impl Solution
  def parse!(raw) do
    raw |> split_lines()
  end

  @impl Solution
  def solve(program) do
    {snapshots, _} = cycle(program)
    Enum.sum(snapshots)
  end

  @impl Solution
  def solve_again(program) do
    {_, pixels} = cycle(program)

    pixels
    |> Enum.reverse()
    |> Enum.chunk_every(40)
    |> Enum.map(fn l ->
      Enum.join(l, "")
    end)
    |> Enum.join("\n")
  end

  def cycle(program), do: cycle(1, program, program)

  def cycle(x, instructions, program, snapshots \\ {[], []}, queue \\ [], ticks \\ 1)

  def cycle(_x, _instructions, _program, snapshots, _queue, 241) do
    snapshots
  end

  def cycle(x, [], program, snapshots, queue, ticks) do
    cycle(x, program, program, snapshots, queue, ticks)
  end

  def cycle(x, instructions, program, snapshots, [v | queue], ticks) do
    cycle(x + v, instructions, program, log(snapshots, ticks, x), queue, ticks + 1)
  end

  def cycle(x, ["noop" | instructions], program, snapshots, queue = [], ticks) do
    cycle(x, instructions, program, log(snapshots, ticks, x), queue, ticks + 1)
  end

  def cycle(x, ["addx " <> v | instructions], program, snapshots, queue = [], ticks) do
    cycle(
      x,
      instructions,
      program,
      log(snapshots, ticks, x),
      [String.to_integer(v) | queue],
      ticks + 1
    )
  end

  def log({snapshots, pixels}, ticks, x) when ticks in [20, 60, 100, 140, 180, 220] do
    {[ticks * x | snapshots], lit(pixels, ticks, x)}
  end

  def log({snapshots, pixels}, ticks, x) do
    {snapshots, lit(pixels, ticks, x)}
  end

  def lit(pixels, pos, x) when rem(pos - 1, 40) in (x - 1)..(x + 1) do
    ["#" | pixels]
  end

  def lit(pixels, _pos, _x), do: ["." | pixels]
end
