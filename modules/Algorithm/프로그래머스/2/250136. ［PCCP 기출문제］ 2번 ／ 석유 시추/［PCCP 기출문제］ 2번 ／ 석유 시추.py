from collections import deque

d = ((0,1), (0,-1), (1,0), (-1,0))

def bfs(sr, sc, land):
    global N, M
    que = deque()
    que.append((sr,sc))
    
    land[sr][sc] = 0
    count = 1
    
    oil_range = [sc, sc]
    
    
    while que:
        r, c = que.popleft()
        
        for dr, dc in d:
            nr = r + dr
            nc = c + dc
            
            if nr < 0 or nc < 0 or nr >= N or nc >= M: continue
            if not land[nr][nc] : continue
            
            land[nr][nc] = 0
            count += 1
            oil_range[1] = max(nc, oil_range[1])
            
            que.append((nr, nc))

        
    return oil_range, count

N = None
M = None

def solution(land):
    global N, M
    answer = 0
    
    N = len(land)
    M = len(land[0])
    
    # for row in land:
    #     print(*row)
    
    oils = list()
    
    
    for m in range(M):     
        for n in range(N):
            if not land[n][m] : continue
            oils.append(bfs(n, m, land))

    
    dig = [0 for _ in range(M)]
    
    for oil, count in oils:
        sc, ec = oil
        for i in range(sc, ec+1):
            dig[i] += count
    
    return max(dig)