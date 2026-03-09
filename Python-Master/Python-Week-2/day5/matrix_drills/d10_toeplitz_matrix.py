# Drill 10: Toeplitz Matrix
# Every diagonal from top-left to bottom-right has the same elements.

def is_toeplitz_matrix(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[r][c] != matrix[r - 1][c - 1]:
                return False
                
    return True

if __name__ == "__main__":
    print(is_toeplitz_matrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])) # Expected: True
