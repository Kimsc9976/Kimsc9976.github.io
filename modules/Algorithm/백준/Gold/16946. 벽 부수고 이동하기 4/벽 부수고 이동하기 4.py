from collections import deque

N,M = map(int,input().split())
ans = list()
matrix = list()
is_travel = list()
blocks = list()
for i in range(N):
    row = list(map(int,input()))
    row_ = []
    _row = []
    matrix.append(row)
    for j in range(M):
        if row[j]:
            blocks.append((i,j))
        row_.append(0)
        _row.append(False)
    ans.append(row_)
    is_travel.append(_row)


groups = dict()
group = 10
def bfs(start):
    global group
    cnt = 1
    que = deque()
    que.append(start)
    is_travel[start[0]][start[1]] = True

    while que:
        x,y = que.popleft()

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx>=N or ny>= M:continue
            if matrix[nx][ny] == 1: continue
            if is_travel[nx][ny] :continue
            is_travel[nx][ny] = True
            matrix[nx][ny] = group
            que.append((nx,ny))
            cnt += 1
        
    groups[group] = cnt
    group += 1

    return cnt

for a in range(N):
    for b in range(M):
        if matrix[a][b] == 0:
            matrix[a][b] = group
            bfs((a,b))

# print(groups)
for block in blocks:
    group_visited = set()
    link = 1
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx = block[0] + dx
        ny = block[1] + dy

        if nx < 0 or ny < 0 or nx>=N or ny>= M:continue
        if matrix[nx][ny] == 1 : continue
        group_visited.add(matrix[nx][ny])

    for k in group_visited:
        link += groups[k]
    # matrix[block[0]][block[1]] = 0
    ans[block[0]][block[1]] = link%10
    # matrix[block[0]][block[1]] = 1

# for row in matrix:
#     print(*row)
# print()
for row in ans:
    print(*row,sep='')