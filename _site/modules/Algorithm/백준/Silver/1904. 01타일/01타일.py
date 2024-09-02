N = int(input())


ans = [0, 1, 2,]
###### 3  1  2
###### 6  4  5

t= 3
while t>=3 and t<=N :
    ans[t%3] =  (ans[(t-1)%3] + ans[(t-2)%3])%15746
    t += 1

print(ans[N%3])

