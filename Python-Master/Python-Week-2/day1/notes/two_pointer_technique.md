# Two-Pointer Technique

The **Two-Pointer technique** is a fundamental algorithmic pattern used heavily in array and string problems. It dramatically reduces the time complexity of many solutions, often turning $O(N^2)$ (quadratic) algorithms into $O(N)$ (linear) ones with just $O(1)$ space.

## Core Idea
Instead of using nested loops to compare elements (which creates $O(N^2)$ paths), you use two integer variables that act as indices (or "pointers") pointing to different elements within an array. You then move these pointers relative to each other based on specific conditions.

## Two Main Patterns

### 1. Opposite Direction (Inward Traversal)
*   **Initial State**: `left = 0`, `right = len(arr) - 1`
*   **Termination**: Typically `while left < right`
*   **Use Cases**:
    *   Reversing an array (`d01_reverse_array.py`)
    *   Finding a pair that sums to a target in a **sorted** array (`d02_two_sum_sorted.py`)
    *   Comparing elements from opposing ends (Checking palindromes)

*   **Example (Two Sum Sorted)**:
    If the current sum is smaller than the target, you *increase* the lower bound (`left += 1`). If the current sum is larger, you *decrease* the upper bound (`right -= 1`).

### 2. Same Direction (Sliding Window / Fast & Slow Pointers)
*   **Initial State**: Both start at index 0 (or `slow = 0`, `fast = 1`)
*   **Termination**: Typically when the `fast` pointer reaches the end of the array.
*   **Use Cases**:
    *   Removing duplicates or target values in-place (`d03_remove_duplicates.py`, `d04_remove_element.py`)
    *   Moving specific items to the end (`d05_move_zeroes.py`)
    *   Cycle detection (Floyd's algorithm - commonly linked lists, but sometimes conceptually in arrays)
    *   Finding pairs with a specific difference (`d13_pair_difference.py`)

*   **Example (Remove Duplicates)**:
    The `slow` pointer keeps track of where to write the *next* valid element. The `fast` pointer scans ahead to find elements that satisfy the condition (e.g., they are different from the last element written by `slow`).

## Important Gotchas
*   **Sorted vs. Unsorted**: Many two-pointer strategies (specifically the *Opposite Direction* pattern for sum/difference problems) rely heavily on the input array being **sorted**. If the array is unsorted, you might need to sort it first ($O(N \log N)$), or use a Hash Map instead ($O(N)$ time & space, which we cover later).
*   **Off-by-One Errors**: Be meticulous with your array bounds. Always test with empty arrays, single-element arrays, and arrays with even/odd lengths.
*   **While Loops**: Notice that `while left < right` will stop *before* the pointers overlap. Sometimes you might need `while left <= right` depending on the logic (like binary search).
