import heapq

def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, (0, start))
    d[start] = 0
    path = [-1] * (N + 1)

    while heap:
        check, i = heapq.heappop(heap)
        
        if d[i] < check:
            continue

        for v, w in adj[i]:
            tmp = w + check
            if d[v] > tmp:
                d[v] = tmp
                path[v] = i  # 경로 저장
                heapq.heappush(heap, (tmp, v))

    return d[end], path

def reconstruct_path(start, end, path):
    rev_path = []
    while end != start:
        rev_path.append(end)
        end = path[end]
    rev_path.append(start)
    return rev_path[::-1]  # 경로 뒤집기

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append([e, w])

start, end = map(int, input().split())

d = [100000*1000] * (N+1)
min_cost, path = dijkstra(start, end)
route = reconstruct_path(start, end, path)

print(min_cost)
print(len(route))  # 경로에 포함된 노드 수
print(*route)  # 최단 경로 출력
