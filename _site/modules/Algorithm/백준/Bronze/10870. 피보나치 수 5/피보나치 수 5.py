N = int(input())

def fect(Num):
  if Num == 0:
    return 0
  if Num == 1:
    return 1
  
  return fect(Num-2) + fect(Num-1)
    
print(fect(N))