import sys

def find(num):
    cnt = 0
    if num < 10:
        cnt = 1
        return cnt
    
    num = str(num)
    arithm = int(num[0]) - int(num[1])
    
    for i in range(len(num) - 1):
        compare = int(num[i]) - int(num[i+1])
        if(arithm != compare):
            return cnt
    cnt = 1
    return cnt

T = int(sys.stdin.readline())
count = 0
for idx in range(T):
    number = idx + 1
    count += find(number)
print(count)