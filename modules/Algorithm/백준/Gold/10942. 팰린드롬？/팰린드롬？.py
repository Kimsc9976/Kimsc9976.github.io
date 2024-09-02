import sys
N = int(sys.stdin.readline())

# seg_tree = [0]*(4*N)
points = list(map(int,sys.stdin.readline().split()))

# def tree(idx, start, end):
#     if start == end:
#         seg_tree[idx] = 1
#         return
#     mid = (start + end) // 2
#     tree(idx*2, start, mid)
#     tree(idx*2+1, mid+1, end) 

# tree(1, 1, N)

check = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for start in range(N - i):
        end = start + i
        if start == end: check[start][end] = 1
        elif points[start] == points[end]:
            if start + 1 == end : check[start][end] = 1
            elif check[start + 1][end - 1]: check[start][end] = 1


M = int(sys.stdin.readline())

for _ in range(M):
    S, E = map(int,sys.stdin.readline().split())

    print(check[S-1][E-1])