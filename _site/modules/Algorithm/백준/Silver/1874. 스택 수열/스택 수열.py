import sys
M = int(sys.stdin.readline())

number = 1
cnt = 0
lst = []
ls = []
compare = []
ans = []
i = 0
while i < M:
  target = int(sys.stdin.readline())
  compare.append(target)
  while number <= target:
    lst.append(number)
    ans.append('+')
    number += 1
  
  try:
    while lst[-1] >= target:
      ls.append(lst.pop())
      ans.append('-')
  except:
    pass
    
  i += 1

is_correct = True
for i in range(M):
  if(ls[i] != compare[i]):
    is_correct = False
    break
  
if is_correct:
  for i in range(len(ans)):
    print(ans[i])
else:
  print('NO')
