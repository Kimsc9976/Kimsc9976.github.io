nanj = list()
for _ in range(9):
    nanj += [int(input())]

trigger = False
for i in range(9):
    temp_i = nanj[i]
    nanj.pop(i)
    for j in range(8):
        temp_j = nanj[j]
        nanj.pop(j)
        
        if sum(nanj) == 100:
            print(*sorted(nanj),sep='\n')
            trigger = True
            break
        nanj.insert(j,temp_j)
    
    if trigger :
        break
    nanj.insert(i,temp_i)
