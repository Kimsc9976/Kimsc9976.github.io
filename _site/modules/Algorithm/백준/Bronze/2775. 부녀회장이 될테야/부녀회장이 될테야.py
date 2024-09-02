import sys
T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    apt =[[0 for _ in range(n)] for _ in range(k+1)]
    for i in range(n):
        apt[0][i] = i+1
    for j in range(k+1):
        apt[j][0] = 1
    for j in range(k):
        for i in range(n - 1):
            apt[j+1][i+1] = apt[j+1][i] + apt[j][i+1]
    print(apt[k][n-1])