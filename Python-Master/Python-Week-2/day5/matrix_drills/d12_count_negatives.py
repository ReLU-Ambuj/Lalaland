# Drill 12: Count Negatives in Sorted Matrix

def count_negatives(grid):
    ROWS, COLS = len(grid), len(grid[0])
    
    count = 0
    # Process from top-right
    r, c = 0, COLS - 1
    
    while r < ROWS and c >= 0:
        if grid[r][c] < 0:
            count += (ROWS - r)
            c -= 1
        else:
            r += 1
            
    return count

if __name__ == "__main__":
    print(count_negatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])) # Expected: 8
