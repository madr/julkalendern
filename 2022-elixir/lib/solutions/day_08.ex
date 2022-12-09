defmodule Aoc.Solution.Day08 do
  import Aoc.Utils

  @name "Day 8: Treetop Tree House"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def present(solution), do: "#{solution} trees are visible"

  @impl Solution
  def present_again(solution), do: "Highest scenic score possible is #{solution}"

  @impl Solution
  def parse!(raw) do
    raw
    |> split_lines()
    |> Enum.map(fn line -> String.codepoints(line) |> Enum.map(&String.to_integer/1) end)
  end

  @impl Solution
  def solve(map) do
    find_visible(map)
  end

  @impl Solution
  def solve_again(map) do
    scenic_scores(map)
    |> MapSet.to_list()
    |> Enum.max()
  end

  def find_visible(map) do
    {h, w} = _map_size(map)
    count_visibles(map, 0, 0, h, w, 0)
  end

  def count_visibles(_map, y, _x, h, _w, count) when y == h do
    count
  end

  def count_visibles(map, y, x, h, w, count) when x == w do
    count_visibles(map, y + 1, 0, h, w, count)
  end

  def count_visibles(map, y, x, h, w, count) do
    if visible?(map, y, x, h, w) do
      count_visibles(map, y, x + 1, h, w, count + 1)
    else
      if Enum.zip(map) |> Enum.map(&Tuple.to_list/1) |> visible?(x, y, w, h) do
        count_visibles(map, y, x + 1, h, w, count + 1)
      else
        count_visibles(map, y, x + 1, h, w, count)
      end
    end
  end

  def visible?(_map, y, _x, _h, _w) when y == 0 do
    true
  end

  def visible?(_map, y, _x, h, _w) when y == h - 1 do
    true
  end

  def visible?(_map, _y, x, _h, _w) when x == 0 do
    true
  end

  def visible?(_map, _y, x, _h, w) when x == w - 1 do
    true
  end

  def visible?(map, y, x, _h, _w) do
    value = Enum.at(map, y) |> Enum.at(x)
    {l, r} = Enum.at(map, y) |> Enum.split(x)
    r = Enum.drop(r, 1)

    Enum.max(l) < value or Enum.max(r) < value
  end

  def scenic_scores(map) do
    {h, w} = _map_size(map)

    scenic_score(map, Enum.zip(map) |> Enum.map(&Tuple.to_list/1), 0, 0, h, w, MapSet.new())
  end

  def scenic_score(_lr_map, _tb_map, y, _x, h, _w, scores) when y == h do
    scores
  end

  def scenic_score(lr_map, tb_map, y, x, h, w, scores) when x == w do
    scenic_score(lr_map, tb_map, y + 1, 0, h, w, scores)
  end

  def scenic_score(lr_map, tb_map, y = 0, x, h, w, scores) do
    zero_score(lr_map, tb_map, y, x, h, w, scores)
  end

  def scenic_score(lr_map, tb_map, y, x = 0, h, w, scores) do
    zero_score(lr_map, tb_map, y, x, h, w, scores)
  end

  def scenic_score(lr_map, tb_map, y, x, h, w, scores) when x == w - 1 do
    zero_score(lr_map, tb_map, y, x, h, w, scores)
  end

  def scenic_score(lr_map, tb_map, y, x, h, w, scores) when y == h - 1 do
    zero_score(lr_map, tb_map, y, x, h, w, scores)
  end

  def scenic_score(lr_map, tb_map, y, x, h, w, scores) do
    value = Enum.at(lr_map, y) |> Enum.at(x)

    {l, r} = lr(lr_map, y, x)
    {t, b} = lr(tb_map, x, y)

    %{pos: {y, x}, value: value}

    score =
      [t, r, b, l]
      |> Enum.map(fn trbl -> view_distance(trbl, value) end)
      |> Enum.product()

    scenic_score(lr_map, tb_map, y, x + 1, h, w, MapSet.put(scores, score))
  end

  def zero_score(lr_map, tb_map, y, x, h, w, scores) do
    scenic_score(lr_map, tb_map, y, x + 1, h, w, MapSet.put(scores, 0))
  end

  def lr(map, y, x) do
    {l, r} = Enum.at(map, y) |> Enum.split(x)
    {Enum.reverse(l), Enum.drop(r, 1)}
  end

  def _map_size(map) do
    h = Enum.count(map)
    w = List.first(map) |> Enum.count()

    {h, w}
  end

  @doc """
  Calculate the trees that can be seen in a given direction.

  ## Examples

      iex> Aoc.Solution.Day08.view_distance([3], 5)
      1
      iex> Aoc.Solution.Day08.view_distance([5, 2], 5)
      1
      iex> Aoc.Solution.Day08.view_distance([1, 2], 5)
      2
      iex> Aoc.Solution.Day08.view_distance([3, 5, 3], 5)
      2
      iex> Aoc.Solution.Day08.view_distance([3, 3], 5)
      2
      iex> Aoc.Solution.Day08.view_distance([4, 9], 5)
      2

  """
  def view_distance(list, value, count \\ 0)

  def view_distance([], _value, count) do
    count
  end

  def view_distance([nearest | _beyond], value, count) when value <= nearest do
    count + 1
  end

  def view_distance([_nearest | beyond], value, count) do
    view_distance(beyond, value, count + 1)
  end
end
