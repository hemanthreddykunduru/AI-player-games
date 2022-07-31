import numpy as np
grid=[
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]]
# assuming of rows and columns ans initating the 0 as numbers
# substitute the given sudoko problem in the place of "0's" blank places as 0
def possible(row, column, number):
    global grid
#taking the x and y directionas i and j vectors i=rows,j=columns
    for i in range (0,9):
        if grid[row][i] == number:
            return False
    for i in range(0,9):
        if grid[i][column] == number:
            return False

    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False
    return True
def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return
    print(np.matrix(grid))
    input("that's the solution")
solve()
