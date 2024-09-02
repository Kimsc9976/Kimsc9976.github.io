import sys
N = int(sys.stdin.readline())

items = list(map(int, sys.stdin.readline().split()))

answer = [items[0], items[-1]]


a = 0
b = N-1
while a < b:
    checksum = items[a] + items[b]
    if abs(checksum) <= abs(sum(answer)):
        answer = [items[a], items[b]]

        if checksum == 0:
            break
    
    if checksum < 0:
        a += 1
    else:
        b -= 1

print(*answer)