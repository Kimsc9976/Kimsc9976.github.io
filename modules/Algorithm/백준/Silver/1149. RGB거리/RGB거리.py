import sys

N = int(sys.stdin.readline())

ans = [0 for _ in range(3)]


for i in range(N):
  RGB = list(map(int,sys.stdin.readline().split()))
  if i == 0:
    ans[0] = RGB[0]
    ans[1] = RGB[1]
    ans[2] = RGB[2]
    continue

  R = (min(ans[1], ans[2]) + RGB[0])
  G = (min(ans[0], ans[2]) + RGB[1])
  B = (min(ans[0], ans[1]) + RGB[2])
  ans[0], ans[1], ans[2] = R, G, B
print(min(ans))