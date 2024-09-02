import sys
N,M = map(int,sys.stdin.readline().split())


N_lst = []
for _ in range(N):
  row = list(map(int,sys.stdin.readline().split()))
  N_lst.append(row)

M_lst = []
for _ in range(N):
  row = list(map(int,sys.stdin.readline().split()))
  M_lst.append(row)
  

for i in range(N):
  for j in range(M):
    print(N_lst[i][j] + M_lst[i][j], end=" ")
  print()
