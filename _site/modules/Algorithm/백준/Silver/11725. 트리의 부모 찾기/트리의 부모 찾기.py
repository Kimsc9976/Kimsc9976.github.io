import sys
sys.setrecursionlimit(10000000)

N = int(input())
rlt = [list(map(int,input().split())) for i in range(N-1)]

nodes = [list() for o in range(N+1)]
for i in range(N-1):
    nodes[rlt[i][0]].append(rlt[i][1])
    nodes[rlt[i][1]].append(rlt[i][0])
is_traveled = [False for _ in range(N+1)]
ans = [0 for _ in range(N+1)]
def inorder(v):
    # if v= 1 일 겨우에는 -> 6번하고 4번이
    # if v= 6 일 경우에는 -> 1하고 3 // 아니? 1은 부모아니였어?
    for node in nodes[v]: # -> 모르겠으니까 for문을 돌린거야
        if is_traveled[node] == True:
            continue
        is_traveled[node] = True
        inorder(node) # -> 6번하고 4번 탐색 할 수 있겠찌
        # 우리가 원하는 수식 == 이친구의 부모 노드가 뭐야!!!
        # 이곳에서 우리는 알 수 있다!
        ans[node] = v

    
is_traveled[1] = True
inorder(1)
    
for idx in range(2,N+1):
    print(ans[idx])