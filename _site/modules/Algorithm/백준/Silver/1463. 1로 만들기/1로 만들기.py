N = int(input())

dp = [0 for _ in range(N + 1)]


for idx in range(2,N+1): # 어차피2 일때는 무조건 count가 +1이된다.
  dp[idx] = dp[idx - 1] + 1
  
  if idx % 3 == 0:
    dp[idx] = min(dp[idx//3] + 1, dp[idx]) 
  if idx % 2 == 0 :
    dp[idx] = min(dp[idx//2] + 1, dp[idx]) 
print(dp[N])