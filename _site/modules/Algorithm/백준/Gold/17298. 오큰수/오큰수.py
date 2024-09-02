N = int(input())
numbers = list(map(int, input().split()))
X = [-1 for _ in range(N)]
stacks = []
for i in range(N-1, -1, -1):
    target = numbers[i]
    while stacks and stacks[-1] <= target:
        stacks.pop()
    if not stacks : X[i] = -1
    if stacks : X[i] = stacks[-1]
    stacks.append(target)
print(*X)