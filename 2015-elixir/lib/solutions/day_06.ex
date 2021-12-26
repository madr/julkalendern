defmodule Aoc.Solution.Day06 do
  @name "Day 6: Probably a Fire Hazard"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def parse!(raw) do
    r = ~r/ ?(\S+) (\d+),(\d+) through (\d+),(\d+)/

    raw
    |> String.split("\n")
    |> Enum.map(fn row ->
      [_, verb, x1, y1, x2, y2] = Regex.run(r, row)
      {verb, String.to_integer(x1)..String.to_integer(x2), String.to_integer(y1)..String.to_integer(y2)}
    end)
  end

  @impl Solution
  def solve_first_part(input) do
    lit = MapSet.new()
    change_state(lit, input) |> MapSet.size()
  end

  @impl Solution
  def solve_second_part(input) do
    lit = Map.new()
    adjust_brightness(lit, input)
  end

  defp change_state(lit, []) do
    lit
  end

  defp change_state(lit, [ {verb, xset, yset} | remaining]) do
    change = for x <- xset do
      for y <- yset do
        {x, y}
      end
    end |> List.flatten() |> MapSet.new()
    case verb do
      "on" ->
        change_state(MapSet.union(lit, change), remaining)

      "off" ->
        change_state(MapSet.difference(lit, change), remaining)

      "toggle" ->
        to_lit = MapSet.difference(change, lit)
        to_unlit = MapSet.difference(lit, change)
        change_state(MapSet.union(to_lit, to_unlit), remaining)
    end
  end

  defp adjust_brightness(lit, []) do
    Map.values(lit) |> Enum.sum
  end

  defp adjust_brightness(lit, [ {verb, xset, yset} | remaining]) do
    change = for x <- xset do
      for y <- yset do
        {x, y}
      end
    end |> List.flatten()
    updated = case verb do
      "on" ->
        Enum.reduce(change, lit, fn xy, acc ->
          if Map.has_key?(acc, xy) do
            %{acc | xy => Map.get(acc, xy) + 1}
          else
            Map.put(acc, xy, 1)
          end
        end)

      "off" ->
        Enum.reduce(change, lit, fn xy, acc ->
          if Map.has_key?(acc, xy) do
            %{acc | xy => max(Map.get(acc, xy) - 1, 0)}
          else
            acc
          end
        end)

      "toggle" ->
        Enum.reduce(change, lit, fn xy, acc ->
          if Map.has_key?(acc, xy) do
            %{acc | xy => Map.get(acc, xy) + 2}
          else
            Map.put(acc, xy, 2)
          end
        end)
      end
      adjust_brightness(updated, remaining)
  end
end
