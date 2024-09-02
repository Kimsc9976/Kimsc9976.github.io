
from collections import deque

def solution(n, edge):
       
    answer = 0
    Tree = [set() for _ in range(n+1)]
    is_visited = [False for _ in range(n+1)]
    far = [ 0 for _ in range(n+1)]
    
    for s, e in edge:
        Tree[s].add(e)
        Tree[e].add(s)
    
    que = deque()
    que.append((1,0))
    is_visited[1] = True
    
    while que:
        now, depth = que.popleft()
        
        for item in Tree[now]:
            if is_visited[item] : continue
            is_visited[item] = True
            far[item] = depth + 1
            que.append((item, depth + 1))
    
    F = max(far[1:])
    
    for i in range(1,n+1):
        if far[i] == F:
            answer += 1
    
    return answer