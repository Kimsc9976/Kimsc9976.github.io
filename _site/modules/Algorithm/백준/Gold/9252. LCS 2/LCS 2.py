import sys
# https://www.acmicpc.net/problem/9252

text1 = [''] + list(sys.stdin.readline().rstrip())
text2 = [''] + list(sys.stdin.readline().rstrip())

l1 = len(text1)
l2 = len(text2)

LCS = [['']*l2 for _ in range(l1)]

for i in range(1,l1):
    for j in range(1,l2):
        if text1[i] == text2[j]:
            LCS[i][j] = LCS[i-1][j-1] + text1[i]
        else:
            if len(LCS[i-1][j]) > len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]
result = LCS[-1][-1]
print(len(result))
print(result)