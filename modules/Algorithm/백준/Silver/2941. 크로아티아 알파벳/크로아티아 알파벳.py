text = input()
croait = ['c=','c-','dz=','d-','lj','nj','s=','z=']
text_char = list(text)
checker = ""

cnt = 0
for i in text_char:
    
    cnt += 1
    
    checker += i
    
    for j in croait:
        
        if (j in checker):
            if j =='dz=':
                cnt -= 2
            else:
                cnt -= 1
            checker = ""
            break

print(cnt)