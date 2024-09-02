from collections import deque

def check():
    for l in range(H):
        for i in range(N):
            for j in range(M):
                if box[l][i][j] == 0:
                    return False
    return True


M, N, H = map(int,input().split())

result = 0
box = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
is_visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

dx = (1,-1,0,0,0,0)
dy = (0,0,-1,1,0,0)
dz = (0,0,0,0,-1,1)
def bfs(lst):
    que = deque()
    depth = 0
    for domado in lst:
        que.append((domado[0],domado[1],domado[2],depth))
        is_visited[domado[0]][domado[1]][domado[2]] = True

    while que:
        z,x,y,depth = que.popleft()

        for k in range(6):
            nz = z + dz[k]
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nz < 0 or nx >= N or ny >= M or nz >= H: continue
            if box[nz][nx][ny] == -1 or box[nz][nx][ny] == 1: continue
            if is_visited[nz][nx][ny] : continue
            is_visited[nz][nx][ny] = True
            box[nz][nx][ny] = 1

            que.append((nz,nx,ny,depth+1))

    return depth

domados = []
for l in range(H):
    for i in range(N):
        for j in range(M):
            if box[l][i][j] == 1 and not is_visited[l][i][j]:
                domados.append((l,i,j))
            # result = max(bfs(i,j),result)

result = bfs(domados)

if check():
    print(result)
else:
    print(-1)