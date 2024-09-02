F,S,G,U,D = map(int,input().split())
# F층 , S시작 G끝 , U 번 위로 D번 아래로
  
  
dp = [F for _ in range(F+1)]
is_visited = [False for _ in range(F+1)]
from collections import deque
def bfs(start):
  x = (U, -1 * D)
  que = deque()
  que.append((start, 0))
  
  while que:
    now, depth = que.popleft()
    if now == G: return depth
    if depth == F: return 'use the stairs'
    if is_visited[now]: continue
    is_visited[now] = True
    
    for k in range(2):
      next = now + x[k]
      if next < 1 or next > F : continue
      if depth+1 > dp[next] : continue
      if is_visited[next] : continue
      
      dp[next] = depth+1
      que.append((next, depth+1))
  
  return 'use the stairs'
print(bfs(S))