from collections import deque

N,M = map(int,input().split())

lst = [[] for _ in range(N+1)]
cnts = [ 0 for _ in range(N+1)]
for _ in range(M):
    s, e = map(int,input().split())
    lst[s] += [e]
    cnts[e] += 1

ans = []

que = deque()
for i in range(1,N+1):
    if cnts[i] == 0:
        que.append(i)
        
while que:
    x = que.popleft()
    
    for item in lst[x]:
        cnts[item] -= 1
        if cnts[item] == 0:
            que.append(item)
    print(x,end=' ')