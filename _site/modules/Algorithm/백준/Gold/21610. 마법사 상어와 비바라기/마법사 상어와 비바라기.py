N, M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

d = ((0,0),
    (0,-1),(-1,-1),(-1,0),(-1,1),
    (0,1),(1,1),(1,0),(1,-1))

controller = []
for i in range(M):
  controller.append(list(map(int,input().split())))
cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

def move_and_rain(item):
  new_cloud = []
  for cl_x, cl_y in cloud:
    nx = cl_x + d[item[0]][0]*item[1]
    ny = cl_y + d[item[0]][1]*item[1]
    
    if nx < 0:
      nx = nx%N
    elif nx >= N:
      nx = nx%N
    
    if ny < 0:
      ny = ny%N
    elif ny >= N:
      ny = ny%N
      
    matrix[nx][ny] += 1
    new_cloud.append((nx,ny))
  return new_cloud

dev = ((-1,-1),(-1,1),(1,-1),(1,1))
def ctrl_c_ctrl_v(CLOUD):
  
  for cl_x, cl_y in CLOUD:    
    for k in (0,1,2,3):  
      nx = cl_x + dev[k][0]
      ny = cl_y + dev[k][1]

      if nx < 0 or nx >= N or ny < 0 or ny >= N : continue
      
      if matrix[nx][ny] != 0:
        matrix[cl_x][cl_y] += 1

def make_cloud(CLOUD):
  cld = []
  K = []
  for a, b in CLOUD:
    K.append(matrix[a][b])
    matrix[a][b] -= matrix[a][b]
  
  for i in range(N):
    for j in range(N):
      if matrix[i][j] >= 2:
        cld.append((i,j))
        matrix[i][j] -= 2

  for i in range(len(CLOUD)):
    matrix[CLOUD[i][0]][CLOUD[i][1]] += K[i]
  return cld


# cloud = [(N,1),(N,2),(N-1,1),(N-1,2)]
for control in controller:
  cloud = move_and_rain(control)
  ctrl_c_ctrl_v(cloud)
  cloud = make_cloud(cloud)

cnt = 0
for i in range(N):
  for j in range(N):

    cnt += matrix[i][j]
print(cnt)