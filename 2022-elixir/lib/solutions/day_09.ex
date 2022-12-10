defmodule Aoc.Solution.Day09 do
  import Aoc.Utils

  @name "Day 9: Rope Bridge"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def present(solution), do: "The rope tail visits #{solution} positions at least once"

  @impl Solution
  def present_again(solution), do: "Solution is #{solution}"

  @impl Solution
  def parse!(raw) do
    raw |> split_lines()
  end

  @impl Solution
  def solve(motions) do
    motions
    |> move()
    |> visited()
  end

  @impl Solution
  def solve_again(_input) do
    "(TBW)"
  end

  def move(motions) when is_list(motions) do
    {_h, _t, seen} = Enum.reduce(motions, {{0, 0}, {0, 0}, MapSet.new()}, &move/2)

    seen
  end

  def move("R " <> steps, acc) do
    change = {0, String.to_integer(steps)}
    {h, t, seen} = acc
    {y, x} = h

    {y, x + String.to_integer(steps)}
    |> follow(change, t, seen)
  end

  def move("L " <> steps, acc) do
    change = {0, 0 - String.to_integer(steps)}
    {h, t, seen} = acc
    {y, x} = h

    {y, x - String.to_integer(steps)}
    |> follow(change, t, seen)
  end

  def move("U " <> steps, acc) do
    change = {String.to_integer(steps), 0}
    {h, t, seen} = acc
    {y, x} = h

    {y + String.to_integer(steps), x}
    |> follow(change, t, seen)
  end

  def move("D " <> steps, acc) do
    change = {0 - String.to_integer(steps), 0}
    {h, t, seen} = acc
    {y, x} = h

    {y - String.to_integer(steps), x}
    |> follow(change, t, seen)
  end

  def follow(h = {y2, x2}, _change, t = {y1, x1}, seen) when y2 == y1 and x2 == x1 do
    {h, t, MapSet.put(seen, t)}
  end

  def follow(h = {_yH, xH}, {change, 0}, {y, _x}, seen) when change > 2 do
    pos = {y + change - 1, xH}
    {h, pos, MapSet.put(seen, pos)}
  end

  def follow(h = {_yH, xH}, {change, 0}, {y, _x}, seen) when change < -2 do
    pos = {y + change + 1, xH}
    {h, pos, MapSet.put(seen, pos)}
  end

  def follow(h = {yH, _xH}, {0, change}, {_y, x}, seen) when change > 2 do
    pos = {yH, x + change - 1}
    {h, pos, MapSet.put(seen, pos)}
  end

  def follow(h = {yH, _xH}, {0, change}, {_y, x}, seen) when change < -2 do
    pos = {yH, x + change + 1}
    {h, pos, MapSet.put(seen, pos)}
  end

  def follow(h = {y2, x2}, _change, t = {y1, x1}, seen) do
    pos =
      case {abs(abs(y2) - abs(y1)), abs(abs(x2) - abs(x1))} do
        {1, 1} -> t
        {1, 0} -> t
        {0, 1} -> t
      end

    {h, pos, MapSet.put(seen, pos)}
  end

  def visited(positions) do
    MapSet.size(positions)
  end
end
