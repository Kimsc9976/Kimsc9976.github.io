def prec(n):
    if(n == '(' or n == ')'):
        return 0
    elif(n == '+' or n == '-'):
        return 1
    elif(n == '*' or n == '/'):
        return 2 

#식 입력
calculation = input()


stack =[]

for i in calculation:
    #문자가 숫자이면
    if(i.isalnum()):
        print(i, end='')
    else:
        if (i == '+' or i == '-' or i == '*' or i == '/'):
            #우선순위가 늪은 것이 스택 밑에 있다면 낮은거 있을 때까지 pop()
            while(stack != [] and prec(i) <= prec(stack[-1])):
                print(stack.pop(), end='')
            stack.append(i)

        elif(i == '('):
            stack.append(i)
            
        elif(i == ')'):
            k = stack.pop()
            while(k != '('):
                print(k, end='')
                k = stack.pop()
    
while(stack != []):
    print(stack.pop(), end='')