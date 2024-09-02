import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    global result
    visited[node] = True
    cycle.append(node)  # 사이클을 형성하는 노드 저장
    next_node = _list[node]

    if visited[next_node]:
        if next_node in cycle:  # 사이클이 형성된 경우
            result += cycle[cycle.index(next_node):]  # 사이클에 포함된 노드만 결과에 추가
        return
    else:
        dfs(next_node)

T = int(sys.stdin.readline().split()[0])
for _ in range(T):
    n = int(sys.stdin.readline().split()[0])
    _list = [0]+list(map(int, sys.stdin.readline().split()))
    visited = [False] * (n + 1)
    result = []

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(result))