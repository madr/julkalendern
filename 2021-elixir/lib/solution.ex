defmodule Solution do
  @callback parse!(String.t()) :: Any
  @callback get_name() :: String.t()
  @callback solve_first_part(Any) :: String.t()
  @callback solve_second_part(Any) :: String.t()
end
