# Matrix Coordinate Geometry

## Standard Representation
A matrix in Python is typically represented as a List of Lists.
```python
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

## Dimensions
- **Rows**: `R = len(matrix)`
- **Columns**: `C = len(matrix[0])` if `R > 0`

## Directions/Neighbor Offsets
When performing BFS/DFS or just checking neighbors, use a `directions` array.
```python
# (row_offset, col_offset)
directions = [
    (-1, 0), # Up
    (1, 0),  # Down
    (0, -1), # Left
    (0, 1)   # Right
]

# 8-directional (includes diagonals)
dirs_8 = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
```

## Indexing
Value at row `r` and column `c` is `matrix[r][c]`.
Remember: First bracket is Y-axis (top to bottom), second bracket is X-axis (left to right).
