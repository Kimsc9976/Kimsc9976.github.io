import sys
# https://www.acmicpc.net/problem/9252

texts = sys.stdin.readlines()
len_text = 0
for idx in range(len(texts)):
    texts[idx] = texts[idx].strip()
    len_text = max(len_text, len(texts[idx]))

N = len(texts)

for j in range(len_text):
    for i in range(N):
        try:
            print(texts[i][j],end='')
        except:
            continue