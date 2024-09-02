N, M = map(int, input().split())
cakes = list(map(int, input().split()))

tens = [cake for cake in cakes if cake % 10 == 0]
not_tens = [cake for cake in cakes if cake % 10 != 0]

tens.sort()
not_tens.sort()

ans = 0

for cake in tens:
    if M <= 0:
        break
    pieces = cake // 10
    if pieces-1 <= M:
        M -= (pieces-1)
        ans += pieces
    else:
        ans += M
        M = 0

for cake in not_tens:
    if M <= 0:
        break
    pieces = cake // 10
    if pieces <= M:
        M -= pieces
        ans += pieces
    else:
        ans += M
        M = 0

print(ans)