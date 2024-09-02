
import sys
N = int(sys.stdin.readline())

lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 0

lines.sort(key= lambda x: (x[0], x[1])) 
# 정렬을 해서 아래서부터 탐색하기

start = lines[0][0]
end = lines[0][1]
for i in range(1, N):
    
    line_s, line_e = lines[i]
    
    if end > line_s: # 겹치는 케이스
        end = max(end, line_e)
    else:
        ans += (end - start)
        start, end = line_s, line_e
        

ans += (end - start)
print(ans)