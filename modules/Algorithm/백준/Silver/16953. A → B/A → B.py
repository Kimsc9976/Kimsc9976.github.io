from collections import deque
N, M = map(int,input().split())

que = deque()

def bfs(start, end):
    que.append((start,0))

    while que:
        now, depth = que.popleft()

        if now > end:
            continue
        if now == end:
            return depth+1

        x1 = now*10 + 1
        x2 = now *2
        que.append((x1,depth+1))
        que.append((x2,depth+1))
    return -1

print(bfs(N,M))