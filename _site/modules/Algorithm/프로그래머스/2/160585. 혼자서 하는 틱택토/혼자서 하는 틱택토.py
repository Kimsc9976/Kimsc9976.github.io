def countOX(board):
    O = 0
    X = 0
    
    for row in board:
        for c in row:
            if c == 'O' : O += 1
            if c == 'X' : X += 1
    return O, X

def bingo(board, target):
    
    is_bingo = False
    for row in board:
        for c in row:
            if c != target : break
        else : return True
        
    for i in range(3):
        col = board[0][i] + board[1][i] + board[2][i]
        for c in col:
            if c != target : break
        else : return True
    
    diagL2R = board[0][0] + board[1][1] + board[2][2]
    diagR2L = board[0][2] + board[1][1] + board[2][0]
    
    diags = [diagL2R, diagR2L]
    for diag in diags:
        for c in diag:
            if c != target : break
        else : return True
    
    return False
        
def solution(board):
    
    O, X = countOX(board)
    
    if O < X : return 0
    if abs(O - X) >= 2 : return 0

    is_O_bingo = bingo(board, 'O')
    is_X_bingo = bingo(board, 'X')
    
    if is_O_bingo and is_X_bingo : return 0

    if is_O_bingo and O == X : return 0
    if is_X_bingo and O > X : return 0
    
    return 1