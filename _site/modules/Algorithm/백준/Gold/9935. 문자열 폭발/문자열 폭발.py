import sys

text = sys.stdin.readline().rstrip()
bmb = sys.stdin.readline().rstrip()
b = len(bmb)
ans = list()

for i in range(len(text)):
  ans.append(text[i])
  # print(ans[-b:]) # ㅋㅋㅋㅋ ans[-b]는 error나는데 ans[-b:]는 error 가 안남 
  if ''.join(ans[-b:]) == bmb:
    for _ in range(b):
        ans.pop()
if ans:
  print(''.join(ans))
else:
  print('FRULA')
  