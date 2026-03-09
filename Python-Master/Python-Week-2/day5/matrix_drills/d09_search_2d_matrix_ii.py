# Drill 9: Search a 2D Matrix II (Rows/Cols sorted independently)
# O(M + N) traversal from top-right or bottom-left corner

def search_matrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])
    
    # Start at top-right
    r, c = 0, COLS - 1
    
    while r < ROWS and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1 # target must be to the left
        else:
            r += 1 # target must be below
            
    return False

if __name__ == "__main__":
    mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    print(search_matrix(mat, 5)) # Expected: True
