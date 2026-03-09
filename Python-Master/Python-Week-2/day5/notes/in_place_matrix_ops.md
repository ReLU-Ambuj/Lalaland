# In-Place Matrix Operations

Many matrix problems (like Rotate Image or Set Matrix Zeroes) ask for O(1) space complexity, meaning you must modify the matrix in place.

## 1. Using Sentinels / State Encoding
If a matrix contains only positive numbers, you can encode state by making a number negative to indicate it was "visited" or "changed", then do a second pass to clean it up.

## 2. Using the First Row/Column as Storage
For "Set Matrix Zeroes", you can use the first row `matrix[0][...]` and first column `matrix[...][0]` to store boolean flags instead of creating separate `O(M) + O(N)` arrays. 
*Note: The `[0][0]` element overlaps, so you usually need one extra variable for the first row or column.*

## 3. Transpose + Reverse Rotation
To rotate an N x N matrix 90 degrees clockwise in place:
1. Transpose the matrix (swap `matrix[i][j]` with `matrix[j][i]`).
2. Reverse every row `matrix[i].reverse()`.
