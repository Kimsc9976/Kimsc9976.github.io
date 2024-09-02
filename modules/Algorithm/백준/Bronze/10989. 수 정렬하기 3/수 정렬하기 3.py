import sys
N = int(input())
lst = [0] * 10001

for i in range(N):
    _input = int(sys.stdin.readline())
    lst[_input] += 1

for i in range(10001):
    if lst[i]:
        for _ in range(lst[i]):
            print(i)