import math
import sys
T = int(sys.stdin.readline())

for _ in range(T):
  x,y = map(int,sys.stdin.readline().split())
  distance = y - x

  sqrt = math.floor(math.sqrt(distance))
  ran_min = sqrt**2
  ran_max = sqrt**2 + sqrt
  ran = (sqrt+1)**2

  ans = None
  if(distance == ran_min):
    ans = 2*sqrt - 1  
  elif(distance > ran_min and distance <= ran_max):
    ans = 2*sqrt
  elif(distance > ran_max):
    ans = 2*sqrt + 1
  print(ans)