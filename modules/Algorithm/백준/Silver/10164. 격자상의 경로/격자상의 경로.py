import math

N,M,K = map(int,input().split())

# 특정한 점이 있을 경우
if K:
    # 특정한 점의 좌표를 계산합니다.
    x, y = divmod(K-1, M)
    x += 1
    y += 1
    
    # 시작점에서 특정한 점까지의 경로의 수를 계산합니다.
    a = math.comb(x+y-2, x-1)
    
    # 특정한 점에서 종점까지의 경로의 수를 계산합니다.
    b = math.comb(N+M-x-y, N-x)
    
    # 전체 경로의 수는 두 하위 경로의 수를 곱한 것과 같습니다.
    print(a*b)
    
# 특정한 점이 없을 경우
else:
    # 시작점에서 종점까지의 경로의 수를 계산합니다.
    print(math.comb(N+M-2, N-1))