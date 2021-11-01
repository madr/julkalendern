defmodule Day01 do
  defp find_recurring(data) do
    Enum.reduce_while(data, {0, MapSet.new([0])}, fn term, {prev, known} ->
      freq = prev + term
      if MapSet.member?(known, freq) do
        {:halt, freq}
      else
        {:cont, {freq, MapSet.put(known, freq)}}
      end
    end)
  end

  defp parse(data) do
    String.split(data, "\n")
      |> Enum.map(&String.trim/1)
      |> Enum.map(&String.to_integer/1)
  end

  def solve(data) do
    data
    |> parse
    |> Enum.sum
  end

  def solve_again(data) do
    data
    |> parse
    |> Stream.cycle
    |> find_recurring
  end

  def show do
    data = File.read!("data/01.in")
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
Day01.show()