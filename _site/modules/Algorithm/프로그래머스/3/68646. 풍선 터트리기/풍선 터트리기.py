def solution(a):
    
    len_a = len(a)
    if len_a <= 2:
        return len_a
    
    # 왼쪽과 오른쪽 방향에서의 최소값을 저장할 배열 초기화
    left_min = [0 for _ in range(len_a)]
    right_min = [0 for _ in range(len_a)]
    
    # 왼쪽에서의 최소값 계산
    min_value = a[0]
    for i in range(len_a):
        if a[i] < min_value:
            min_value = a[i]
        left_min[i] = min_value
        
    # 오른쪽에서의 최소값 계산
    min_value = a[-1]
    for i in range(len_a-1, -1, -1):
        if a[i] < min_value:
            min_value = a[i]
        right_min[i] = min_value
    

    answer = 0
    for i in range(len_a):
        # 해당 풍선이 왼쪽 또는 오른쪽 방향에서 최소값보다 크면 터트려야 함
        # 단, 양 끝의 풍선은 항상 남길 수 있음
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            answer += 1
            
    return answer