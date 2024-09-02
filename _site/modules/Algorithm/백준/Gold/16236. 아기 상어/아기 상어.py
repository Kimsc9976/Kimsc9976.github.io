from collections import deque

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]

# print(N, *matrix, sep='\n')

def find_fish(start):
    is_travel = [[False for _ in range(N)] for _ in range(N)]
    is_travel[start[0]][start[1]] = True
    
    que = deque([[start, 0]])
    fishes = []
    min_move = N*N
    
    while que:
        [x, y], move = que.popleft()
        if move + 1 > min_move : break
        
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            
            if nx < 0 or ny < 0 or nx>=N or ny >=N : continue
            if is_travel[nx][ny] : continue
            is_travel[nx][ny] = True
            fish_size = matrix[nx][ny]
            if shark_size < fish_size: continue
            
            if shark_size > fish_size and fish_size:
                
                min_move = min(min_move,move + 1)
                fishes.append([nx,ny])
            
            que.append([[nx,ny], move+1])
    
    return [fishes, min_move]

shark_size = 2
shark_stomp = 0

d = ((-1,0),(0,-1),(1,0),(0,1))
# 가까운 물고기가 많으면 위 -> 좌측 우선으로 탐색

shark = None

for i in range(N):
    for j in range(N):

        if(matrix[i][j] == 9):
            shark = [i, j]

ans = 0
while True:
    fishes, move = find_fish(shark)
    if not fishes or move == N*N: break
    fish = min(fishes, key=lambda fish: (fish[0], fish[1]))
    fx, fy = fish
    sx, sy = shark
    
    ans += move
    
    matrix[fx][fy] = 9
    shark = [fx,fy]
    
    matrix[sx][sy] = 0
    
    shark_stomp += 1
    if shark_stomp == shark_size:
        shark_size += 1
        shark_stomp = 0

print(ans)