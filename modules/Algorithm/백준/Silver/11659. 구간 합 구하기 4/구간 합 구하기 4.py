
import sys

N, M = map(int, sys.stdin.readline().split())

List = list(map(int,sys.stdin.readline().split()))


dp = [ 0 for _ in range(N)]

for i in range(N):
    dp[i] = dp[i-1] + List[i]

dp = [0] + dp

for _ in range(M):
    s, e = map(int,sys.stdin.readline().split())
    print(dp[e] - dp[s-1])