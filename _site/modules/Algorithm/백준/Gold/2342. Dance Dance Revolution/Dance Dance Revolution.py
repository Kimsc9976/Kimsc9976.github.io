import sys
move = list(map(int,sys.stdin.readline().split()))[:-1]
N = len(move)


def cost(end, start):
    if start == 0:
        if end == 0: return 0
        else : return 2
    elif start == end : return 1
    elif abs(start - end) == 1 or abs(start - end) == 3: return 3
    else : return 4

dp = [[[float('inf') for _ in range(5)] for _ in range(5)] for _ in range(N + 1)]
dp[-1][0][0] = 0 # 마지막 지점에 발이 0,0 에 위치할 수는 없음.

if N == 0:
    print(0)
else:
    for i in range(N):
        # l = move[i], 왼발로 이번 위치 누를 때
        for r in range(5):  # 왼발이 움직이니 오른발은 고정
            for k in range(5):  # k 는 왼발의 이전 위치.
                add = cost(move[i], k)  # 왼발이 k에서 move[i]로 움직일 때 드는 비용
                dp[i][move[i]][r] = min(dp[i][move[i]][r], dp[i - 1][k][r] + add)

        # r = move[i], 오른발로 이번 위치 누를 때
        for l in range(5):  # 오른발이 움직이니 왼발은 고정
            for k in range(5):  # k는 오른발의 이전 위치.
                add = cost(move[i], k)  # 오른발이 k에서 move[i]로 움직일 때 드는 비용
                dp[i][l][move[i]] = min(dp[i][l][move[i]], dp[i - 1][l][k] + add)

    m = float('inf')
    for l in range(5):
        for r in range(5):
            m = min(m, dp[N - 1][l][r])
    print(m)