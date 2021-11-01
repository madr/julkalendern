defmodule Day01Test do
  use ExUnit.Case
  doctest Day01

  test "adjust frequency" do
    assert Day01.solve("+1\n+1\n+1") == 3
    assert Day01.solve("+1\n+1\n-2") == 0
    assert Day01.solve("-1\n-2\n-3") == -6
  end

  test "finds recurring frequency" do
    assert Day01.solve_again("+1\n-1") == 0
    assert Day01.solve_again("+3\n+3\n+4\n-2\n-4") == 10
    assert Day01.solve_again("-6\n+3\n+8\n+5\n-6") == 5
    assert Day01.solve_again("+7\n+7\n-2\n-7\n-4") == 14
  end
end
