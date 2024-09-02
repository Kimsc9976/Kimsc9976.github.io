import heapq
from collections import namedtuple

INF = float('inf')
Node = namedtuple('Node', ['x', 'y', 'd', 'cnt'])

dx = [0, 0, 1, -1] # x방향 설정
dy = [1, -1, 0, 0] # y방향 설정

def set_door_direction(door, dist, pq):
    x, y = door[0].x, door[0].y
    # 문 앞에서 이동할 수 있는 방향을 체크한 후 pq에 넣어서 이동을 시킬 수 있도록 작업한다.
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '*':
            heapq.heappush(pq, Node(x, y, d, 0))
            dist[x][y][d] = 0

def dijkstra(door, dist, pq):
    global ans
    while pq:
        x, y, d, cnt = heapq.heappop(pq)
        if (x, y) == (door[1].x, door[1].y):
            ans = min(cnt, ans)
            # return cnt

        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '*':
            if grid[nx][ny] == '!': # 경로에 거울을 설치할 수 있을 경우
                nd = [0, 1] if d > 1 else [2, 3]
                for i in nd:
                    if dist[nx][ny][i] > cnt + 1:
                        heapq.heappush(pq, Node(nx, ny, i, cnt + 1))
                        dist[nx][ny][i] = cnt + 1

            if dist[nx][ny][d] > cnt: # 경로에 cnt 가 더 작을경우는 cnt로 변경한 뒤 pd에 투입
                heapq.heappush(pq, Node(nx, ny, d, cnt))
                dist[nx][ny][d] = cnt

    return INF

n = int(input())
grid = [list(input().strip()) for _ in range(n)]
dist = [[[INF] * 4 for _ in range(n)] for _ in range(n)] # 각 방향에 대하여 이동이 가능한지 여부 파악하기
pq = []  # 힙큐
door = []# 시작과 끝 넣어둔 배열
ans = INF
for i in range(n):
    for j in range(n):
        if grid[i][j] == '#':
            door.append(Node(i, j, -1, 0))

set_door_direction(door, dist, pq) # 초기 경로 매핑하기
dijkstra(door, dist, pq)
print(ans)