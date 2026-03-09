# Deque Internals
`collections.deque` is a doubly-linked list under the hood (technically an array of unrolled doubly linked blocks).
- `append(x)`: $O(1)$
- `appendleft(x)`: $O(1)$
- `pop()`: $O(1)$
- `popleft()`: $O(1)$

Always import it: `from collections import deque`
