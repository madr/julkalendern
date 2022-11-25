defmodule Aoc.Solution.Day07 do
  import Bitwise
  import Aoc.Utils

  @name "Day 7: Some Assembly Required"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def parse!(raw) do
    split_lines(raw)
    |> Enum.map(fn l -> parse_values(l, " -> ") end)
  end

  @impl Solution
  def solve(input, k \\ "a") do
    wires = Map.new()
    all = Enum.count(input)
    wire(wires, all, input) |> Map.get(k)
  end

  @impl Solution
  def solve_again(input) do
    value = solve(input)

    solve(
      Enum.map(
        input,
        fn [o, i] ->
          case i do
            "b" -> [Integer.to_string(value), i]
            _ -> [o, i]
          end
        end
      )
    )
  end

  def wire(wires, all, queue) do
    wires = walk(wires, queue)

    case Enum.count(wires) do
      ^all -> wires
      _ -> wire(wires, all, queue)
    end
  end

  def walk(wires, []), do: wires

  def walk(wires, [[output, input] | remain]) do
    case apply_rule(wires, String.split(output)) do
      nil ->
        walk(wires, remain)

      v ->
        walk(
          Map.put_new(
            wires,
            input,
            v
          ),
          remain
        )
    end
  end

  def apply_rule(wires, ["NOT", wire]) do
    case Map.get(wires, wire) do
      nil -> nil
      v -> 65536 + bnot(v)
    end
  end

  def apply_rule(wires, [l, "AND", r]) do
    l = _value(wires, l)
    r = _value(wires, r)
    case Enum.all?([l, r]) do
      false -> nil
      true -> l &&& r
    end
  end

  def apply_rule(wires, [l, "OR", r]) do
    l = _value(wires, l)
    r = _value(wires, r)
    case Enum.all?([l, r]) do
      false -> nil
      true -> bor(l, r)
    end
  end

  def apply_rule(wires, [l, "RSHIFT", r]) do
    case Map.get(wires, l) do
      nil -> nil
      l -> l >>> String.to_integer(r)
    end
  end

  def apply_rule(wires, [l, "LSHIFT", r]) do
    case Map.get(wires, l) do
      nil -> nil
      l -> l <<< String.to_integer(r)
    end
  end

  def apply_rule(wires, [wire]) do
    _value(wires, wire)
  end

  def _value(seen, k) do
    try do
      case Map.get(seen, k) do
        nil -> String.to_integer(k)
        v -> v
      end
    rescue
      _e -> nil
    end
  end
end
