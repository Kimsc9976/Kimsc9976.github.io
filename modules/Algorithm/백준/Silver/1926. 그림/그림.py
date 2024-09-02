import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

d = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(i, j):
    result = 1
    que = deque([(i,j)])
    matrix[i][j] = 2

    while que:
        x, y = que.popleft()

        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= M : continue
            if matrix[nx][ny] == 0 or matrix[nx][ny] == 2 : continue
            matrix[nx][ny] = 2
            que.append((nx, ny))
            result += 1
    return result

count = 0
area = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            count += 1
            area = max(area, bfs(i, j))

print(count)
print(area)