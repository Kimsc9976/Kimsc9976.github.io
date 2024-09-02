N,M = map(int,input().split())

from collections import deque

dx = (1,-1,0,0)
dy = (0,0,-1,1)

def bfs(a,b):
    global is_travel
    que = deque()
    que.append((a,b))
    is_travel[a][b] = True
    
    while que:
        x, y = que.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = 2
                is_travel[nx][ny] = True
                que.append((nx,ny))

row_matrix = [list(map(int,input().split())) for _ in range(N)]

binkan = tuple()
for i in range(N):
    for j in range(M):
        if row_matrix[i][j] == 0:
            binkan += ((i,j),)


from itertools import combinations
ans = 0
for items in combinations(binkan,3):
    
    matrix = [arr[:] for arr in row_matrix]
    for item in items:
        a, b = item
        matrix[a][b] = 1
    
    
    is_travel = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not is_travel[i][j] and matrix[i][j] == 2:
                bfs(i,j)
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                cnt += 1
    ans = max(ans,cnt)
print(ans)