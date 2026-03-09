# Drill 11: Reshape the Matrix

def matrix_reshape(mat, r, c):
    ROWS, COLS = len(mat), len(mat[0])
    if ROWS * COLS != r * c:
        return mat
        
    ans = [[0] * c for _ in range(r)]
    curr_r = 0
    curr_c = 0
    
    for i in range(ROWS):
        for j in range(COLS):
            ans[curr_r][curr_c] = mat[i][j]
            curr_c += 1
            if curr_c == c:
                curr_c = 0
                curr_r += 1
                
    return ans

if __name__ == "__main__":
    print(matrix_reshape([[1,2],[3,4]], 1, 4)) # Expected: [[1, 2, 3, 4]]
