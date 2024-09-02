N = int(input())

for _ in range(N):
    string = list(input())
    is_VPS = True
    s = []
    for c in string:
        
        if c == '(' : 
            s.append(c)
        else : # c == ')'
            if not s : 
                is_VPS = False
                break
            else :
                s.pop()
    else:
        if s :
            is_VPS = False
    
    print('YES' if is_VPS else 'NO')