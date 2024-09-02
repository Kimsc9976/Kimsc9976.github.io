T = int(input())

dp = [0 for _ in range(T+1)]

for i in range(1,T+1):
    row = list(map(int,input().split()))
    
    if i == 1:
        dp[i] = row[0]
    else:
        temp = [0 for _ in range(len(row))]
        for a in range(len(row)-1):
            temp[a] = dp[a+1] + row[a] if dp[a+1] + row[a] > temp[a] else temp[a]
            temp[a+1] = dp[a+1] + row[a+1]

        dp[1:len(row)+1] = temp
    
print(max(dp[1:]))