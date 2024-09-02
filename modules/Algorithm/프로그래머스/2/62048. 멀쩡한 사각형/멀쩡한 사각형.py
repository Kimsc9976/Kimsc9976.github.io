import math

def solution(w,h):
    answer = 1
    square = w*h
    # print(math.gcd(w,h))
    # 그래프는 hx + wy = wh이다.
    # 좌하단, 우상단을 비교했을 때, 해당 그래프가 범위안에 포함되면, 못쓰는 사각형
    # h*xl + w*y1 <= w*h and h*xr + w*yr >= w*h
#     for i in range(h):
#         for j in range(w):
#             xl, yl = j, i
#             xr, yr = j+1, i+1
            
#             if (h * xl + w * yl < w*h) and (h * xr + w * yr > w*h):
#                 cnt += 1
    
    

    return square - (w + h - math.gcd(w,h))