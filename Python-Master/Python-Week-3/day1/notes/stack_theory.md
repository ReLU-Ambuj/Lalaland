# Stack Theory
## Array vs Stack
Why use a Stack when Arrays can do everything?
- **Intent**: Using `.append()` and `.pop()` communicates LIFO intent.
- **Safety**: Restricting operations prevents accidental mid-array modifications.
- **Complexity**: `append()` and `pop()` are `O(1)` amortized. `pop(0)` is `O(N)` and should **never** be used for a stack.
