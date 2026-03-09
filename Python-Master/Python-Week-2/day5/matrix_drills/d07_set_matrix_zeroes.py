# Drill 7: Set Matrix Zeroes
# In place boolean markers (O(1) space)

def set_zeroes(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    row_zero = False
    
    # 1. Determine which rows/cols need to be zero
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    row_zero = True
                    
    # 2. Zero out based on markers (skip first row/col for now)
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
                
    # 3. Zero out first col if needed
    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0
            
    # 4. Zero out first row if needed
    if row_zero:
        for c in range(COLS):
            matrix[0][c] = 0
