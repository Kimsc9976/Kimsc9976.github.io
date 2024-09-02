import sys
import math

M = int(sys.stdin.readline())

while M != 0 :
    N = 2*M
    num_list = [True for _ in range(N + 1)]

    for idx in range(2, int(math.sqrt(N)) + 1):
        if num_list[idx] == True:
            i = 2
            while idx * i <= N:
                num_list[idx * i] = False
                i += 1
    cnt = 0
    for i in range(M+1, N + 1):
        if num_list[i]:
            if i != 1:
                cnt += 1
    print(cnt)
    M = int(sys.stdin.readline())