sampleMatrix = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

#This functions validates the 'k' which is the value given to it that whether that satisfies the rules of sudoku
def isValid(grid, r, c, k):

    not_in_row = k not in grid[r] #checks if the given row has 'k' or not. If not value is True
    not_in_column = k not in [grid[i][c] for i in range(9)] #checks if the column has 'k' or not. If not value is True
    start_row, start_col = (r//3)*3, (c//3)*3
    not_in_box = k not in [grid[i+start_row][j+start_col] for i in range(3) for j in range(3)] #checks if the subbox has the value 'k' in it or not, If not value is True

    return not_in_row and not_in_column and not_in_box #returns True if all are True, if not returns False

def solve(grid, r=0, c=0):
    if r==9:
        return grid #All rows has been validated, return the grid
    elif c==9:
        return solve(grid, r+1, 0) #Current row has been validated, move onto the next
    elif grid[r][c]:
        return solve(grid, r, c+1) #Cell is not empty, cell already has a value so move on.
    else:
        for k in range(1,10):
            if isValid(grid, r, c, k):
                grid[r][c] = k #if satisfied with current 'k', put it in the cell and move on to the next.
                if solve(grid, r, c+1):
                    return grid #if the next cells still remain valid with our previous changes, then return the solved grid
                grid[r][c] = 0 #Set back to 0, try new value
        return False #Nothing worked, return False

def generate(difficulty):
    grid = [ [0]*9 for _ in range(9)]
    import random
    for val in range(9):
        i,j = random.choice([_ for _ in range(9)]), random.choice([_ for _ in range(9)])
        grid[i][j] = val

    grid = solve(grid)

    if difficulty == "Easy":
        empty_cells = random.choice([_ for _ in range(50, 60)])
    elif difficulty == "Medium":
        empty_cells = random.choice([_ for _ in range(60, 70)])
    elif difficulty == "Hard":
        empty_cells = random.choice([_ for _ in range(80, 90)])
    else:
        return False

    for _ in range(empty_cells):
        i,j = random.choice([_ for _ in range(9)]), random.choice([_ for _ in range(9)])
        grid[i][j] = ""

    return grid

if __name__ == '__main__':

    # generated = generate('easy')
    # if generated:
    #     print(generated)
    # else:
    #     print("Enter a valid difficulty")

    # Solve the Sudoku puzzle and update the sampleMatrix
    solution = solve(sampleMatrix)
    if solution:
        sampleMatrix = solution  # Update sampleMatrix with the solved grid
        print("Sudoku puzzle solved successfully:")
        print(sampleMatrix)
    else:
        print("No solution found for the Sudoku puzzle.")