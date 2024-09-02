from collections import deque
N, K = map(int,input().split())
dx = [1, -1, 2]
que = deque()

def bfs(start,depth):
  
  isVisited = [False] * (2*10**5 + 1)
  que.append((start, depth))
  
  while len(que):
    now, dep = que.popleft()
    
    if now == K:
      return dep
      
    for t in range(3):
      if t == 2:
        nx = now * 2
      else:
        nx = now + dx[t]
        
      if nx >= 2*100000:
        continue
      if isVisited[nx]: # 앞에 더욱 먼저 이곳에 도착한 친구들이 있음.
        continue
      if nx < -1:
        continue
      que.append((nx,dep+1))
      isVisited[nx] = True 
answer = bfs(N, 0)
print(answer)