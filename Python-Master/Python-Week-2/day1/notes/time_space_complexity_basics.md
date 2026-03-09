# Time and Space Complexity Basics

When dealing with Data Structures and Algorithms, we use **Big-O Notation** to describe the performance or complexity of an algorithm. It describes the worst-case scenario.

## Time Complexity ($O(T)$)
How does the runtime of the algorithm grow as the input size ($N$) grows?

* **$O(1)$ - Constant Time**: The operation takes the same amount of time regardless of the input size.
  * *Example*: Accessing an array element by index (`arr[5]`).
* **$O(\log N)$ - Logarithmic Time**: The operation time goes up linearly while the $N$ goes up exponentially. Usually found when you cut the problem size in half each step.
  * *Example*: Binary Search.
* **$O(N)$ - Linear Time**: The runtime grows directly in proportion to the input size. Let's say it takes 1 second to process 10 items; it will take 10 seconds to process 100 items. 
  * *Example*: Iterating through an array once.
* **$O(N \log N)$ - Linearithmic Time**: 
  * *Example*: Efficient sorting algorithms (Merge Sort, Quick Sort, Timsort - Python's built-in `sort()`).
* **$O(N^2)$ - Quadratic Time**: The runtime grows proportional to the square of the input size. If the input size doubles, the runtime quadruples.
  * *Example*: Nested loops iterating over an array.

## Space Complexity ($O(S)$)
How much *extra* memory does the algorithm need, apart from the input data, as the input size ($N$) grows?

* **$O(1)$ - Constant Space**: The algorithm requires a fixed amount of extra space, regardless of the input size. This is what we call an **"in-place"** algorithm.
  * *Example*: The Two-Pointer technique for reversing an array uses just two integer variables.
* **$O(N)$ - Linear Space**: The extra space required grows linearly with the input size.
  * *Example*: Creating a copy of an array or returning a new array of the same size as the input.

## Golden Rules for Arrays
1. **Always check if you can do it in-place!** If the problem asks for constant extra space ($O(1)$), you probably need pointers, swapping, or storing multiple values in a single element.
2. **If sorting is allowed**, it will take $O(N \log N)$ time but might reduce later logic from $O(N^2)$ down to $O(N)$.
