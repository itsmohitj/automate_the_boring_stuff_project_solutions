#Character Picture Grid

def charPictureGrid(grid):
    result = ""
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if j == len(grid) - 1:
                result += grid[j][i] + "\n"
            else:
                result += grid[j][i]
    return result



grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]



print(charPictureGrid(grid))