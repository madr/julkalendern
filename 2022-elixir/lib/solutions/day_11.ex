defmodule Aoc.Solution.Day11 do
  import Aoc.Utils

  @turns 20

  @name "Day 11: Monkey in the Middle"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def present(solution), do: "Monkey business is #{solution} (50616)"

  @impl Solution
  def present_again(solution), do: "Solution is #{solution}"

  @impl Solution
  def parse!(raw) do
    raw
    |> parse_values("\n\n")
    |> into_monkeys()
  end

  @impl Solution
  def solve(monkeys) do
    monkeys
    |> take_turns()
    |> investigate()
    |> monkey_biz()
  end

  @impl Solution
  def solve_again(_input) do
    "(TBW)"
  end

  def into_monkeys(monkeys) when is_list(monkeys) do
    Enum.map(monkeys, &monkey/1)
  end

  def monkey([], ms) when is_map(ms) do
    ms
  end

  def monkey(["Starting items: " <> items | data], ms) do
    monkey(data, %{ms | items: parse_values(items, ", ")})
  end

  def monkey(["Operation: new = " <> f | data], ms) do
    monkey(data, %{ms | op: operation(f)})
  end

  def monkey(["Test: divisible by " <> d | data], ms) do
    monkey(data, %{ms | test: String.to_integer(d)})
  end

  def monkey(["If true: throw to monkey " <> mid | data], ms) do
    monkey(data, %{ms | pass: String.to_integer(mid)})
  end

  def monkey(["If false: throw to monkey " <> mid | data], ms) do
    monkey(data, %{ms | fail: String.to_integer(mid)})
  end

  def monkey(["Monkey " <> mid | data]) do
    mid = String.first(mid) |> String.to_integer()
    monkey(data, %{id: mid, items: [], op: nil, test: 0, pass: 0, fail: 0, count: 0})
  end

  def monkey(text) do
    monkey(split_lines(text))
  end

  def operation("old * old") do
    {&oo/2, nil}
  end

  def operation("old * " <> x) do
    {&o_times_x/2, String.to_integer(x)}
  end

  def operation("old + " <> x) do
    {&o_plus_x/2, String.to_integer(x)}
  end

  def oo(x, _) when is_binary(x) do
    oo(String.to_integer(x), nil)
  end

  def oo(x, _), do: x * x

  def o_plus_x(x, y) when is_binary(x) do
    String.to_integer(x) + y
  end

  def o_plus_x(x, y), do: x + y

  def o_times_x(x, y) when is_binary(x) do
    String.to_integer(x) * y
  end

  def o_times_x(x, y), do: x * y

  def take_turns(monkeys, n \\ 0)

  def take_turns(monkeys, @turns) do
    monkeys
  end

  def take_turns(monkeys, n) do
    monkeys
    |> take_turns(n + 1)
    |> exchange_items()
  end

  def monkey_biz(monkeys) do
    [a, b | _] =
      monkeys
      |> Enum.map(fn %{count: count} -> count end)
      |> Enum.sort()
      |> Enum.reverse()

    a * b
  end

  def exchange_items(monkeys) do
    monkeys
    |> throw_items()
    |> receive_items()
    |> investigate()
  end

  def throw_items(monkeys) when is_list(monkeys) do
    {
      Enum.reduce(monkeys, [], &throw_items/2),
      monkeys
    }
  end

  def throw_items(%{id: mid, items: items, op: {f, a}, test: test, pass: pass, fail: fail}, acc) do
    q =
      Enum.filter(acc, fn {to, _v, _f, _s} -> to == mid end)
      |> Enum.map(fn {_t, v, _f, _s} -> v end)

    acc =
      Enum.map(acc, fn t = {to, v, f, s} ->
        case Enum.member?(q, v) do
          true -> {to, v, f, s + 1}
          false -> t
        end
      end)

    throws =
      for item <- items ++ q do
        wl = f.(item, a) |> div(3)

        case rem(wl, test) do
          0 -> {pass, wl, mid, 0}
          _ -> {fail, wl, mid, 0}
        end
      end

    throws ++ acc
  end

  def receive_items({throws, monkeys}) do
    Enum.map(monkeys, fn monkey = %{id: mid, count: count} ->
      c =
        Enum.filter(throws, fn {_to, _v, from, _} -> from == mid end)
        |> Enum.count()

      %{
        monkey
        | items:
            throws
            |> Enum.filter(fn {to, _v, _from, s} -> s < 1 and to == mid end)
            |> Enum.map(fn {_t, v, _f, _s} -> v end),
          count: count + c
      }
    end)
  end

  def investigate(monkeys) do
    Enum.map(monkeys, fn %{id: id, count: count, items: items} ->
      {
        id,
        count,
        items
      }
    end)
    |> IO.inspect()

    monkeys
  end
end
