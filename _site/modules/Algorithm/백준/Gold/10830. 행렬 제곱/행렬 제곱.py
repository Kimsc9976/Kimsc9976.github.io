import sys

N, B = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def pw_m(m1 : list, m2 : list):
  result = [[0]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      for k in range(N):
        result[i][j] += (m1[i][k] * m2[k][j])%1000
  return result

def dac(num : int ,matrix : list):
  if num == 1: return matrix
  mat = dac(num // 2, matrix)
  return pw_m(mat, mat) if num%2 ==0 else pw_m(pw_m(mat, mat),matrix)

ans = dac(B, A)
for row in ans : 
  for col in row:
    print(col%1000,end=" ")
  print()