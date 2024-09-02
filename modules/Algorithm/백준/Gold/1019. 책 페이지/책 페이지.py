
N = int(input())
lst = [ 0 for _ in range(10)]

# 0,1,2,3,4,5,6,7,8,9
# 10, 11,12,13,14,15,16,17,18,19
# 20, 21,22,23,24,25,26,27,28,29
# ...
# 100
def calc(n, ten):
    while (n > 0):
        lst[n%10] += ten
        n //= 10

def solve(A, B, ten):
    while (A% 10 != 0 and A<=B):
        calc(A,ten)
        A += 1
    if (A > B) : return

    while (B% 10 != 9 and B>=A):
        calc(B,ten)
        B -= 1
    cnt = (B // 10 - A // 10 + 1)

    for i in range(10):
        lst[i] += cnt * ten

    solve(A//10, B//10, ten*10)
solve(1, N, 1)
print(*lst)