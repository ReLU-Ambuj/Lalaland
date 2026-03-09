# Drill 2: Matrix Diagonal Sum
# Sum main and anti diagonals. Do not double count the center if N is odd.

def diagonal_sum(mat):
    n = len(mat)
    total = 0
    
    for i in range(n):
        total += mat[i][i] # Primary
        total += mat[i][n - 1 - i] # Secondary
        
    if n % 2 == 1:
        total -= mat[n // 2][n // 2]
        
    return total

if __name__ == "__main__":
    print(diagonal_sum([[1,2,3], [4,5,6], [7,8,9]])) # Expected: 25
