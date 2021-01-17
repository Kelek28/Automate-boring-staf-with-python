# Chapter 4
# Project: Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def printGrid(grid):
    for column in range(len(grid[0])):
        for row in range(len(grid)):
            print(grid[row][column], end=" ")
            if(row == 8):
                print('\n')
                break

printGrid(grid)
# function returns 
# . . O O . O O . .

# . O O O O O O O .

# . O O O O O O O .

# . . O O O O O . .

# . . . O O O . . .

# . . . . O . . . .
# from grid