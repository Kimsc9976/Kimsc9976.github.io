x = int(input())
arr = list(map(int, input().split()))
dp = [0 for i in range(x)]

for i in range(x):
    dp[i] = arr[i]
    for j in range(i):
        if arr[i] > arr[j]:        
            dp[i] = max(dp[i], dp[j]+ arr[i])
print(max(dp))
