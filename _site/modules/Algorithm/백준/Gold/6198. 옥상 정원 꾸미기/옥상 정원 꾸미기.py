N = int(input())
buildings = [int(input()) for _ in range(N)]

stack = []
count = 0

for building in buildings:
    while stack and stack[-1] <= building:
        stack.pop()
    stack.append(building)
    count += len(stack) - 1

print(count)