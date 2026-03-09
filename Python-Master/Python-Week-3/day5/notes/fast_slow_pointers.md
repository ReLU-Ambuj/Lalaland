# Fast and Slow Pointers

## Finding the Middle
Initialize `slow = head` and `fast = head`.
Move `slow` by 1 step, and `fast` by 2 steps.
When `fast` reaches the end (or `fast.next` is None), `slow` will be exactly at the middle.

## Cycle Detection (Floyd's Algorithm)
If there is a cycle, the `fast` pointer will eventually "lap" the `slow` pointer inside the cycle.
`if fast == slow: return True`
