A, B, C = map(int, input().split())
def pow(a,b):
  if b == 1: return a % C
  temp = pow(a,b//2)
  return (temp * temp) % C if (b%2 ==0) else (temp * temp * a) % C
print(pow(A,B))