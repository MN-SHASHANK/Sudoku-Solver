GRID_SIZE = 9

def display_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))
    print()

def can_place_number(grid, row, col, num):
    # Check the row
    for x in range(GRID_SIZE):
        if grid[row][x] == num:
            return False
    
    # Check the column
    for x in range(GRID_SIZE):
        if grid[x][col] == num:
            return False

    # Check the 3x3 sub-grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(grid, row=0, col=0):
    if row == GRID_SIZE - 1 and col == GRID_SIZE:
        return True
    if col == GRID_SIZE:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)

    for num in range(1, GRID_SIZE + 1):
        if can_place_number(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0  # Backtrack
    return False

# Initial grid with zeros representing empty cells
sudoku_grid = [
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]
]

if solve_sudoku(sudoku_grid):
    display_grid(sudoku_grid)
else:
    print("No solution exists.")
