from collections import deque

N,W,L = map(int,input().split())

start = deque(map(int,input().split()))
bridge = deque([0 for _ in range(W)])

cnt = 0
while start or bridge:
    bridge.popleft()
    if len(start):
        for i in range(len(start)):
            temp = start[i]
            if int(sum(bridge) + temp)> L:
                bridge.append(0)
                break
            else:
                start.remove(temp)
                bridge.append(temp)
                trigger = True
                break
    cnt+=1
print(cnt)