# Drill 8: Search a 2D Matrix (Strictly Sorted)
# Treat 2D matrix as a flat 1D array.

def search_matrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])
    
    low, high = 0, ROWS * COLS - 1
    
    while low <= high:
        mid = (low + high) // 2
        # Convert 1D index to 2D coordinates
        r = mid // COLS
        c = mid % COLS
        
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return False

if __name__ == "__main__":
    print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # Expected: True
