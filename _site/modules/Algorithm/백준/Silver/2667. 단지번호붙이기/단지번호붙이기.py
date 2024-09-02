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
      
      if nx < 0 or ny < 0 or nx >= N or ny >= N : continue
      if (matrix[nx][ny] == 0) or (matrix[nx][ny]== 2): continue
      
      matrix[nx][ny] = 2
      que.append((nx, ny))
      result += 1
      
  return result


N,= map(int, sys.stdin.readline().split())

matrix = [ list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

ans = []


cnt = 0
for a in range(N):
  for b in range(N):
    if matrix[a][b] == 1:
      cnt +=1
      ans.append(bfs(a, b))


print(cnt)
print(*sorted(ans))