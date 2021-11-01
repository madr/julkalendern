defmodule Aoc19.Solution.Day08 do
  @name "Day 8: Space Image Format"
  @behaviour Solution
  @image_width 25
  @image_height 6
  @black " "
  @white "X"

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def parse!(str), do: str

  @impl Solution
  @doc """
  Solution for the first part of "Day 8: Space Image Format".
  """
  def solve_first_part(data), do: data |> _solve_first_part(@image_width, @image_height)

  @impl Solution
  @doc """
  Solution for the second part of "Day 8: Space Image Format".
  """
  def solve_second_part(data) do
    data |> _solve_second_part(@image_width, @image_height) |> reveal(@image_width)
  end

  @doc """
  Actual solution for part 1, but with the ability to test.

  ## Examples

      iex> Aoc19.Solution.Day08._solve_first_part("123456789012", 3, 2)
      1

  """
  def _solve_first_part(data, image_width, image_height) do
    data
    |> layers(image_width, image_height)
    |> fewest_zeros
    |> multiply()
  end

  @doc """
  Actual solution for part 2, but with the ability to test.

  ## Examples

      iex> Aoc19.Solution.Day08._solve_second_part("0222112222120000", 2, 2)
      [" ", "X", "X", " "]

  """
  def _solve_second_part(data, image_width, image_height) do
    data
    |> layers(image_width, image_height)
    |> pixels()
    |> colors
  end

  @doc """
  get layers from image data.

  ## Examples

      iex> Aoc19.Solution.Day08.layers("123456789012", 3, 2)
      ["123456", "789012"]

      iex> Aoc19.Solution.Day08.layers("0222112222120000", 2, 2)
      ["0222", "1122", "2212", "0000"]

  """
  def layers(data, x, y) do
    data
    |> String.codepoints()
    |> Enum.chunk_every(x * y)
    |> Enum.map(&Enum.join/1)
  end

  @doc """
  Get layers with the fewest zeros.

  ## Examples

      iex> Aoc19.Solution.Day08.fewest_zeros(["123456", "789012"])
      "123456"

      iex> Aoc19.Solution.Day08.fewest_zeros(["103406", "789012"])
      "789012"

  """
  def fewest_zeros(layers) do
    layers
    |> Enum.map(fn layer -> {layer, layer} end)
    |> Enum.map(fn {layer, data} ->
      {layer, data |> String.replace("0", "") |> String.length()}
    end)
    |> Enum.sort(fn a, b -> elem(a, 1) > elem(b, 1) end)
    |> Enum.at(0)
    |> elem(0)
  end

  @doc """
  return the number of 1 digits multiplied by the number of 2 digits of a layer.

  ## Examples

      iex> Aoc19.Solution.Day08.multiply("121226")
      6

      iex> Aoc19.Solution.Day08.multiply("293416")
      1

  """
  def multiply(layer) do
    {x, y} =
      layer
      |> String.codepoints()
      |> Enum.map(&String.to_integer/1)
      |> Enum.reduce({0, 0}, fn
        1, {x, y} -> {x + 1, y}
        2, {x, y} -> {x, y + 1}
        _, acc -> acc
      end)

    x * y
  end

  @doc """
  Regroup a set of layers to pixels.

  ## Examples

      iex> Aoc19.Solution.Day08.pixels(["0222", "1122", "2212", "0000"])
      [[0, 1, 2, 0], [2, 1, 2, 0], [2, 2, 1, 0], [2, 2, 2, 0]]

      iex> Aoc19.Solution.Day08.pixels(["123456", "789012"])
      [[1, 7], [2, 8], [3, 9], [4, 0], [5, 1], [6, 2]]

  """
  def pixels(_layers, {count, _depth}, pixels, pos) when pos > count,
    do: pixels |> Enum.reverse()

  def pixels(layers, {count, depth}, pixels, pos) do
    pixel =
      0..depth
      |> Enum.map(fn layer ->
        layers
        |> Enum.at(layer)
        |> Enum.at(pos)
        |> String.to_integer()
      end)

    pixels(layers, {count, depth}, [pixel | pixels], pos + 1)
  end

  def pixels(layers) do
    count = layers |> Enum.at(0) |> String.length()
    depth = layers |> length

    pixels(
      layers |> Enum.map(&String.codepoints/1),
      {count - 1, depth - 1},
      [],
      0
    )
  end

  def colors(pixels) do
    pixels
    |> Enum.map(&color/1)
  end

  @doc """
  determine color of pixel based on layer.

  ## Examples

      iex> Aoc19.Solution.Day08.color([0, 1, 2, 0])
      " "

      iex> Aoc19.Solution.Day08.color([2, 1, 2, 0])
      "X"

      iex> Aoc19.Solution.Day08.color([2, 2, 1, 0])
      "X"

      iex> Aoc19.Solution.Day08.color([2, 2, 2, 0])
      " "

      iex> Aoc19.Solution.Day08.color([2, 2, 2, 2, 1, 2, 2, 0])
      "X"

  """
  def color([2 | queue]), do: color(queue)
  def color([1 | _]), do: @white
  def color([0 | _]), do: @black

  @doc """
  determine color of pixel based on layer.

  ## Examples

      iex> Aoc19.Solution.Day08.reveal(["X", " ", " ", "X"], 2)
      "\\nX \\n X"

  """
  def reveal(pixels, breakpoint) do
    output =
      pixels
      |> Enum.chunk_every(breakpoint)
      |> Enum.map(&Enum.join/1)
      |> Enum.join("\n")

    "\n" <> output
  end
end
