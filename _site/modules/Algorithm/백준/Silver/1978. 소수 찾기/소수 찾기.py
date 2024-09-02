import sys
T = int(sys.stdin.readline())

num_list = list(map(int,sys.stdin.readline().split()))

cnt = 0

for i in range(T):
    trigger = 0
    num = num_list[i]
    if num == 1:
        continue
    for idx in range(2,num):
        if num % idx == 0:
            trigger = 1
            break
    if trigger == 1:
        continue
    else:
        cnt += 1
print(cnt)