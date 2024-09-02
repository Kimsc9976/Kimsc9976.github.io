N = int(input())

r = []
for _ in range(N):
    r.append(list(map(int,input().split())))
r.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = r[0][1]
for i in range(1, N):
    if r[i][0] >= end_time:
        cnt += 1
        end_time = r[i][1]
print(cnt)