import sys

N = int(sys.stdin.readline())
A = [[1, 1], [1, 0]]

def pw_m(m1 : list, m2 : list):
  result = [[0]*2 for _ in range(2)]
  for i in range(2):
    for j in range(2):
      for k in range(2):
        result[i][j] += (m1[i][k] * m2[k][j]) % 1000000007
  return result


def dac(num : int ,matrix : list):
  if num == 1: return matrix
  mat = dac(num // 2, matrix)
  return pw_m(mat, mat) if num%2 ==0 else pw_m(pw_m(mat, mat),matrix)

ans = dac(N, A)
print(ans[0][1]%1000000007) 