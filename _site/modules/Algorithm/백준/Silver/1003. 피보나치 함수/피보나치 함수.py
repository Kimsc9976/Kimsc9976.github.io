import sys

def fibonacci(n):
    zeros=[1,0,1] # 0이 출력되는 횟수 리스트
    ones=[0,1,1] # 1이 출력되는 횟수 리스트
    if n >= 3:
        for i in range(2,n):
            zeros.append(zeros[i-1] + zeros[i]) # 숫자가 생성되는 것은 피보나치를 따르기 때문에 
            ones.append(ones[i-1] + ones[i])    # 이 정보들도 피보나치를 따르며 증가한다.

    print(f"{zeros[n]} {ones[n]}")
    
    
N = int(sys.stdin.readline().split()[0])

for _ in range(N):
    K = int(sys.stdin.readline().split()[0])
    fibonacci(K)
    
