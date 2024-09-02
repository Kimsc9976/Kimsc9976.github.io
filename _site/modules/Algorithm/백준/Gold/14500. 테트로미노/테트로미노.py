N,M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

from itertools import combinations

dx = (0,0,-1,1)
dy = (1,-1,0,0)
def check(tetromino):
  cnt = 0
  for a,b in tetromino:
    for k in (0,1,2,3):
      na = a+dx[k]
      nb = b+dy[k]
      if na<0 or nb<0 or na>=N or nb>=M: continue
      if (na,nb) in tetromino:
        cnt += 1
  return True if cnt >= 6 else False


tetromino = set()

result = 0
mx_col = 0
mx_row = 0
for items in combinations(range(0,8), 4):
  tet_col = tuple()
  tet_row = tuple()
  ## 테트로미노 찾기
  for idx in items:
    ## col_case
    r_r = idx // 2
    r_c = idx % 2
    tet_col += ((r_r,r_c),)
    ## row_case
    c_r = idx//4
    c_c = idx%4
    tet_row += ((c_r,c_c),)
    
  ## col 방향 테트로미노에 대해서
  if check(tet_col): 
    for i in range(N - 3):
      for j in range(M - 1):
        _sum = 0
        for x,y in tet_col:
          _sum += matrix[i+x][j+y]
        mx_col = _sum if _sum > mx_col else mx_col
    
  ## row 방향 테트로미노에 대해서
  if check(tet_row): 
    for i in range(N - 1):
      for j in range(M - 3):
        _sum = 0
        for x,y in tet_row:
          _sum += matrix[i+x][j+y]
        mx_row = _sum if _sum > mx_row else mx_row
  
  result = max(result,mx_col,mx_row)
print(result)
