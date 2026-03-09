# Drill 3: Transpose Matrix
# Note: Matrix might not be square (M x N -> N x M)

def transpose(matrix):
    R, C = len(matrix), len(matrix[0])
    
    # Create N x M matrix
    ans = [[0] * R for _ in range(C)]
    
    for r in range(R):
        for c in range(C):
            ans[c][r] = matrix[r][c]
            
    return ans

if __name__ == "__main__":
    print(transpose([[1,2,3],[4,5,6]])) # Expected: [[1, 4], [2, 5], [3, 6]]
