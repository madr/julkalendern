defmodule Solution do
  @callback parse!(String.t()) :: Any
  @callback get_name() :: String.t()
  @callback solve(Any) :: String.t()
  @callback solve_again(Any) :: String.t()
end
