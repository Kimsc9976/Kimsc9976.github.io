import sys

N = int(sys.stdin.readline().split()[0])

dp = [0 for _ in range(N+1)]
path = ["" for _ in range(N+1)] # 최단 경로
path[1] = "1"

for idx in range(2, N+1):
    dp[idx] = dp[idx-1] + 1
    prev = idx - 1
    
    if idx % 2 == 0 and dp[idx//2]+1 < dp[idx]:
        dp[idx] = dp[idx//2] + 1
        prev = idx // 2
    if idx % 3 == 0 and dp[idx//3]+1 < dp[idx]:
        dp[idx] = dp[idx//3] + 1
        prev = idx // 3
    path[idx] = str(idx) + " " + path[prev]

print(dp[N])
print(path[N])