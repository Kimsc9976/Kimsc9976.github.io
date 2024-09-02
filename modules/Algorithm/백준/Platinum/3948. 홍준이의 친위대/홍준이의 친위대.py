
dp =[[0]*(i+1) for i in range(21)]

dp[0][0] = 1

for n in range(21):
    for k in range(1,n+1):
        dp[n][k] = dp[n][k-1] + dp[n-1][n-k]



T = int(input())

for t in range(T):
    x = int(input())
    if x != 1:
        print(2*dp[x][x])
    else:
        print(1)
