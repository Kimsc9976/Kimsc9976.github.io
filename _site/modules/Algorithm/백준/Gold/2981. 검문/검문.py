import sys
import math
T = int(sys.stdin.readline())

Num = [int(sys.stdin.readline()) for _ in range(T)]
Num.sort()
subed = []
for i in range(0,T-1):
  subed.append(Num[i+1] - Num[i])
gcd = math.gcd(*subed)
ans = set({gcd})
for i in range(2, int(gcd**0.5)+1):
  if gcd % i == 0:
    ans.add(i)
    ans.add(gcd//i)
print(*sorted(list(ans)))
