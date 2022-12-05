defmodule Aoc.Solution.Day05 do
  import Aoc.Utils

  @name "Day 5: Supply Stacks"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def present(solution), do: "On 9000, top crate on each stack is #{solution}"

  @impl Solution
  def present_again(solution), do: "On 9001, top crate on each stack is #{solution}"

  @impl Solution
  def parse!(raw) do
    [initial_state, instructions] = raw |> String.split("\n\n")

    {
      initial_state |> String.split("\n") |> Enum.drop(-1) |> parse_state(),
      instructions |> String.trim() |> split_lines() |> parse_instructions()
    }
  end

  @impl Solution
  def solve({state, instructions}) do
    state
    |> move(instructions, 9000)
    |> topmost()
  end

  @impl Solution
  def solve_again({state, instructions}) do
    state
    |> move(instructions, 9001)
    |> topmost()
  end

  def parse_state(state) do
    blank = "[-]"
    len = Enum.map(state, &String.length/1) |> Enum.max()

    Enum.map(state, fn line ->
      line
      |> String.pad_trailing(len)
      |> String.pad_leading(len + 1)
      |> String.replace("    ", " #{blank}")
    end)
    |> Enum.map(fn l ->
      l
      |> String.trim()
      |> String.split()
    end)
    |> Enum.zip()
    |> Enum.map(fn t ->
      t
      |> Tuple.to_list()
      |> Enum.reject(fn v -> v == blank end)
      |> Enum.map(fn v ->
        v
        |> String.slice(1..-2)
      end)
    end)
  end

  def parse_instructions(lines) do
    Enum.map(lines, fn "move " <> line ->
      [steps, _f, from, _t, to] = String.split(line)
      Enum.map([steps, from, to], &String.to_integer/1)
    end)
  end

  def move(state, [], _), do: state

  def move(state, [[n, from, to] | remaining], model) do
    move(
      case model do
        9000 -> _move_9000(state, from - 1, to - 1, n)
        9001 -> _move_9001(state, from - 1, to - 1, n)
      end,
      remaining,
      model
    )
  end

  def _move_9001(state, from, to, n) do
    {pre, rem} = state |> Enum.at(from) |> Enum.split(n)

    state
    |> List.update_at(from, fn _ -> rem end)
    |> List.update_at(to, fn l -> pre ++ l end)
  end

  def _move_9000(state, _from, _to, 0) do
    state
  end

  def _move_9000(state, from, to, n) do
    case Enum.at(state, from) do
      [a | rem] ->
        _move_9000(
          state
          |> List.update_at(from, fn _ -> rem end)
          |> List.update_at(to, fn l -> [a | l] end),
          from,
          to,
          n - 1
        )

      [] ->
        state

      nil ->
        state
    end
  end

  def topmost(state) do
    state |> Enum.map(&List.first/1) |> Enum.join("")
  end
end
