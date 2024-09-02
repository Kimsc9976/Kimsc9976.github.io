import sys
from collections import deque
Ns = list(map(int,sys.stdin.readlines()))[:-1]



def solve(N):
    bins = ['1','0']
    que = deque(bins)
    ans = []
    
    while que:
        now = que.popleft()

        for b in bins:
            next_ = b + now
            if int(next_) and int(next_) % N == 0:
                return next_
            else:
                que.append(next_)
    return

for N in Ns:
    x = solve(N)
    print(x)