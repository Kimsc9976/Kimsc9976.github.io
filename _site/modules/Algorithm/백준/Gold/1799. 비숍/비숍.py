N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * (N * 3) for _ in range(2)]


def recur(row, col, cnt):
    global ans

    if N % 2:  # 짝수일때
        if col == N:
            row += 1
            col = 0
        elif col == N + 1:
            row += 1
            col = 1
    else:  # 홀수일때
        if col == N:
            row += 1
            col = 1
        elif col == N + 1:
            row += 1
            col = 0

    if row == N:
        if ans < cnt:
            ans = cnt
        return
    # 해당 위치에 비숍을 놓을 수 있고 오른쪽대각선은 열과 행의 합이 다똑같기 때문에 row + col
    # 왼쪽대각선은 열과 행의 차(row - col)가 똑같다. 즉, 방문처리를 다음과 같이 한번에 해준다.
    if arr[row][col] == 1 and not visited[0][row + col] and not visited[1][row - col]:
        visited[0][row + col] = True
        visited[1][row - col] = True
        recur(row, col + 2, cnt + 1)
        visited[0][row + col] = False
        visited[1][row - col] = False

    recur(row, col + 2, cnt)


ans = 0
recur(0, 0, 0)
Bcnt = ans  # 검은색인 경우
ans = 0
recur(0, 1, 0)
Wcnt = ans  # 흰색인 경우

print(Bcnt + Wcnt)