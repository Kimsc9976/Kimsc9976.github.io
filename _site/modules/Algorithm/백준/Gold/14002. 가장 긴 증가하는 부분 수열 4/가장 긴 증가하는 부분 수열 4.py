T = int(input())
lst = list(map(int,input().split()))
dp = [1 for _ in range(T)]
ans = []
for i in range(T):
  rlt = set()
  rlt.add(lst[i])
  for j in range(i):
    if lst[i] > lst[j]:
      # print(dp[i],dp[j])
      if dp[i] >= dp[j]+1:
        dp[i] = dp[i]
      else : # if dp[i] < dp[j]+1
        dp[i] = dp[j] + 1
        rlt = ans[j].copy()
        rlt.add(lst[i])
  ans.append(rlt)

idx = 0
mx = dp[0]
for i in range(1,T):
  if dp[i] > mx:
    idx = i
    mx = dp[i]
print(mx)
x = sorted(ans[idx])
print(*x)
