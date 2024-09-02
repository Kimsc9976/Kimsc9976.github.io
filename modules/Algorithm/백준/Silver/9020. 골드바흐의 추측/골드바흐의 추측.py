import sys
T = int(sys.stdin.readline())

import math
def isPrime(num):
  
  for i in range(2, int(math.sqrt(num)+1)):
    if num % i == 0:
      return False
  return True


for idx in range(T):
  
  num = int(sys.stdin.readline())

  
  a = num//2
  b = num//2
  b_save = b
  while True:
    # 짝수니까 반반나누는거 가능
    if (isPrime(a) and isPrime(b)):
      print(f'{a} {b}')
      break
    a -= 1
    b += 1