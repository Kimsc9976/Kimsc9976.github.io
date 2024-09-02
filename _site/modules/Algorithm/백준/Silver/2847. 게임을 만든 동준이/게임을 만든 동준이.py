import sys
N = int(sys.stdin.readline())

score = [int(sys.stdin.readline()) for _ in range(N)]

count = 0
for i in range(N-2, -1, -1):
    if score[i] >= score[i+1]:
        count += score[i] - score[i+1] + 1
        score[i] = score[i+1]-1
        
print(count)