defmodule Aoc.Solution.Day05 do
  @name "Day 5: Doesn't He Have Intern-Elves For This?"
  @behaviour Solution

  @impl Solution
  def get_name, do: @name

  @impl Solution
  def parse!(raw) do
    raw
    |> String.split()
  end

  @impl Solution
  def solve_first_part(strings) do
    strings
    |> Enum.map(fn s -> nice?(s) end)
    |> Enum.map(fn b ->
      if b, do: 1, else: 0
    end)
    |> Enum.sum()
  end

  @impl Solution
  def solve_second_part(strings) do
    strings
    |> Enum.map(fn s -> still_nice?(s) end)
    |> Enum.map(fn b ->
      if b, do: 1, else: 0
    end)
    |> Enum.sum()
  end

  defp nice?(subject) do
    Enum.all?([
      does_not_contain_the_strings(subject),
      contains_at_least_three_vowels(subject),
      contains_at_least_one_letter_pair(subject)
    ])
  end

  defp still_nice?(subject) do
    Enum.all?([
      contains_a_letter_pair_without_overlapping(subject),
      contains_one_letter_pair_which_repeats_with_exactly_one_letter_between_them(subject)
    ])
  end

  defp contains_at_least_three_vowels(subject) do
    r = ~r/[aeiou].*[aeiou].*[aeiou].*/
    String.match?(subject, r)
  end

  defp contains_at_least_one_letter_pair(subject) do
    r = ~r/(\w)\1/
    String.match?(subject, r)
  end

  defp does_not_contain_the_strings(subject) do
    r = ~r/ab|cd|pq|xy/
    not String.match?(subject, r)
  end

  defp contains_a_letter_pair_without_overlapping(subject) do
    r = ~r/(\w{2}).*\1/
    String.match?(subject, r)
  end

  defp contains_one_letter_pair_which_repeats_with_exactly_one_letter_between_them(subject) do
    r = ~r/(\w)\w\1/
    String.match?(subject, r)
  end
end
