while True:
    lst = list(map(int,input().split()))
    if lst[0] == 0:
        break
    
    N = lst[0]
        
    stack = []
    max_rlt = 0
    lst = lst[1:]
    for i in range(N):
        height = lst[i]
        stack_i = i
        while stack and stack[-1][1] > height:  # 스택에서 빼내며 최대 직사각형 넓이를 계산
            # 스택에 들어있는 막대 중에서 현재 막대의 길이보다 큰 것들만 꺼내서 계산
            stack_i, stack_height = stack.pop()
            result = (i - stack_i) * stack_height
            max_rlt = max(result, max_rlt) # 최대값 갱신
            

        stack.append((stack_i, height))  # 스택에 현재 막대기를 추가
            
    # 반복이 종료되고, 스택에 남은 막대기가 있다면 계산
    while stack:
        stack_i, stack_height = stack.pop()
        result = (N - stack_i) * stack_height
        max_rlt = max(result, max_rlt) # 최대값 갱신  
        
    print(max_rlt)
