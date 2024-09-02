from collections import deque
# 0 : 북
# 1 : 동
# 2 : 남
# 3 : 서
# row 방향 서 -> 동
# col 방향 북 -> 남

# d = (0,3,2,1) # 반시계로 회전
d = (0,1,2,3) # 시계방향...
dxy = ((-1,0),(0,1),(1,0),(0,-1))

def clean(i,j,l):
    que = deque()
    que.append((i,j,l))
    cnt = 0
    while que:
        x,y,Look = que.popleft()
        for k in range(Look-1 ,Look-4 - 1, -1):
            nx = x + dxy[k][0]
            ny = y + dxy[k][1]
            if room[nx][ny] == 1 or room[nx][ny] == 9:
                continue
            room[nx][ny] = 9
            que.append((nx,ny,(k+4)%4))
            cnt += 1
            break
        else:
            nx = x + dxy[Look - 2][0]
            ny = y + dxy[Look - 2][1]
            if room[nx][ny] == 1:
                break
            que.append((nx,ny,Look))

    return cnt

N, M = map(int,input().split())
a, b, diraction = map(int,input().split())

room = [list(map(int,input().split())) for _ in range(N)]


room[a][b] = 9
ans = 1
ans += clean(a,b,diraction)
print(ans)