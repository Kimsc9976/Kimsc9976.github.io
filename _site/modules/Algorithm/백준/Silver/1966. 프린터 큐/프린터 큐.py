import sys
import collections

M = int(sys.stdin.readline())

for i in range(M):
  
  line_len, wheres_t = map(int,sys.stdin.readline().split())
  data = map(int,sys.stdin.readline().split())
  get_line = list(enumerate(data))

  get_line = collections.deque(get_line)
  get_mine = get_line[wheres_t]
  
  poped = None
  cnt = 0
  while (get_mine in get_line):
    main = max(get_line,key=lambda x : x[1])
    
    if(main[1] == min(get_line,key=lambda x : x[1])[1]):
      break
    
    i = 0
    idx = get_line.index(main)
    while i < idx:
      get_line.append(get_line.popleft())
      i += 1
    poped = get_line.popleft()
    cnt += 1
  
  if (poped == get_mine):
    print(cnt)
  else:
    left = get_line.index(get_mine)
    print(cnt + left + 1)