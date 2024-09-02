import sys
from collections import deque

def bfs(j, f):

    que = deque()
    
    for fire in f:
        que.append((fire[0],fire[1], 0, '*'))
        is_travel[fire[0]][fire[1]] = True

    que.append((j[0],j[1], 0, '@'))
    is_travel[j[0]][j[1]] = True
    

    while que:
        x, y, depth, type = que.popleft()

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= M : continue
            if is_travel[nx][ny] : continue
            if type == '@' and (nx == 0 or ny == 0 or nx == N-1 or ny == M-1) and matrix[nx][ny] == '.' : return depth + 2
            if matrix[nx][ny] == '*' or matrix[nx][ny] == '#' : continue

            is_travel[nx][ny] = True
            que.append((nx, ny, depth + 1, type))

    return 'IMPOSSIBLE'


T = int(sys.stdin.readline())

for t in range(T):

    M, N = map(int, sys.stdin.readline().split())
    matrix = [list(map(str,sys.stdin.readline())) for _ in range(N)]

    d = [(0,1),(0,-1),(1,0),(-1,0)]

    is_travel = [[False for _ in range(M)] for _ in range(N)]
    jihon = None
    fire = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '@':
                jihon = (i, j)
            if matrix[i][j] == '*':
                fire.append((i,j))

    if (jihon[0] == 0 or jihon[1] == 0 or jihon[0] == N-1 or jihon[1] == M-1):
        answer = 1
    else:
        answer = bfs(jihon, fire)

    print(answer)