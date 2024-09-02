import sys
import heapq

def dijkstra(start):
    que = []
    heapq.heappush(que, (0,start))
    dist[start] = 0

    while que:
        d, now = heapq.heappop(que)

        if dist[now] < d: continue

        for node in groups[now]:
            cost = d + node[1]
            if cost < dist[node[0]]:
                dist[node[0]] = cost
                heapq.heappush(que,(cost,node[0]))

V, E = map(int,input().split())
S = int(input())
dist = [float('inf') for _ in range(V+1)]
groups = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, v = map(int,input().split())
    groups[s].append([e,v])


dijkstra(S)
for i in range(1,V+1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])