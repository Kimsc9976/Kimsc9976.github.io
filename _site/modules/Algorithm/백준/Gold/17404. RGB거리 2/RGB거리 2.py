N = int(input())
RGBS = [list(map(int,input().split())) for _ in range(N)]

inf = float('inf')
dp = [[inf, inf, inf] for _ in range(N)]
ans = inf

for c in range(3):
    dp = [[inf, inf, inf] for _ in range(N)]
    dp[0][c] = RGBS[0][c]
 
    for i in range(1, N):
        dp[i][0] = RGBS[i][0] + min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = RGBS[i][1] + min(dp[i-1][0],dp[i-1][2])
        dp[i][2] = RGBS[i][2] + min(dp[i-1][0],dp[i-1][1])

    for k in range(3):
        if k != c :
            ans = min(ans,dp[-1][k])
print(ans)