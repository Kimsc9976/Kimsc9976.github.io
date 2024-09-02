
import sys
from collections import deque

def bfs(x, y):
  result = 1
  d = [(0, 1),(0, -1),(1, 0),(-1, 0)]
  
  que = deque([(x, y)])
  matrix[x][y] = 2
  
  while que:
    x, y = que.popleft()
    
    for dx, dy in d:
      nx = x + dx
      ny = y + dy
      
      if nx < 0 or ny < 0 or nx >= N or ny >= M : continue
      if (matrix[nx][ny] == 0) or (matrix[nx][ny]== 2): continue
      
      matrix[nx][ny] = 2
      que.append((nx, ny))
      result += 1
      
  return result


N, M, K = map(int, sys.stdin.readline().split())

matrix = [[1 for _ in range(M)] for _ in range(N)]

ans = []
for _ in range(K):
  Lx, Ly, Rx, Ry = map(int, sys.stdin.readline().split())
  

  for j in range(Lx, Rx):
    for i in range(Ly, Ry):
      matrix[i][j] = 0
      
# print(*matrix, sep="\n")

cnt = 0
for a in range(N):
  for b in range(M):
    if matrix[a][b] == 1:
      cnt +=1
      ans.append(bfs(a, b))

  
# print(*matrix, sep="\n")
print(cnt)
print(*sorted(ans))