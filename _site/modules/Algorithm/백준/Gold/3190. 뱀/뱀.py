import sys
from collections import deque
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())


apples = [[False for _ in range(N)] for _ in range(N)]
for _ in range(K):
    x, y = map(int,sys.stdin.readline().split())
    apples[x-1][y-1] = True

L = int(sys.stdin.readline())
move = deque([list(map(str,sys.stdin.readline().split())) for _ in range(L)])


d = [(0,1),(1,0),(0,-1),(-1,0)] # 나의 방향 기준 왼쪽(-1) 오른쪽(+1) 이 되도록 방향 설정
#    오른    아래   위     왼
def Dummy():
    snake = deque()
    snake.append((0,0))
    direction = 0

    time = 0
    while True:
        time += 1
        
        x, y = snake[-1]
        
        nx = x + d[direction][0]
        ny = y + d[direction][1]

        if nx < 0 or ny < 0 or nx>= N or ny >= N:
            break
        if (nx,ny) in snake : 
            break

        
        snake.append((nx,ny))
        if apples[nx][ny]:
            apples[nx][ny] = False
        else:
            snake.popleft()

        if move:
            t, D = move[0]
            t = int(t)
            if t == time:
                move.popleft()

                D = -1 if D == 'L' else 1
                direction = (direction + D + 4) % 4
    return time

print(Dummy())