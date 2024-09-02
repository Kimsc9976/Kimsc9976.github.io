N = int(input())

A = list(map(int, input().split()))
B = [0]*N

A.sort(reverse=False)

result = 0

for i in range(N):
    B[i] = A[i] + B[i-1]
    
print(sum(B))