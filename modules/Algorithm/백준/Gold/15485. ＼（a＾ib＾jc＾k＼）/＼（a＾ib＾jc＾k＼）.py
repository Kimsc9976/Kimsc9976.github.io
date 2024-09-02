import sys
lst = sys.stdin.readline().rstrip()

len_lst = len(lst)
matrix = [[0 for _ in range(len_lst)] for _ in range(3)]
K = 1000000007
cnt_a = 0
cnt_b = 0
cnt_c = 0
for c in range(len_lst):
    if lst[c] == 'a':
        matrix[0][c] = (matrix[0][c-1] * 2 %K + 1)%K
        matrix[1][c] = matrix[1][c-1]
        matrix[2][c] = matrix[2][c-1]
    elif lst[c] == 'b':
        matrix[0][c] = matrix[0][c-1]
        matrix[1][c] = (matrix[0][c-1]+(matrix[1][c-1] * 2 %K))%K # 조합 nCr = n-1Cr + nCr-1 같은 느낌이네
        matrix[2][c] = matrix[2][c-1]
    elif lst[c] == 'c':
        matrix[0][c] = matrix[0][c-1]
        matrix[1][c] = matrix[1][c-1]
        matrix[2][c] = (matrix[1][c-1]+(matrix[2][c-1] * 2 %K)%K)%K

print(matrix[-1][-1])