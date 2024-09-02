import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
# https://www.acmicpc.net/board/view/38887#comment-69010

def bfs(start, end):
    ans = 0
    path = f'{start}'
    
    que = deque([(start, 0, path)])
    
    target = max(start, end)*2 + 1
    
    matrix = [0 for _ in range(target)] 
    is_travel = [False for _ in range(target)] 
    
    is_travel[start] = True
    
    while que:
        now, depth, path = que.popleft()

        if now == end : return (matrix[now], path)
        # print(now, depth)
        for i in (2, -1, 1):
            
            if i == 2 and now <= target//2:
                _next = 2*now
                if is_travel[_next] : continue
                matrix[_next] = depth + 1
                que.append((_next, depth + 1, f'{path} {_next}'))
                is_travel[_next] = True
                
            if i == -1 and now > 0:
                _next = now-1
                if is_travel[_next] : continue
                matrix[_next] = depth + 1
                que.append((_next, depth + 1, f'{path} {_next}'))
                is_travel[_next] = True
                
            if i == 1 and now <= target//2:
                _next = now+1
                if is_travel[_next] : continue
                matrix[_next] = depth + 1
                que.append((_next, depth + 1, f'{path} {_next}'))
                is_travel[_next] = True
            
            # print(matrix)
            if _next == end : return (matrix[_next], f'{path} {_next}')
        # print()
    
    return (ans, path)

result = bfs(N,K)
print(result[0], result[1], sep="\n")