import sys
N = int(sys.stdin.readline())
r = []
for _ in range(N):
    r.append(int(sys.stdin.readline()))
r.sort(reverse=True)

temp_max = r[0]
for i in range(N):
    mr = r[i]*(i+1)
    if mr > temp_max:
        temp_max = mr

print(temp_max)
