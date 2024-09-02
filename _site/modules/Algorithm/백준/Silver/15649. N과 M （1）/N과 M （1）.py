import sys

def NM(n, m):
  N, M = n+1, m
  is_used = list()
  
  def bt(used):
    if len(used) >= M:
      print(*used)
      return
    for i in range(1, N):
      if i in used :
        continue
      used.append(i)
      bt(used)
      used.pop()

  for i in range(1, N):
    is_used.append(i)
    bt(is_used)
    is_used.pop()


NM(*map(int,sys.stdin.readline().split()))