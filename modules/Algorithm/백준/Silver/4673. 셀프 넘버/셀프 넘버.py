n = 10000

check = [0 for _ in range(n)]

for idx in range(len(check)):
    num = idx + 1
    
    d = num
    while num != 0:
        r = num % 10
        num = num // 10
        d += r
    if(d <= n):
        check[(d-1)] += 1
    
for idx in range(len(check)):
    if check[idx] == 0:
        print(idx+1)