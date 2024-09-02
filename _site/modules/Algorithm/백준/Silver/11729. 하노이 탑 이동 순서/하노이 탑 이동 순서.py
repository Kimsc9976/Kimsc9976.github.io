N = int(input())

def move(Num):
  return (2**Num) - 1

print(move(N))
def hanoi(Num,start,target,waypoint):
  if Num == 1:
    print(start,target)
  else:
    hanoi(Num-1,start,waypoint,target)
    print(start,target)
    hanoi(Num-1,waypoint,target,start)
  return ''

print(hanoi(N,1,3,2))