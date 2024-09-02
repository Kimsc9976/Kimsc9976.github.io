from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def checkNstart(mat, type):
    is_travel = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mat[i][j] == '2':
                if type == 'bfs':
                    rlt = bfs(mat, is_travel, i , j)
                    return rlt 
                if type == 'dfs':
                    is_travel[i][j] = True
                    rlt = set()
                    dfs(mat, is_travel, i, j, 0, rlt)

                    
                    return 0 if len(rlt) == 0 else min(rlt) 


def dfs(mat, is_travel, i, j, depth, rlt:set):
    if mat[i][j] == '3':
        rlt.add(depth-1)
        return 
    
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
        if mat[nx][ny] == '1' or is_travel[nx][ny] == True: continue
        is_travel[nx][ny] = True
        dfs(mat, is_travel, nx, ny, depth+1, rlt)
        is_travel[nx][ny] = False


def bfs(mat, is_travel, i, j):

    que = deque()
    is_travel[i][j] = True
    que.append((i,j, 1))

    while que:
        x, y, cnt = que.popleft()

        if x == N-1 and y == M-1:
            return cnt

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if mat[nx][ny] == '0' or is_travel[nx][ny] == True: continue
            is_travel[nx][ny] = True
            que.append((nx,ny,cnt+1))

    return 0


N, M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
is_travel = [[False for _ in range(M)] for _ in range(N)]

print(bfs(matrix, is_travel, 0 , 0))