import sys
import math

M, N = map(int, sys.stdin.readline().split())
num_list = [True for _ in range(N + 1)]

for idx in range(2, int(math.sqrt(N)) + 1):
    if num_list[idx] == True:
        i = 2
        while idx * i <= N:
            num_list[idx * i] = False
            i += 1

for i in range(M, N + 1):
    if num_list[i]:
        if i != 1:
            print(i)