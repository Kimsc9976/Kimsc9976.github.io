N = int(input())
start = list(map(int, input()))
end =  list(map(int, input()))
start_cpy = start[:]
rlt = 2*N
d= (-1,0,1)

x = 0
is_click = False
# cpy는 첫번째 스위치 켜고 출발
for k in d:
    nx = x + k
    if nx < 0 or nx >= N: continue
    start_cpy[nx] = (start_cpy[nx] + 1) % 2
ans = 0
ans_cpy = 1
x += 1


while x < N:

    x_ = x - 1
    if (start[x_] != end[x_]) :
        ans += 1
        for k in d:
            nx = x + k
            if nx < 0 or nx >= N: continue
            start[nx] = (start[nx] + 1) % 2
        pass
    if (start_cpy[x_] != end[x_]) : 
        ans_cpy += 1
        for k in d:
            nx = x + k
            if nx < 0 or nx >= N: continue
            start_cpy[nx] = (start_cpy[nx] + 1) % 2
        pass
        # is_start = False
        # if (start[nx] != end[nx]):
        #     is_click = True
    x += 1

if start == end:
    rlt = min(ans,rlt)
if start_cpy == end:
    rlt = min(ans_cpy,rlt)
if rlt == 2*N:
    rlt = -1
print(rlt)