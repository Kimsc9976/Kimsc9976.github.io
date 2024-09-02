x1,y1,x2,y2 = list(map(int,input().split()))
x3,y3,x4,y4 = list(map(int,input().split()))

p1 = (x1,y1)
p2 = (x2,y2)
p3 = (x3,y3)
p4 = (x4,y4)


# 이렇게 4개의 좌표가 있다고 하고, ab, cd 두 선분이 있다고 했을 때
# 두 선분이 교차하는지를 보려면, ab와 ac의 외적값과 ab와 ad의 외적 값을 곱해 음수가 나오고
# cd와 ca, cd와 cb의 외적값 곱이 음수가 나오면 된다.
# [출처] 2차원 벡터의 외적 특성|작성자 대꼬
def cp(a,b,c):
    v1 = [b[0] - a[0], b[1] - a[1]]
    v2 = [c[0] - b[0], c[1] - b[1]]
    return v1[0]*v2[1] - v1[1]*v2[0]

# 직선의 방정식 구하기 https://mathbang.net/443#gsc.tab=0
# 좌표값 찾기는 니 알아서 하세요^^ 머리 깨지겠네ㅎ
def point():
    a1 = (y2-y1)
    b1 = (x2-x1)
    c1 = (x2*y1 - x1*y2) # (x2-x1)*y1 - (y2-y1)*x1 이기 때문

    a2 = (y4-y3)
    b2 = (x4-x3)
    c2 = (x4*y3 - x3*y4) # (x4-x3)*y3 - (y4-y3)*x3 이기 때문

    x = (c2*b1 - c1*b2)/(b2*a1 - b1*a2)
    y = (c2*a1 - c1*a2)/(b2*a1 - b1*a2)
    return (x,y)

if (max(x1,x2) < min(x3,x4) or max(x3,x4) < min(x1,x2)) or (max(y1,y2) < min(y3,y4) or max(y3,y4) < min(y1,y2)):
    print(0)
else:
    # 외적의 특징을 이용해서 교점의 존재 유무를 찾음
    case1 = cp(p1, p2, p3) * cp(p1, p2, p4)
    case2 = cp(p3, p4, p1) * cp(p3, p4, p2)

    if case1 <= 0 and case2 <= 0:
        print(1)
        # 기울기가 동일한 경우 한 점만 만날 수 있는 case 가 존재한다 + 겹치는 경우는 배제해줘야한다.
        # 에제 6번
        # if (y2-y1)*(x4-x3) == (y4-y3)*(x2-x1):
        #     if max(x1,x2) == min(x3,x4) or max(x3,x4) == min(x1,x2):
        #         if p1 in (p3,p4): print(*p1)
        #         elif p3 in (p1,p2): print(*p3)
        # else:
        #     print(*point())
    else:
        print(0)