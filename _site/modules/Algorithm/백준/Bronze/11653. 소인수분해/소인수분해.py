import math
import sys

N = int(sys.stdin.readline())

def isPrime(num):
  for i in range(2, int(math.sqrt(num)+1)):
    if num % i == 0:
      return False
  return True
div = 2

if N != 1:
  if(isPrime(N)):
    print(N)

  while not isPrime(N):
    if (isPrime(div)):
      while N % div == 0:
        print(div)
        N //= div
    div += 1
    if(isPrime(N) and N != 1):
      print(N)