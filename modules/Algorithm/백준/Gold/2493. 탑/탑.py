N = int(input())
tower = list(map(int,input().split()))
gett = [0 for _ in range(N)]


# target = 0
# for i in range(1,N):
#     if tower[target] <= tower[i]:
#         target = i
#     else:
#         for j in range(i-1, target - 1, -1):
#             if tower[j] >= tower[i]:
#                 gett[i] = j+1
#                 break
# print(*gett)
stack = []
gett1 = [0 for _ in range(N)]
stack.append((tower[0],1))
for i in range(1,N):
    if tower[i] < stack[-1][0]:
        gett1[i] = stack[-1][1]
    else:
        while stack:
            if tower[i] < stack[-1][0]:
                gett1[i] = stack[-1][1]
                break
            else:
                stack.pop()

    stack.append((tower[i],i+1))
print(*gett1)