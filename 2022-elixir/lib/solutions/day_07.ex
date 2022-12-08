defmodule Aoc.Solution.Day07 do
  import Aoc.Utils

  @name "Day 7: No Space Left On Device"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def present(solution), do: "The small directories sizes sum is #{solution} (1644735)"

  @impl Solution
  def present_again(solution), do: "The best dir to remove has a size of #{solution}"

  @impl Solution
  def parse!(raw) do
    raw |> split_lines()
  end

  @impl Solution
  def solve(output) do
    output
    |> traverse()
    |> small_dir_sum()
  end

  @impl Solution
  def solve_again(output) do
    output
    |> traverse()
    |> removal_dir()
  end

  def traverse(files) when is_list(files) do
    Enum.reduce(
      files,
      %{
        pwd: ["/"],
        tree: %{
          "/" => %{
            children: %{},
            files: []
          }
        }
      },
      &traverse/2
    )
  end

  def traverse("$ cd /", tree) do
    %{tree | pwd: ["/"]}
  end

  def traverse("$ cd ..", tree = %{pwd: path}) do
    %{tree | pwd: path |> Enum.drop(1)}
  end

  def traverse("$ cd " <> dirname, tree = %{pwd: path}) do
    %{tree | pwd: [dirname | path]}
  end

  def traverse("dir " <> dirname, state = %{pwd: pwd, tree: tree}) do
    pp = _path(pwd, :children)
    node = Map.put(get_in(tree, pp), dirname, %{children: %{}, files: []})
    %{state | tree: put_in(tree, pp, node)}
  end

  def traverse("$ ls", tree) do
    tree
  end

  def traverse(item, %{pwd: pwd, tree: tree}) do
    [size, _name] = String.split(item)
    pp = _path(pwd, :files)
    files = get_in(tree, pp)

    %{
      pwd: pwd,
      tree: put_in(tree, pp, [String.to_integer(size) | files])
    }
  end

  def _path(pwd, pos),
    do:
      [
        pos
        | pwd
          |> Enum.map(fn s -> [s, :children] end)
      ]
      |> List.flatten()
      |> Enum.drop(-1)
      |> Enum.reverse()

  def small_dir_sum(%{tree: tree}) do
    tree
    |> dir_sizes()
    |> Enum.filter(fn v -> v < 100_000 end)
    |> Enum.sum()
  end

  def removal_dir(%{tree: tree}) do
    needed = 30_000_000
    disk = 70_000_000

    dirs =
      tree
      |> dir_sizes()

    used = Enum.max(dirs)
    free = disk - used

    dirs
    |> Enum.filter(fn s -> free + s > needed end)
    |> Enum.min()
  end

  def dir_sizes(%{"/" => node}) do
    dir_sizes("/", node, [])
    |> Enum.map(fn {_k, v} -> v end)
  end

  def dir_sizes(_name, children, seen) when is_list(children) do
    sums =
      Enum.map(children, fn {name, data} ->
        dir_sizes(name, data, seen)
      end)
      |> List.flatten()

    sums ++ seen
  end

  def dir_sizes(name, data, seen) do
    size = dir_size(data)

    seen =
      case Enum.empty?(Map.get(data, :children)) do
        true -> seen
        false -> dir_sizes(name, Map.get(data, :children) |> Map.to_list(), seen)
      end

    [{name, size} | seen]
  end

  def dir_size(data) do
    size = Map.get(data, :files, []) |> Enum.sum()

    child_size =
      data
      |> Map.get(:children)
      |> Enum.map(fn {_n, d} ->
        dir_size(d)
      end)
      |> Enum.sum()

    size + child_size
  end
end
