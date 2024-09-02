import sys

N, M = map(int, sys.stdin.readline().split()) 
num_lst = sorted(list(map(int, sys.stdin.readline().split())))

lst = num_lst.copy()

def NM(target):
  
  is_used = list()
  def bt(depth,is_used):
    if len(is_used) == M:
      print(*is_used)
      return
    
    for i in range(depth, len(target)):
      is_used.append(target[i])
      bt(i,is_used)
      is_used.pop()
  bt(0,is_used)

NM(lst)