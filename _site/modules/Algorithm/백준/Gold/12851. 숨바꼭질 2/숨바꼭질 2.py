from collections import deque

N, K = map(int, input().split())
dx = [1, -1, 2]
que = deque()
cnt = 0
ans = 10 ** 5

arr = [0]*(10**6+1)
def bfs(start, depth):
  global cnt, ans, arr

  isVisited = [False] * (2 * 10 ** 5 + 1)
  que.append((start, depth))
  trigger = False
  while len(que):
    now, dep = que.popleft()

    if now > K and dep > ans:
        return
      
    if trigger == True:
      if now == K:
        cnt +=1
      continue
    
    if now == K:
        ans = dep
        trigger = True
        cnt += 1
        continue

    for t in range(3):
      if t == 2:
          nx = now * 2
      else:
          nx = now + dx[t]
      if nx >= 10 ** 5 + 5 * 10 ** 4:  # 이러한 경우로 도착하면 가깝게 될 일이 없음
          continue  ### N <= 10**5, K <= 10**5
      # if isVisited[nx] and nx != K: # 앞에 더욱 먼저 이곳에 도착한 친구들이 있음.
      #   continue
      if nx < -1:
          continue
      if arr[nx] != 0 and (dep+1) > arr[nx]:
        continue
      
      arr[nx] = dep+1
      que.append((nx, dep + 1))
      isVisited[nx] = True


bfs(N, 0)
print(ans, cnt, sep="\n")