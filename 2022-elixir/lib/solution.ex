defmodule Solution do
  @callback parse!(String.t()) :: Any
  @callback get_name() :: String.t()
  @callback solve(Any) :: String.t()
  @callback solve_again(Any) :: String.t()
  @callback present(Any) :: String.t()
  @callback present_again(Any) :: String.t()
end
