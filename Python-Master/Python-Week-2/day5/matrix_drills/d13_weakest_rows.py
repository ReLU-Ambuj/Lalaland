# Drill 13: The K Weakest Rows in a Matrix

def k_weakest_rows(mat, k):
    # Could optimize using Binary Search to count 1s + Max Heap
    # Simple sort approach:
    row_strengths = []
    
    for i, row in enumerate(mat):
        # since 1s always appear before 0s
        # sum(row) is number of ones
        row_strengths.append((sum(row), i))
        
    row_strengths.sort() # sorted by strength, then index
    
    return [i for strength, i in row_strengths[:k]]

if __name__ == "__main__":
    mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]]
    print(k_weakest_rows(mat, 3)) # Expected: [2, 0, 3]
