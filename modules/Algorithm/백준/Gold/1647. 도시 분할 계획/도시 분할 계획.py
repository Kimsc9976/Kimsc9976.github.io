import sys

N, M = map(int, sys.stdin.readline().split())
  
parent = [i for i in range(N+1)] # 각 노드는 자신이 부모노드일 수 있다 따라서 이렇게 시작함

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
graph = []
for _ in range(M):
    graph.append([int(x) for x in sys.stdin.readline().rstrip().split()]) # S E C 형식으로 Graph 쪼개기

graph.sort(key= lambda x:x[2]) # 가중치 기준으로 오름차순

result = 0
max_cost = 0

for edge in graph:
    start, end, cost = edge
    if find_parent(start) != find_parent(end):
        union(start, end)
        result += cost
        max_cost = max(cost, max_cost)
        
print(result - max_cost)