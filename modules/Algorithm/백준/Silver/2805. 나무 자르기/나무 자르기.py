import sys
M,N = map(int,sys.stdin.readline().split())

l_lst = list(map(int,sys.stdin.readline().split()))
l_lst.sort()

cnt = 0
start = 1
mid = 0
end = l_lst[-1]
i = 0
while start <= end : # cnt < N:
  
  mid = (start+end) // 2 ## 얼마만큼 남길지
  cnt = 0
  for line in l_lst:
    if (line - mid) >= 0:
      cnt += (line - mid)
  
  if cnt >= N: # 더 잘렸을 경우 mid를 높여야함
    start = mid + 1 
  elif cnt < N: # 덜 잘렸을 경우 mid를 낮춰야함
    end = mid - 1

  
print(start - 1)