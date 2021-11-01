defmodule Day02 do
  defp parse(data) do
    data
    |> String.split("\n", trim: true)
    |> Enum.map(&String.trim/1)
  end

  def countn(data, n) do
    data
    |> Enum.filter(fn s -> MapSet.size(MapSet.new(String.to_charlist(s))) != String.length(s) - n + 1 end)
    |> Enum.count
  end

  def solve(data) do
    parsed = data
      |> parse
    f2 = parsed
      |> countn(2)
    f3 = parsed
      |> countn(3)
    f2 * f3
  end

  def solve_again(data) do
    data
    |> parse
  end

  def show do
    data = File.read!("data/02.in")
    :timer.tc(fn -> solve(data) end)
    |> elem(0)
    |> Kernel./(1_000_000)
    |> IO.inspect
    :timer.tc(fn -> solve_again(data) end)
    |> elem(0)
    |> Kernel./(1_000_000)
    |> IO.inspect
  end
end
