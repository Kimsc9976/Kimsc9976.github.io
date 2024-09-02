import sys
N, M = map(int, sys.stdin.readline().split()) 
num_lst = sorted(list(map(int, sys.stdin.readline().split())))

def NM(target):
  check = set()
  is_used = list()
  is_true = [True for _ in range(len(target))]
  
  def bt(depth, is_used : list):
    nonlocal check, is_true
    if len(is_used) == M:
      print(' '.join(map(str,is_used)))
      return
    remember = -1 
    for i in range(depth, len(target)):
      if (is_true[i] == False)or (remember == target[i]):
        continue
      is_true[i] = False
      is_used.append(target[i])
      remember = target[i]
      bt(i + 1, is_used)
      is_true[i] = True
      is_used.pop()

  bt(0, is_used)
  
NM(num_lst)