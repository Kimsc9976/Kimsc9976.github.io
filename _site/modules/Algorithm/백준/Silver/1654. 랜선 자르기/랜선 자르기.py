import math

import sys
M,N = map(int,sys.stdin.readline().split())

l_lst = []
for i in range(M):
  line = int(sys.stdin.readline())
  l_lst.append(line)
l_lst.sort()
pred = sum(l_lst)

cnt = 0
start = 1
mid = 0
end = l_lst[-1]
while start <= end : # cnt < N:
  
  mid = (start+end) // 2
  
  cnt = 0
  for line in l_lst:
    cnt += line // mid

  if cnt >= N:
    start = mid + 1
  elif cnt < N:
    end = mid - 1
print(start-1)