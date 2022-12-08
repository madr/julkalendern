defmodule Day07Test do
  use ExUnit.Case
  doctest Aoc.Solution.Day07
  import Aoc.Solution.Day07

  @input ~s(
    $ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
  )

  test "07: No Space Left On Device, part 1" do
    expected = 95437

    result = @input |> parse!() |> solve()

    assert result == expected
  end

  test "07: No Space Left On Device, part 2" do
    expected = 24_933_642

    result = @input |> parse!() |> solve_again()

    assert result == expected
  end
end
