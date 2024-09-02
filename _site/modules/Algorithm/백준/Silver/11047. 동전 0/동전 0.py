N,K = map(int,input().split())

c = []
for _ in range(N):
    c.append(int(input()))
c.sort(reverse= True)



ans = 0
idx = 0
res = K
while res != 0:
    if res // c[idx]== 0:
        idx +=1
    else:
        ans += res//c[idx]
        res = res%c[idx]

print(ans)