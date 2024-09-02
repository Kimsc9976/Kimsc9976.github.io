import sys

def color(n,k,answer):
    if(n/k == 2):
        return 2
    if(k == 1):
        return n
    if(dp[n][k] == 0):
        total = color(n-1,k,answer) + color(n-2,k-1,answer)
        dp[n][k] = total
        return total
    else:
        return dp[n][k]
        
n = int(sys.stdin.readline().split()[0])
k = int(sys.stdin.readline().split()[0])

dp = [[0]*(n+1) for i in range(n+1)]

if(n/2 < k):
    print(0)
else:
    print(color(n,k,dp)%1000000003)