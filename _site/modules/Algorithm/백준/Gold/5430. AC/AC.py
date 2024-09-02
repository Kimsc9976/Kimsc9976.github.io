import sys

T = int(sys.stdin.readline())

for i in range(T):
  graph = sys.stdin.readline().rstrip()
  len_graph = len(graph)
  len_lst = int(sys.stdin.readline())
  lst = sys.stdin.readline().rstrip()
  if lst != '[]':
    lst = list(lst[1:-1].split(','))
  else:
    lst = []
  
  cnt = 0
  trigger = False
  for j in range(len_graph):
    try:
      if graph[j] == 'R':
        cnt += 1
      elif graph[j] == 'D':
        if cnt % 2 == 0:
          lst.pop(0)
        if cnt % 2 == 1:
          lst.pop()
    except:
      trigger = True
      break
  ans = None
  if trigger == False:
    if cnt % 2 == 0:
      ans = '['+','.join(lst)+']'
    if cnt % 2 == 1:
      lst.reverse()
      ans = '['+','.join(lst)+']'
  else:
    ans = 'error'
  print(ans)