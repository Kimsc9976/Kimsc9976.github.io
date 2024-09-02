from collections import deque
N, M = map(int, input().split())

dx = (-1,1,0,0)
dy = (0,0,-1,1)

def bfs(start):
    que = deque()
    que.append(start)
    while que:
        x, y = que.popleft()

        for k in (0,1,2,3,):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx<0 or ny<0 or nx>=N or ny>=M: continue
            if cheeses[nx][ny] == 1: continue
            if cheeses[nx][ny] == 2: continue
            cheeses[nx][ny] = 2
            que.append((nx,ny))

cheeses = [list(map(int,input().split())) for _ in range(N)]
che =[]

def find_outside() : 
    check = False
    for i in range(N):
        for j in range(M):
            if cheeses[i][j] == 0:
                bfs((i,j))
                return True
            if cheeses[i][j] == 1:
                che.append((i,j))
                check= True
    return check
def find_cheese() : 
    for i in range(N):
        for j in range(M):
            if cheeses[i][j] == 1:
                che.append((i,j))

time = 0
find_outside()
find_cheese()
l_che = len(che)
chee = 0

def check():
    chee = 0
    for i,j in che:
        if cheeses[i][j] == 2 : chee += 1; continue
    return False if chee == l_che else True

while check():
    time += 1

    C = set()
    chee = 0
    not_melt = 0
    for i,j in che:
        if cheeses[i][j] == 2 : chee += 1
        if cheeses[i][j] == 1 : not_melt += 1

        count = 0
        for l in (0,1,2,3,):
            ni = i + dx[l]
            nj = j + dy[l]

            if cheeses[ni][nj] == 2:
                C.add((i,j))

        
            
    
    for cx, cy in C:
        cheeses[cx][cy] = 2
        bfs((cx,cy))

print(time)
print(not_melt)