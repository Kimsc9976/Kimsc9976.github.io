N, K = map(int,input().split())
from collections import deque
conv = deque(map(int,input().split()))

# 올리는 위치는 -1 씩 계속 진행
# 내리는 위치 역시 -1 씩 계속 진행



def c1():
  global conv
  conv.appendleft(conv.pop())
  conv[N-1][1] = 0
  pass


def c2():
  for i in range(N-1, 0, -1):
    if conv[i-1][1] == 1:
      if conv[i][0] != 0 and conv[i][1] != 1: # 컨베이어가 0이 아니고 로봇이 없을 경우
        conv[i][0] -= 1
        conv[i][1] = 1
        conv[i-1][1] = 0
        
  conv[N-1][1] = 0
  pass


def c3():
  if conv[0][0] != 0:
    conv[0][0] -= 1
    conv[0][1] = 1


def c4():
  cnt_zero = 0
  for x, y in conv:
    if x == 0 :
      cnt_zero += 1
  return True if cnt_zero < K else False



for k in range(len(conv)):
  conv[k] = [conv[k], 0]

trial = 0
Trigger = True
while Trigger:
  c1()
  c2()
  c3()
  Trigger = c4()
  trial += 1
  
print(trial)