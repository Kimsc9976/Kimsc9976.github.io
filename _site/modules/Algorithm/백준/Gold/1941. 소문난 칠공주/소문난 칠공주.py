from itertools import combinations
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(lst : tuple):
    target = []
    for cmb in lst:
        x = cmb//5
        y = cmb%5
        target.append((x,y))
    
    is_travel = {t:False for t in target}

    que = deque()
    que.append(target[0])
    is_connected = 0
    while que:
        a, b = que.popleft()
        for k in range(4):
            na = a + dx[k]
            nb = b + dy[k]
            if (na, nb) in target:
                if is_travel[(na,nb)]:
                    continue
                is_travel[(na,nb)] = True
                is_connected += 1
                que.append((na,nb))                
    if is_connected == 7:
        return 1
    else :
        return 0

N = 5
combs = list(combinations(range(0,25), 7))
# print(combs)
clas = [list(input()) for _ in range(N)]

ans = 0
for comb in combs:
    cnt = 0
    Trigger = True
    for student in comb:
        i = student//5
        j = student%5
        if clas[i][j] == 'Y':
            cnt += 1
        if cnt >= 4:
            Trigger = False
            break
    if Trigger:
        ans += bfs(comb)

print(ans)