N = int(input())

cnt = 1
target = 1
while target < N :
    target += 6*cnt
    cnt += 1   
print(cnt)