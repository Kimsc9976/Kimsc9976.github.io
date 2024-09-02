import sys
from heapq import heappush, heappop

def cp(a,b,c):
    v1 = [b[0] - a[0], b[1] - a[1]]
    v2 = [c[0] - b[0], c[1] - b[1]]
    return v1[0]*v2[1] - v1[1]*v2[0]

N = int(input())
Ls = []

for _ in range(N):
    a,b,c,d = map(int,sys.stdin.readline().split())
    if c < a :
        a,b,c,d = c,d,a,b
    heappush(Ls,(a, [a,b,c,d]))


ans = 0

L1 = 0
L2 = 1

while L2 != N:
    _, [x1,y1,x2,y2] = Ls[L1]
    _, [x3,y3,x4,y4] = Ls[L2]

    p1 = (x1,y1)
    p2 = (x2,y2)
    p3 = (x3,y3)
    p4 = (x4,y4)

    x_case = (max(x1,x2) < min(x3,x4) or max(x3,x4) < min(x1,x2))
    y_case = (max(y1,y2) < min(y3,y4) or max(y3,y4) < min(y1,y2))

    if x_case or y_case:
        if x_case:
            L1 += 1
            L2 = L1 + 1
        else:
            L2 += 1
        ans = 0
        continue
    else:
        # 외적의 특징을 이용해서 교점의 존재 유무를 찾음
        case1 = cp(p1, p2, p3) * cp(p1, p2, p4)
        case2 = cp(p3, p4, p1) * cp(p3, p4, p2)

        if case1 == 0 and case2 == 0: 
            ## 평행한 경우
            if (y2-y1)*(x4-x3) == (y4-y3)*(x2-x1):
                if (min(x3,x4) < x1 < max(x3,x4) and min(y3,y4) < y1 < max(y3,y4)) or (min(x3,x4) < x2 < max(x3,x4) and min(y3,y4) < y2 < max(y3,y4)):
                    ans = 1
                elif (min(x1,x2) < x3 < max(x1,x2) and min(y1,y2) < y3 < max(y1,y2)) or (min(x1,x2) < x4 < max(x1,x2) and min(y1,y2) < y4 < max(y1,y2)):
                    ans = 1
                else: ans = 0
            # 양 끝점이 일치하는 경우
            elif (p1 == p3 and p2 == p4) or (p2 == p3 and p1 == p4):
                ans = 1
            # 한 점만 일치하는 경우
            elif p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4:
                ans = 0

        elif (case1 <= 0 and case2 <= 0) and not (case1 == 0 and case2 == 0):
            ans = 1
        else:
            ans = 0

    if ans == 1:
        break
    
    if L2 < N:
        L2 += 1
    else:
        L1  += 1
        L2 = L1 + 1

print(ans)