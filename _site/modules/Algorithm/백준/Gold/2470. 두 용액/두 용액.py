import sys

N = int(input())
lst = list(map(int,sys.stdin.readline().split()))

lst.sort()
start = 0
end = N-1

ans = abs(lst[start] + lst[end])
target = [lst[0], lst[-1]]
while start < end:
    
    t = lst[start] + lst[end]

    if abs(t) < abs(ans):
        ans = abs(lst[start] + lst[end])
        target = [lst[start], lst[end]]
        if ans == 0:
            break
    
    if t < 0:
        start += 1
    else:
        end -= 1

print(*target)