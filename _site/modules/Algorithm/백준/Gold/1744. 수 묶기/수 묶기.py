import sys
N = int(sys.stdin.readline())

plus = []
minus = []

result = 0
for i in range(N):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    elif num == 1:
        result += num
        
plus.sort(reverse=True) # [6, 5, 4, 3, 2, ---]
minus.sort()            # [-3, -2, -1, 0, ---]

# 양수 묶기
for i in range(0, len(plus), 2):
    if i+1 >= len(plus):  # 홀수개인 경우, 마지막것 더하기
        result += plus[i]
    else:                 # 짝수개인 경우 그냥 곱해
        result += (plus[i] * plus[i+1])
        
# 음수 묶기
for i in range(0, len(minus), 2):
    if i+1 >= len(minus): # 홀수개인 경우, 마지막것 더하기
        result += minus[i]
    else:                 # 짝수개인 경우 그냥 곱해
        result += (minus[i] * minus[i+1])
        
print(result)