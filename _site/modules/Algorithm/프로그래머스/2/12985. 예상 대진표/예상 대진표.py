def solution(n,a,b):
    answer = 1

    a -= 1
    b -= 1
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')
    # n 이면 총 n-1 회 대전합니다.
    # 이 때 1,2, 3,4 5,6 7,8, --- 대전하면 특징은

    
    while ((a//2) != (b//2)):
        a //= 2
        b //= 2
        answer += 1
    
    return answer