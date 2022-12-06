defmodule Day06Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day06
  import Aoc.Solution.Day06

  @input [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
  ]

  test "06: Tuning Trouble, part 1" do
    [input_a, input_b, input_c, input_d, input_e] = @input

    result_a = input_a |> parse!() |> solve()
    result_b = input_b |> parse!() |> solve()
    result_c = input_c |> parse!() |> solve()
    result_d = input_d |> parse!() |> solve()
    result_e = input_e |> parse!() |> solve()

    assert result_a == 7
    assert result_b == 5
    assert result_c == 6
    assert result_d == 10
    assert result_e == 11
  end

  test "06: Tuning Trouble, part 2" do
    [input_a, input_b, input_c, input_d, input_e] = @input

    result_a = input_a |> parse!() |> solve_again()
    result_b = input_b |> parse!() |> solve_again()
    result_c = input_c |> parse!() |> solve_again()
    result_d = input_d |> parse!() |> solve_again()
    result_e = input_e |> parse!() |> solve_again()

    assert result_a == 19
    assert result_b == 23
    assert result_c == 23
    assert result_d == 29
    assert result_e == 26
  end
end
