sudoku = [list(map(int,input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i,j))

def check(x,y,a):
    for j in range(9):
        if a == sudoku[x][j]:
            return False
        
    for i in range(9):
        if a == sudoku[i][y]:
            return False
        
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == sudoku[nx+i][ny+j]:
                return False
    return True

def bt(idx):
    global blank
    if idx == len(blank):
        for row in sudoku:
            print(*row)
        return True

    for i in range(1,10):
        x = blank[idx][0]
        y = blank[idx][1]
        if check(x,y,i):
            sudoku[x][y] = i
            trigg = bt(idx+1)
            if trigg:
                return True
            sudoku[x][y] = 0

bt(0)