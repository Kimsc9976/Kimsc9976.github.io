import math
import sys
def rnd(num):
  flr = math.floor(num)
  return flr + 1 if(num >= flr + 0.5) else flr

T = int(sys.stdin.readline())

num_sum = 0
num_list = dict()
for i in range(T):
  num = int(sys.stdin.readline())
  if (not num_list.get(num)):
    num_list.setdefault(num,0)
  num_list[num] += 1
  num_sum += num

AVG = rnd(num_sum/T)
lst_mode = sorted(list(num_list.items()), key=lambda x: (x[1], - x[0]),reverse=True)
lst_minMax = sorted(list(num_list.items()), key=lambda x: (x[0], x[1]),reverse=True)

if len(lst_mode) == 1:
  MODE = lst_mode[0][0]
else:
  MODE = lst_mode[0][0] if (lst_mode[0][1] != lst_mode[1][1]) else lst_mode[1][0]
mid = T//2
cnt = 0
MID = None
for idx, counted in lst_minMax:
  cnt += counted
  if cnt > mid:
    MID = idx
    break

RNG = lst_minMax[0][0] - lst_minMax[-1][0]
print(AVG, MID, MODE, RNG, sep="\n")