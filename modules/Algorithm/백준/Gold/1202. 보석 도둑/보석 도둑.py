import sys
import heapq
# https://www.acmicpc.net/problem/1202
N, K = map(int, sys.stdin.readline().split())

jams = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(jams, [M, V]) # 무게별로 push

bags = list(int(sys.stdin.readline()) for _ in range(K))
bags.sort()

# print(N,K)
# print(*jams, sep='\n')
# print(bags)

bag_cargo = []
ans = 0
for idx, bag in enumerate(bags):
    while jams and (bag >= jams[0][0]):
        jam = heapq.heappop(jams)
        heapq.heappush(bag_cargo, -jam[1]) # 가중치별로 push
        
    if bag_cargo:
        ans -= heapq.heappop(bag_cargo)
    elif not jams:
        break


print(ans)