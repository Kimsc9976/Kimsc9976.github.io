N = int(input())
ans = 0

stack = list()

for _ in range(N):
    height = int(input()) # 현재 들어오는 사람의 높이
    
    people = (height, 1) # 사람의 높이를 저장
    
    while stack and stack[-1][0] <= height: # 스텍이 있고 마지막 스텍에 있는 사람의 높이가 현재 사람보다 작을 경우에
        ans += stack[-1][1] # 같은 높이의 사람의 수를 카운팅함.(이렇게 작업하면 같은 숫자를 반복해서 사용할 필요가 없다.....)
        if stack[-1][0] == height: # 사람의 높이가 같을경우
            people = (height, people[1] + stack[-1][1]) # 사람이 함녕 더 있다고 카운팅을 한다.
        stack.pop() # Stack에 들어가있는 사람은 현재 사람보다 작거나 같기 때문에 카운팅 할 필요가 없음.
        
    if stack: # 스텍이 살아 있을 경우에는 쌍이 무조건 하나 생김 (사람이 있기 때문에)
        ans += 1
    stack.append(people)
print(ans)