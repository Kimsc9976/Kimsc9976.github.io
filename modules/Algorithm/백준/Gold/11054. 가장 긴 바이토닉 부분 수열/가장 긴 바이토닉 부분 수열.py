x = int(input())
arr = list(map(int, input().split()))
increase = [1]*x
decrease = [1]*x
result = [0]*x

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j] + 1)

for i in range(x-1, -1, -1):
    for j in range(x-1, i, -1):
        if arr[i] > arr[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

for i in range(x):
    result[i] = increase[i] + decrease[i] - 1

print(max(result))