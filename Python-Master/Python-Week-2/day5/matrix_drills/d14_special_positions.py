# Drill 14: Special Positions in a Binary Matrix

def num_special(mat):
    ROWS = len(mat)
    COLS = len(mat[0])
    
    row_sums = [sum(row) for row in mat]
    col_sums = [sum(mat[r][c] for r in range(ROWS)) for c in range(COLS)]
    
    special = 0
    for r in range(ROWS):
        for c in range(COLS):
            if mat[r][c] == 1 and row_sums[r] == 1 and col_sums[c] == 1:
                special += 1
                
    return special

if __name__ == "__main__":
    print(num_special([[1,0,0],[0,0,1],[1,0,0]])) # Expected: 1
