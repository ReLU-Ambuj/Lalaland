# The Monotonic Stack Pattern
## When to use:
When you need to find the "next strictly greater/smaller element" for every element in an array.

## Core logic:
1. Iterate through the array.
2. While the current element is *greater* than the element at the index sitting on top of the stack:
   - Pop the stack.
   - You have found the "next greater element" for the popped index!
3. Push the current index onto the stack.
