# Drill 15: Matrix Cells in Distance Order

def all_cells_dist_order(rows, cols, rCenter, cCenter):
    cells = []
    for r in range(rows):
        for c in range(cols):
            cells.append([r, c])
            
    # Key function calculates Manhattan distance
    cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
    
    return cells

if __name__ == "__main__":
    print(all_cells_dist_order(2, 2, 0, 1)) # Expected: [[0, 1], [0, 0], [1, 1], [1, 0]]
