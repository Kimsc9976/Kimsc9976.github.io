from collections import deque
T = int(input())

d = ((2,1),(1,2), (2,-1),(1,-2), (-2,1),(-1,2), (-2,-1),(-1,-2))

for _ in range(T):
    N = int(input())
    sx, sy = map(int,input().split())
    ex, ey = map(int,input().split())
    
    que = deque()
    matrix = [[False for _ in range(N)] for _ in range(N)]
    que.append((sx,sy, 0))
    matrix[sx][sy] = True
    ans = 0
    while que:
        x, y, depth = que.popleft()
        
        if x == ex and y == ey:
            ans = depth
            break
        
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N : continue
            if matrix[nx][ny] : continue
            matrix[nx][ny] = True
            
            que.append((nx,ny, depth+1))
        
    print(ans)