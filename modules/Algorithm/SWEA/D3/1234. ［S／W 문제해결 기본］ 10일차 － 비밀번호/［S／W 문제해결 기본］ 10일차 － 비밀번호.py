for j in range(1,11):
    n, word = input().split()


    stack=[]
    for i in range(int(n)): #1238099084
        if len(stack) ==0:
            stack.append(word[i])
        else:
            top=stack[-1]
            if top==word[i]:
                stack.pop()
            else:
                stack.append(word[i])

    print(f'#{j} {"".join(stack)}')
