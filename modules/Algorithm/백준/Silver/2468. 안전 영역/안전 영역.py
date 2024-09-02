
import sys
from collections import deque

def bfs(x, y, water):
  result = 1
  d = [(0, 1),(0, -1),(1, 0),(-1, 0)]
  
  que = deque([(x, y)])
  is_travel[x][y] = True
  
  while que:
    x, y = que.popleft()
    
    for dx, dy in d:
      nx = x + dx
      ny = y + dy
      
      if nx < 0 or ny < 0 or nx >= N or ny >= N : continue
      if (matrix[nx][ny] <= water) or is_travel[nx][ny]: continue
      is_travel[nx][ny] = True
      que.append((nx, ny))
      result += 1
      
  return result


N,= map(int, sys.stdin.readline().split())

matrix = [ list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 0

X = 0
# print(*matrix, sep="\n")

while True:

  cnt = 0

  is_travel = [[ False for _ in range(N)] for _ in range(N) ]
  
  for a in range(N):
    for b in range(N):
      if matrix[a][b] > X and not is_travel[a][b]:
        cnt +=1
        bfs(a, b, X)

  if cnt == 0 : break
  ans = max(ans, cnt)
  
  X += 1

print(ans)