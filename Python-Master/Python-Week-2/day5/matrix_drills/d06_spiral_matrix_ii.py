# Drill 6: Spiral Matrix II
# Generate an N x N matrix filled with elements from 1 to N^2 in spiral order

def generate_matrix(n):
    mat = [[0] * n for _ in range(n)]
    left, right = 0, n
    top, bottom = 0, n
    val = 1
    
    while left < right and top < bottom:
        for i in range(left, right):
            mat[top][i] = val
            val += 1
        top += 1
        
        for i in range(top, bottom):
            mat[i][right - 1] = val
            val += 1
        right -= 1
        
        if not (left < right and top < bottom):
            break
            
        for i in range(right - 1, left - 1, -1):
            mat[bottom - 1][i] = val
            val += 1
        bottom -= 1
        
        for i in range(bottom - 1, top - 1, -1):
            mat[i][left] = val
            val += 1
        left += 1
        
    return mat

if __name__ == "__main__":
    print(generate_matrix(3))
    # Expected: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
