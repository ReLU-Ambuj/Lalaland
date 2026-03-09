# Python Array (List) Memory Model

Understanding how Python lists actually work in memory will help you grasp why certain operations are fast ($O(1)$) and others are slow ($O(N)$).

## Python Lists are Dynamic Arrays
In languages like C, a standard array is a continuous block of memory of a fixed size. If you want a bigger array, you have to allocate a whole new block, copy everything over, and free the old one.

Python `list` objects are **Dynamic Arrays**. This means:
1.  **Contiguous Memory**: Elements (technically, pointers to objects) are stored next to each other in memory.
2.  **Over-allocation**: Python allocates more memory than it strictly needs right now. If you append an item and there's room in the "over-allocated" space, it's an $O(1)$ operation.
3.  **Resizing**: When the array is completely full and you try to append `(N+1)`, Python creates a *new*, significantly larger array elsewhere in memory, copies all $N$ elements over, adds the new element, and destroys the old array.
    *   This single copy operation takes $O(N)$ time.
    *   However, because it happens infrequently (due to over-allocation expanding geometrically), we say that `append()` has an **Amortized $O(1)$** time complexity.

## Time Complexities of Common Operations

| Operation | Syntax | Time Complexity | Note |
| :--- | :--- | :--- | :--- |
| **Index Access** | `arr[i]` | $O(1)$ | Direct memory access via offset |
| **Length** | `len(arr)` | $O(1)$ | Python stores the length as a property |
| **Append** | `arr.append(x)` | $O(1)$ Amortized | Adds to the end |
| **Pop (End)** | `arr.pop()` | $O(1)$ | Removes from the end |
| **Pop (Index)** | `arr.pop(i)` | $O(N)$ | Elements after `i` must shift left |
| **Insert** | `arr.insert(i, x)`| $O(N)$ | Elements after `i` must shift right |
| **Remove Value**| `arr.remove(x)` | $O(N)$ | Searches for `x`, then shifts elements |
| **Containment** | `x in arr` | $O(N)$ | Linear scan |

## Why Two Pointers?
Because insertions (`insert(0, x)`) and deletions (`pop(0)`) at the *beginning* or *middle* of an array force every subsequent element to physically shift in memory ($O(N)$). 

If you do this in a loop ($N$ times), you suddenly have an **$O(N^2)$ algorithm**.

The **Two-Pointer technique** actively avoids inserting or deleting. Instead, it **swaps** or **overwrites** elements in-place using indices, which are $O(1)$ operations, keeping the total time down to $O(N)$.
