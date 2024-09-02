T = int(input())
Ns = [int(input()) for _ in range(T)]

stack = []
for N in Ns:
    
    if N :
        stack.append(N)
    else:
        stack.pop()

print(sum(stack))

