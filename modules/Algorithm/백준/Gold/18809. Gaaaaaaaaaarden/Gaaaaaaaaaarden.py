import sys
from collections import deque
from itertools import combinations

# N = int(sys.stdin.readline())


def selectLand(position, Green_Red, now, sp):
    global answer
    if now == G + R:
        answer = max(answer, simulation(position, sp))
        return 
    
    if Green_Red[0] :
        Green_Red[0] -= 1
        seletedColor[now] = True
        selectLand(position, Green_Red, now + 1, sp)
        Green_Red[0] += 1

    if Green_Red[1] :
        Green_Red[1] -= 1
        seletedColor[now] = False
        selectLand(position, Green_Red, now + 1, sp)
        Green_Red[1] += 1

    
def simulation(position, start_point):
    
    for i in range(R+G):
        # G는 3번 R은 4번으로 배양액 뿌리기
        matrix[pos[i][0]][pos[i][1]] = 3 if position[i] else 4
    
    result = bfs(matrix, start_point)

    for i in range(R+G):
        # G는 3번 R은 4번으로 배양액 뿌리기
        matrix[pos[i][0]][pos[i][1]] = 2

    return result


def bfs(ground, start_point):
    result = 0
    is_visited = [[0 for _ in range(M)] for _ in range(N)]
    que = deque(start_point)

    for x, y in start_point:
        is_visited[x][y] = matrix[x][y]

    next_current = []

    while que or next_current:
        
        # 날이 지날경우 꽃이 핀지 안핀지 확인
        if not que:

            finishGround = set()
            nxt_curt = set()
            for gx, gy, color in next_current:
                
                if is_visited[gx][gy] == 0 and (ground[gx][gy] == 1 or ground[gx][gy] == 2):
                    is_visited[gx][gy] = color
                    nxt_curt.add((gx, gy))
                elif color != is_visited[gx][gy] :
                    is_visited[gx][gy] = 7
                    finishGround.add((gx, gy))
                

            que = deque(list(nxt_curt - finishGround))

            result += len(finishGround)
            next_current = []
            continue
        
        x, y = que.pop()

        for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= M : continue
            if is_visited[nx][ny] or ground[nx][ny] == 0: continue
            if ground[nx][ny] != 1 and ground[nx][ny] != 2 : continue

            
            next_current.append([nx, ny, is_visited[x][y]])

    return result

# seg_tree = [0]*(4*N)
N, M, G, R = list(map(int,sys.stdin.readline().split()))
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
answer = 0

ok_land = []
for n in range(N):
    for m in range(M):
        if matrix[n][m] == 2: ok_land.append((n,m))

# 배양액 G 배양 R 배양액 나둘 위치 결정해야함
# G는 True R는 False 로 작업해서 색 구분
 
seletedColor = [False for _ in range(G+R)]
for pos in combinations(ok_land, G+R):
    selectLand(seletedColor, [G, R], 0, pos)

print(answer)