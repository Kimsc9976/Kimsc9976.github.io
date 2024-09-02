import sys
from collections import deque

sys.setrecursionlimit(10**9)
N = int(input())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
is_travel = [[False for _ in range(N)] for _ in range(N)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def is_edge(i, j):
    if matrix[i][j] <= 0:
        return False
    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 0:
            return True
    return False

def bfs(a, b, island):
    is_travel[a][b] = True
    matrix[a][b] = island
    que = deque([(a, b)])
    
    while que:
        x, y = que.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 1 and not is_travel[nx][ny]:
                matrix[nx][ny] = island
                is_travel[nx][ny] = True
                que.append((nx, ny))

def bfs_route(start, start_island):
    que = deque([(*start, 0)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[start[0]][start[1]] = True

    while que:
        x, y, depth = que.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                if matrix[nx][ny] > 0 and matrix[nx][ny] != start_island:
                    return depth
                if matrix[nx][ny] == 0:
                    que.append((nx, ny, depth + 1))
    return float('inf')

# 섬에 번호를 붙이는 과정
island = 1
for a in range(N):
    for b in range(N):
        if matrix[a][b] == 1 and not is_travel[a][b]:
            bfs(a, b, island)
            island += 1

# 각 섬의 가장자리에서 시작하여 최단 거리 찾기
ans = float('inf')
for a in range(N):
    for b in range(N):
        if is_edge(a, b):
            ans = min(ans, bfs_route((a, b), matrix[a][b]))

if ans == float('inf'):
    ans = 0

print(ans)