# Drill 4: Rotate Image (N x N in-place)

def rotate(matrix):
    n = len(matrix)
    
    # 1. Transpose (swap elements across main diagonal)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # 2. Reverse each row
    for i in range(n):
        matrix[i].reverse()
        # Alternatively: matrix[i] = matrix[i][::-1]
        
if __name__ == "__main__":
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(mat)
    print(mat) # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
