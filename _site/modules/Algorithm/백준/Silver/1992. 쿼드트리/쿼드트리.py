T = int(input())

matrix = []

for _ in range(T):
  row = list(map(int,list(input().strip())))
  matrix.append(row)

def is_full(mat: list, n):
  target = mat[0][0] 
  for i in range(n):
    for j in range(n):
      if mat[i][j] != target: return (False, -1)
  return (True, target)

def slc(mat, row:tuple, col:tuple):
  node = []
  for i in range(row[0],row[1]):
    node.append(mat[i][col[0]:col[1]])
  return node

def quad_tree(mat, N):
  check = is_full(mat,N)
  if check[0]:
    print(check[1],end="")
    return check[1]
  
  
  root = mat
  n = N//2
  V = (slc(root,(0,n),(0,n)), slc(root,(0,n),(n,N)), slc(root,(n,N),(0,n)), slc(root,(n,N),(n,N)))
  # node1 = root[:n][:n]
  # node3 = root[:n][n:]
  # node2 = root[n:][:n]
  # node4 = root[n:][n:]
  print("(",end="")
  for node in V:
    quad_tree(node,n)
  print(")",end="")


quad_tree(matrix,T)