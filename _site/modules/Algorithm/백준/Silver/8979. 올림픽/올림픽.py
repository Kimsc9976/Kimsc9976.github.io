import sys
N, T = map(int, sys.stdin.readline().split())

Countries = []

for _ in range(N):
    c, g, s, b = map(int, sys.stdin.readline().split())
    
    Countries.append([c, g, s, b])


Countries.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

Rank = 1
for i in range(N):
    if i > 0 and (Countries[i][1], Countries[i][2], Countries[i][3]) == (Countries[i-1][1], Countries[i-1][2], Countries[i-1][3]):
        Countries[i].append(Countries[i-1][-1])  
    else:
        Countries[i].append(i + 1)  

# T 국가의 순위를 찾아 출력합니다.
for c in Countries:
    if c[0] == T:
        print(c[-1])
        break