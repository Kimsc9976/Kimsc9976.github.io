import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())


num_list = []
for idx in range(M,N+1):
    if(idx <= 1):
        continue
  
    trigger = 0
    for i in range(2,idx):
        if idx % i == 0:
            trigger = 1
            break
    
    if trigger == 1:
        continue
    else:
        num_list.append(idx)
      
if(len(num_list)):
  print(sum(num_list))
  print(min(num_list))
else:
  print(-1)