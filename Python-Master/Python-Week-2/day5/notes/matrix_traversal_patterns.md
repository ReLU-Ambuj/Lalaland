# Matrix Traversal Patterns

## 1. Row-by-Row (Standard)
```python
for r in range(ROWS):
    for c in range(COLS):
        print(matrix[r][c])
```

## 2. Column-by-Column
```python
for c in range(COLS):
    for r in range(ROWS):
        print(matrix[r][c])
```

## 3. Boundary Checking Function
Always define a helper to avoid `IndexError`.
```python
def is_valid(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS
```

## 4. Main and Anti Diagonals
For a square matrix (N x N):
- **Main Diagonal**: Elements where `r == c`
- **Anti Diagonal**: Elements where `r + c == N - 1`
